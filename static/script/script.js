document.addEventListener("DOMContentLoaded", function() {
    const form = document.querySelector("form");
    const resultDiv = document.querySelector("#result");
  
    form.addEventListener("submit", function(event) {
      event.preventDefault();
      const statement = document.querySelector("#statement").value;
      fetch("/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ statement: statement })
      })
      .then(response => response.json())
      .then(data => {
        resultDiv.innerText = `Sentiment: ${data.sentiment}`;
      })
      .catch(error => {
        console.error(error);
      });
    });
  });