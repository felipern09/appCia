function x(obj){

if((obj).classList.contains('liked')==true){
    (obj).setAttribute('class', 'button-like');
    fetch("/home", {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "post_id": obj.id,
      "curtir": 'False',
    })
    })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
//    location.reload(obj);
}else if((obj).classList.contains('button-like')==true){
    (obj).setAttribute('class', 'button-like liked');
    fetch("/home", {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "post_id": obj.id,
      "curtir": 'True',
    })
    })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
//    location.reload(obj);
}
}

function y(obj){
    fetch("/substit", {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "botao_id": obj.id,
      "autorizado": 'True',
    })
    })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
    console.log(obj.id)
}

function z(obj){
    fetch("/substit", {
    method: 'POST',
    headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "botao_id": obj.id,
      "autorizado": 'False',
    })
    })
    .then(response => response.json())
    .then(response => console.log(JSON.stringify(response)))
    console.log(obj.id)
}
