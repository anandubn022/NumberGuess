async function guessSend() {
    const userGuess = document.getElementById("userGuess").value;
    const response = await fetch('/guess', {method:"POST", headers:{'Content-Type':'application/json'}, body:JSON.stringify({userGuess:userGuess})});
    const data = await response.json();
    document.getElementById("systemOutput").innerText = data.message;

}

async function limitSend()
{
    const upperLimit = document.getElementById("upperlimit").value;
    const response = await fetch("/limit", {method:"POST", headers:{"Content-Type":'application/json'}, body:JSON.stringify({upperLimit:upperLimit})});
    const data = await response.json();
    document.getElementById("usergiveninputcheck").innerText = data.ul;
}