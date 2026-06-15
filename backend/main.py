from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from langchain_google_genai import ChatGoogleGenerativeAI

import shutil
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

vectorstore = None


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def health():
    return {"status": "running"}


@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    global vectorstore

    os.makedirs("data", exist_ok=True)

    file_path = f"data/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    loader = PyPDFLoader(file_path)

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = splitter.split_documents(documents)

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="./db"
    )

    return {
        "message": "PDF uploaded successfully",
        "chunks": len(chunks)
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    global vectorstore

    if vectorstore is None:
        return {
            "error": "Please upload a PDF first."
        }

    results = vectorstore.similarity_search(
        request.question,
        k=2
    )

    context = "\n\n".join(
        [doc.page_content for doc in results]
    )

    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash"
    )

    prompt = f"""
    Answer only using the context below.

    Context:
    {context}

    Question:
    {request.question}
    """

    response = llm.invoke(prompt)

    return {
        "answer": response.content
    }