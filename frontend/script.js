document.getElementById("predictButton").addEventListener("click", async () => {
	const text = document.getElementById("textInput").value;
	var resultElement = document.getElementById("result");

	if (!text.trim()) {
		resultElement.textContent = "Please enter some text.";
		return;
	}

	try {
		const response = await fetch(
			"http://127.0.0.1:8000/predict/" + encodeURIComponent(text),
			{
				method: "GET",
			},
		);

		if (!response.ok) {
			throw new Error("Network response was not ok");
		}

		const prediction = await response.text();
		if (String(prediction).trim() == "1") {
			resultElement.textContent = "The text is toxic.";
		} else if (prediction.trim() == "0") {
			resultElement.textContent = "The text is not toxic.";
		}
	} catch (error) {
		resultElement.textContent = "An error occurred. Please try again.";
		console.error("Error:", error);
	}
});
