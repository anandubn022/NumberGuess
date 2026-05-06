async function guessSend() {
    const userGuess = document.getElementById("userGuess").value;
    const response = await fetch('/guess', {method:POST, headers:{'Content-Type':'application/json'}, body:JSON.stringify({userGuess:userGuess})});
    const data = await response.json();
    document.getElementById("systemOutput").value = data.message;
}