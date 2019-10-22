//TROCAR IMAGENS NA PAGINA DE PRODUTOS 

let i = 0;
let images = [];


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
