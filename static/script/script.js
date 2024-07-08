const analyzeButton = document.querySelector('.analyze-btn');
const predictionSpan = document.getElementById('prediction');

analyzeButton.addEventListener('click', (event) => {
  event.preventDefault(); // Prevent default form submission

  // Get user input from the textarea
  const userInput = document.getElementById('text').value;

  // Send the user input to your Flask app using AJAX (Fetch API)
  fetch('/predict', {
    method: 'POST',
    body: JSON.stringify({ text: userInput }), // Send data as JSON
    headers: { 'Content-Type': 'application/json' } // Set content type
  })
  .then(response => response.json()) // Parse JSON response
  .then(data => {
    // Update the prediction display with the received sentiment
    predictionSpan.textContent = data.predicted_sentiment;
  })
  .catch(error => {
    console.error('Error fetching prediction:', error);
    // Handle errors appropriately (e.g., display an error message)
  });
});
