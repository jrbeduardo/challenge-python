const $submitButton = document.getElementById("send"),
      $response = document.getElementById("response"),
      $formAdjacent = document.getElementById("formAdjacent"),
      URL = "http://127.0.0.1:5000"

document.addEventListener("submit", (e)=>{
  e.preventDefault()
  fetch(`${URL}/adjacent`, {
    method: "POST",
    body: new FormData(e.target)
  })
    .then(res => res.json())
    .then(json => {
      $response.innerHTML = json.msg
      setTimeout(() => {
        $response.innerHTML = ""        
      }, 3000);
    })
})
