var num = [4, 7, 3, 5, 9, 8,]
num[3] = 6 // Adiciona o valor na posição declarada.
console.log(`O vetor é: ${num}`)
console.log(`O vetor tem ${num.length} posições`) // length exibi o comprimento do vetor.
console.log(`O primeiro valor do vetor é: ${num[1]}`)
console.log(`Adicionando o valor 0 na ultima posição: ${num.push(0)}`)// push adiciona o valor na ultima posição. 
console.log(`Agora o vetor é: ${num}`)
console.log(`Organizando os elementos em ordem crescente: ${num.sort()}`)// sort pega todos os elementos e coloca em ordem crescente.
let pos = num.indexOf(8)
if (pos == -1){
    console.log('O valor não foi encontrado')
} else{
    console.log(`O valor 8 está na posição ${pos}`)
}

console.log('SEPARANDO')

let valores = [1, 5, 9, 3, 5, 7]

for(let pos=0; pos < valores.length; pos++){
    console.log(`A posição ${pos} tem o valor ${valores[pos]}.`)
}

console.log('SEPARANDO')

for(let pos in valores){
    console.log(`A posição ${pos} tem o valor ${valores[pos]}.`)
}

console.log('SEPARANDO')

