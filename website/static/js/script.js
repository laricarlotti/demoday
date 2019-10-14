let menuHamburguer = document.querySelector(".menu");
let main = document.querySelector("main");
let input = document.querySelector("input");
let botao = document.querySelector("button");
let h2 = document.querySelector("h2");

function mostrarMenu(){
  
    main.classList.toggle("visivel");
    menuHamburguer.classList.toggle("ativo");
}



//funcao que recebe o próprio evento de pressionar teclas e verifica se a tecla do evento é o Enter, se for enter ele chama a funcao de pegar nome


menuHamburguer.onclick = mostrarMenu;




