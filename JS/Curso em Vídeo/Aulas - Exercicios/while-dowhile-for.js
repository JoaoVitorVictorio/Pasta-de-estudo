//Utilizar o while quando não souber o limite das execuções
console.log('Andando com white...')
var c = 1
while (c <= 3){
    console.log(`${c}º passo`)
    c++
}

///Utilizar o do while quando não souber o limite das execuções, a diferença do for é que primeiro é executado o cód e depois acontece a repetição.
console.log('Andando com do while...')
var c = 1
do {
    console.log(`${c}º passo`)
    c++
} while (c <= 6)

//Utilizar o for quando souber o limite das execuções
console.log('Andando com for...')
for (var c = 1; c <= 9; c++){
    console.log(`${c}º passo`)
}