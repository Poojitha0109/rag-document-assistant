async function uploadPdf() {

    const fileInput =
        document.getElementById("pdfFile");

    const formData =
        new FormData();

    formData.append(
        "file",
        fileInput.files[0]
    );

    const response =
        await fetch(
            "http://localhost:8000/upload",
            {
                method: "POST",
                body: formData
            }
        );

    const data =
        await response.json();

    document.getElementById(
        "status"
    ).innerText =
        "✅ PDF uploaded successfully";
}


async function askQuestion() {

    const questionInput =
        document.getElementById("question");

    const question =
        questionInput.value;

    const chatBox =
        document.getElementById("chatBox");

    chatBox.innerHTML += `
        <div class="message">
            <div class="user">${question}</div>
        </div>
    `;

    questionInput.value = "";

    const response =
        await fetch(
            "http://localhost:8000/ask",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    question
                })
            }
        );

    const data =
        await response.json();

    chatBox.innerHTML += `
        <div class="message">
            <div class="ai">${data.answer}</div>
        </div>
    `;

    chatBox.scrollTop =
        chatBox.scrollHeight;
}