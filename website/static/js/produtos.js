
// FUNÇÃO FUNCIONANDO PORÉM IMAGENS NÃO APARECEM

let i = 0;
let images = [];
let time = 3000;
// let voltar = document.querySelector('.esquerda')


images[0] = document.src= '../static/img/batedeira-laranja-lado.png';
images[1] = document.src = '../static/img/batedeira-laranja-equipamentos.png';
images[2] = document.src ='../static/img/batedeira-laranja.png';



function changeImg(){ 
    document.slide.src = images[i];


    if (i < images.length -1){
        i++;
    }   else{
        i = 0;
    }
}

window = changeImg;












// let botaoMais = document.getElementById('#mais')
// let botaoMenos = document.getElementById('#menos')

// var count = 5;//recebendo o valor 5 que você disse
// $('#addCount').click(function(){
//   alert(count);
//   count++;
// });


// let contador = 0;

// $('#mais').click(function(){
//     alert(contador);
//     contador++;
// });

// function Aumentar(){
//     onclick ()
// }


// function aparecerImg(){
//     document.slide.src = '../static/img/piscina.png';
// }

// window.onload = aparecerImg;

// function voltarImg(){
//     document.slide.scr = '../static/img/batedeira-laranja.png';
// }

// onclick = voltarImg;

// function passarImg(){
//     document.slide.scr = '../static/img/batedeira-vermelha.png';
// }

