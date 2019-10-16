let idade = Number(prompt("Qual a sua idade?"));

while(idade < 0 || isNaN(idade)){
    alert("Idade inválida. Por favor digite novamente")
    idade = Number(prompt("Qual a sua idade?"));
}

let teste = 'oi'