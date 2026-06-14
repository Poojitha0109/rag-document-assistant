from dotenv import load_dotenv
load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI


loader = PyPDFLoader("data/PoojithaPanabakaResume.pdf")

documents = loader.load()

print(f"Pages loaded: {len(documents)}")

splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)

chunks = splitter.split_documents(documents)

print(f"Chunks created: {len(chunks)}")

print("\nFirst Chunk:\n")
print(chunks[0].page_content)

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./db"
)

print("Vector DB created successfully")

question = input("Ask a question: ")

results = vectorstore.similarity_search(
    question,
    k=2
)

print("\nRetrieved Results:\n")

for i, doc in enumerate(results):
    print(f"Result {i+1}")
    print("-" * 50)
    print(doc.page_content)
    print()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash"
)

context = "\n\n".join(
    [doc.page_content for doc in results]
)

prompt = f"""
Answer using only the context below.

Context:
{context}

Question:
{question}
"""

response = llm.invoke(prompt)

print("\nANSWER:")
print(response.content)