async function guessSend() {
    const userGuess = document.getElementById("userGuess").value;
    const upperLimit = document.getElementById("upperlimit").value;
    const response = await fetch('/guess', {method:"POST", headers:{'Content-Type':'application/json'}, body:JSON.stringify({userGuess:userGuess, upperLimit:upperLimit})});
    const data = await response.json();
    document.getElementById("systemOutput").innerText = data.message;
    document.getElementById("usergiveninputcheck").innerText = data.ul;
}