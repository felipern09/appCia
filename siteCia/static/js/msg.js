var msg = document.getElementById('texto-msg');

function mensagem(){
    msg.innerText = ''
    msg.innerHTML = '"{{ item }}"'
//    let col = document.createElement('div');
//    col.classList.add('col-3','card4','shadow','p-2');
//    msg.appendChild(col)
//    let div1 = document.createElement('div');
//    div1.classList.add("divSquare");
//    div1.innerHTML = '<p>Período 1:<br>De:<br></p><input type="date" min="{{inicio_min}}"/>';
//    col.appendChild(div1);
//    let div2 = document.createElement('div');
//    div2.classList.add("divSquare");
//    div2.innerHTML = '<p>Até:<br></p><input type="date" min="{{inicio_min}}" max="{{fim_max}}"/>';
//    col.appendChild(div2);

}
