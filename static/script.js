document.getElementById("predict-btn").addEventListener("click", () => {
    const smsText = document.getElementById("smsText").value.trim();
    const resultDiv = document.getElementById("result");
    const spinner = document.getElementById("loading-spinner");

    resultDiv.innerText = "";
    resultDiv.className = "result-text";
    spinner.style.display = "block";

    if (!smsText) {
        spinner.style.display = "none";
        resultDiv.innerText = "Please enter a message.";
        return;
    }

    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ email: smsText })
    })
    .then(response => {
        if (!response.ok) throw new Error("Server error.");
        return response.json();
    })
    .then(data => {
        spinner.style.display = "none";
        const prediction = data.prediction?.toLowerCase() || "Unexpected result";

        resultDiv.className = prediction === "spam"
            ? "result-text result-spam"
            : prediction === "not spam"
                ? "result-text result-ham"
                : "result-text";

        const icon = prediction === "spam" ? "❌ " :
                     prediction === "not spam" ? "✅ " : "";

        typeText(resultDiv, icon + (data.prediction || "Unknown"));
    })
    .catch(error => {
        spinner.style.display = "none";
        resultDiv.innerText = "Error: " + error.message;
        resultDiv.className = "result-text";
    });
});

function typeText(element, text, i = 0) {
    element.innerText = text.slice(0, i);
    if (i < text.length) {
        setTimeout(() => typeText(element, text, i + 1), 50);
    }
}
