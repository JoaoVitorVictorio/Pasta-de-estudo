let family = {
    incomes: [1000, 1300],
    expenses: [100, 200, 300, 500, 200],
}

function sum (array){
    let total = 0;

    for (let value of array) {
        total += value
    }

    return total
}

function calculateBalance () {
    const calculateIncomes = sum(family.incomes);
    const calculateExpenses = sum(family.expenses);

    const total = calculateIncomes - calculateExpenses

    const ok = total >= 0

    let balanceText = 'negativo'
    if (ok) {
        balanceText = 'positivo'
    }

    console.log(`Seu saldo é ${balanceText}: R$ ${total.toFixed(2)}`)
}

calculateBalance()