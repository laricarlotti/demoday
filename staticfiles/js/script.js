let menuHamburguer = document.querySelector(".menu");
let main = document.querySelector("main");
let input = document.querySelector("input");
let botao = document.querySelector("button");
let h2 = document.querySelector("h2");


function mostrarMenu(){
  
    main.classList.toggle("visivel");
    menuHamburguer.classList.toggle("ativo");
}

menuHamburguer.onclick = mostrarMenu;

//funcao que recebe o próprio evento de pressionar teclas e verifica se a tecla do evento é o Enter, se for enter ele chama a funcao de pegar nome


// FAZER TRIÂNGULO DO ASIDE DESCER //


let triangle = document.querySelector('.triangle');

    triangle.addEventListener('click', function(){
    triangle.classList.toggle('triangle-down')
});


let entrar = document.querySelector('.botao1');

    entrar.addEventListener('click', function(){
        window.location.href = 'login'
});

let cadastrar = document.querySelector('.botao2');

    cadastrar.addEventListener('click', function(){
        window.location.href = 'cadastro'

});




