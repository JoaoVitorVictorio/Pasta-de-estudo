function getScore (score) {
let scoreA = score >= 90 && score <= 100
let scoreB = score >= 80 && score <= 89
let scoreC = score >= 70 && score <= 79
let scoreD = score >= 60 && score <= 69
let scoreE = score < 60 && score >= 0

let scoreFinal

if (scoreA) {
    scoreFinal = 'A'
} else if (scoreB) {
    scoreFinal = 'B'
}else if (scoreC) {
    scoreFinal = 'C'
}else if (scoreD) {
    scoreFinal = 'D'
}else if (scoreE) {
    scoreFinal = 'E'
}else {
    scoreFinal = 'Nota Inválida '
}
return scoreFinal
}
console.log(getScore(-01))
console.log(getScore(14))
console.log(getScore(46))
console.log(getScore(56))
console.log(getScore(68))
console.log(getScore(79))
console.log(getScore(85))
console.log(getScore(93))
console.log(getScore(99))
console.log(getScore(101))
