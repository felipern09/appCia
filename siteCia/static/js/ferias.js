//import { format, compareAsc } from '../node_modules/date-fns'

var datas = document.getElementById('datas');
var hoje = new Date()

function ferias(){
    datas.innerText = ''
    let col = document.createElement('div');
    col.classList.add('col-3','card4','shadow','p-2', 'ms-5');
    datas.appendChild(col)
    let div1 = document.createElement('div');
    div1.classList.add("divSquare");
    div1.innerHTML = '<p>1º Período:<br></p>De:<br><input type="date" min="{{inicio_min}}"/>';
    col.appendChild(div1);
    let div2 = document.createElement('div');
    div2.classList.add("divSquare");
    div2.innerHTML = 'Até:<br><input type="date" min="{{inicio_min}}" max="{{fim_max}}"/>';
    col.appendChild(div2);
    return datas
}
function ferias2(){
    datas.innerText = ''
    let col = document.createElement('div');
    col.classList.add('col-3','card4','shadow','p-2', 'ms-5');
    datas.appendChild(col)
    let div1 = document.createElement('div');
    div1.classList.add("divSquare");
    div1.innerHTML = '<p>1º Período:<br></p>De:<br><input type="date" min="{{inicio_min}}"/>';
    col.appendChild(div1);
    let div2 = document.createElement('div');
    div2.classList.add("divSquare");
    div2.innerHTML = 'Até:<br><input type="date" min="{{inicio_min}}" max="{{fim_max}}"/>';
    col.appendChild(div2);
    let col2 = document.createElement('div');
    col2.classList.add('col-3','card4','shadow','p-2', 'ms-4');
    datas.appendChild(col2)
    let div3 = document.createElement('div');
    div3.classList.add("divSquare");
    div3.innerHTML = '<p>2º Período:<br></p>De:<br><input type="date" min="{{inicio_min}}"/>';
    col2.appendChild(div3);
    let div4 = document.createElement('div');
    div4.classList.add("divSquare");
    div4.innerHTML = 'Até:<br><input type="date" min="{{inicio_min}}" max="{{fim_max}}"/>';
    col2.appendChild(div4);
    return datas
}
function ferias3(){
    datas.innerText = ''
    let col = document.createElement('div');
    col.classList.add('col-3','card4','shadow','p-2', 'ms-5');
    datas.appendChild(col)
    let div1 = document.createElement('div');
    div1.classList.add("divSquare");
    div1.innerHTML = '<p>1º Período:<br></p>De:<br><input type="date" min="{{inicio_min}}"/>';
    col.appendChild(div1);
    let div2 = document.createElement('div');
    div2.classList.add("divSquare");
    div2.innerHTML = 'Até:<br><input type="date" min="{{inicio_min}}" max="{{fim_max}}"/>';
    col.appendChild(div2);
    let col2 = document.createElement('div');
    col2.classList.add('col-3','card4','shadow','p-2', 'ms-4');
    datas.appendChild(col2)
    let div3 = document.createElement('div');
    div3.classList.add("divSquare");
    div3.innerHTML = '<p>2º Período:<br></p>De:<br><input type="date" min="{{inicio_min}}"/>';
    col2.appendChild(div3);
    let div4 = document.createElement('div');
    div4.classList.add("divSquare");
    div4.innerHTML = 'Até:<br><input type="date" min="{{inicio_min}}" max="{{fim_max}}"/>';
    col2.appendChild(div4);
    let col3 = document.createElement('div');
    col3.classList.add('col-3','card4','shadow','p-2', 'ms-4');
    datas.appendChild(col3)
    let div5 = document.createElement('div');
    div5.classList.add("divSquare");
    div5.innerHTML = '<p>3º Período:<br></p>De:<br><input type="date" min="{{inicio_min}}"/>';
    col3.appendChild(div5);
    let div6 = document.createElement('div');
    div6.classList.add("divSquare");
    div6.innerHTML = 'Até:<br><input type="date" min="{{inicio_min}}" max="{{fim_max}}"/>';
    col3.appendChild(div6);
    return datas
}