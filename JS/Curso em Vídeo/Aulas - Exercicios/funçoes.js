// Resultado de par ou ímpar utilizando return dentro da function
function parimpar(n){
    if(n%2 == 0){
        return 'Par!'
    } else{
        return 'Ímpar!'
    }
}

let res = parimpar(6)
console.log(res)

// Somando valores
function soma(n1=0, n2=0){
    return n1 + n2
}
console.log(soma(7 + 50))

// Variavel dentro de uma função
let v = function(x){
    return x * 2
}
console.log(v(5))

// Calculando o fatorial de um número: 
//5! = 5 x 4 x 3 x 2 x 1
function fatorial(n){
    let fat = 1
    for(let c = n; c > 1; c--){
        fat = fat * c
    }
    return fat
}
console.log(fatorial(5))