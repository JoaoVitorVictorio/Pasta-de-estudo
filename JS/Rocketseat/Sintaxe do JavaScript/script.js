/* //BOOLEAN
var verdadeiroOuFalso = true;
console.log(verdadeiroOuFalso);
console.log(typeof(verdadeiroOuFalso)); */

/* //NUMBER
var numero = 1
console.log(number);
console.log(typeof(number)); */

/* //STRING
var string = 'João';
console.log(string);
console.log(typeof(string)); */

/* //DECLARANDO VAR E REATRIBUINDO VALORES.
var variavel = 'João';
variavel = 'Vitor';
console.log(variavel); */

/* //DECLARANDO LET E REATRIBUINDO VALORES.
let variavel = 'João';
variavel = 'Vitor';
console.log(variavel); */

/* //DECLARANDO CONST E TENTANDO REATRIBUINDO VALORES.
const constante = 'muda?';
constante = 'mudou';
//TypeError não capturado: Atribuição à variável constante. CONSTANTE NÃO ALTERA VALORES.
console.log(constante); */

/* //ESCOPO GLOBAL
var escopoGlobal = 'global';
console.log(escopoGlobal);
console.log(typeof(escopoGlobal)); */
 
/* //ESCOPO LOCAL
function escopoLocal() {
    let escopoLocalInterno = 'Local';
    console.log(escopoLocalInterno);
}
    escopoLocal(); */
    
/* //COMPARAÇÃO
var numberAtribuição = 0;
console.log(numberAtribuição);
//R: 0

var numberComparação = '0' == 0;
console.log(numberComparação);
//R: TRUE

var numberComparaçãoIdentica = '0' === 0;
console.log(numberComparaçãoIdentica);
//R: FALSE */

/* //OPERADORES ARITIMÉTICOS
var adição = 1 + 1;
console.log(adição);
//R: 2

var subtração = 5 - 1;
console.log(subtração);
//R: 4

var multiplicação = 3 * 2;
console.log(multiplicação);
//R: 6

var divisãoReal = 10 / 2;
console.log(divisãoReal);
//R: 5

var divisãoInteira = 9 % 2;
console.log(divisãoInteira);
//R: 1

var potenciação = 10 ** 2;
console.log(potenciação);
//R: 100 */

/* //OPERADORES RACIONAIS
var maiorQue = 1 > 2;
console.log(maiorQue);
//R: false

var menorQue = 2 < 3;
console.log(menorQue);
//R: true

var maiorOuIgual = 4 >= 3;
console.log(maiorOuIgual);
//R: true

var menorOuIgual = 5 <= 3;
console.log(menorOuIgual);
//R: false */

/* //OPERADORES LÓGICOS
var e = true && false;
 console.log(e);
 //R: false

  var ou = false || true;
 console.log(ou);
 //R: true

 var não = !false;
 console.log(não);
 //R: true */

/* //ARRAY
 let array = ['string', 10, true, ['array1'], ['array2'], ['array3']];
 array.push('novo_item')//add item no final do array;
 array.pop()//remove item no final do array;
 array.shift()//remove item no início do array;
 array.unshift('novo_item')//add item no início do array;
 console.log(array); */

/* //OBJETOS
 let person = {
     name:'Joao',
     age: 25,
     height: 65,
 }
 console.log(person)
 */

/* // ESTRUTURAS CONDICIONAIS
var jogador1 = 1;
var jogador2 = 0;
var placar;

// utilizando if ternário
jogador1 ≠ -1 && jogador2 ≠ -1 ? console.log('Os jogadores são válidos') : console.log('Jogadores inválidos')

// utilizando if
if (jogador1 > 0){
    console.log('jogador1 marcou ponto');
}
// utilizando else if
else if (jogador2 > 0){
    console.log('jogador2 marcou ponto');
}
// utilizando else
else{
    console.log('ninguém marcou ponto');
}
// switch
switch (placar) {
    case placar = jogador1 > jogador2:
        console.log('jogador1 ganhou');
            break;
    case placar = jogador2 > jogador1:
        console.log('jogador2 ganhou');
            break;
    default:
        console.log('ningém ganhou');
}

let array = ['valor1', 'valor2', 'valor3', 'valor4', 'valor5',];
let object = {propriedade1: 'valor1', propriedade2: 'valor2', propriedade3: 'valor3', propriedade4: 'valor4', propriedade5: 'valor5',};
 
// for
for (let indice = 0; indice < array.length; indice++){
    console.log(indice);
}

// for in
for (let i in array) {
    console.log(i);
}

// for in com object
for (i in object) {
    console.log(i);
}

// for of com array
for (i of array) {
    console.log(i);
}

// for of com object
for (i of object.propriedade1) {
    console.log(i);
}

// while
var a = 0;
while (a < 10) {
    a++;
    console.log(a)
}

// do/while
do {
    a++;
    console.log(a);
} while (a < 10) */

/* // FUNÇÕES E SUAS PARTICULARIDADES
function funcao(){
    console.log('Olá');
}

funcao();

// funções com parâmetros

function mensagem(primeiro, segundo) {
    console.log(primeiro, segundo);
}

mensagem('Olá', 'mundo'); */