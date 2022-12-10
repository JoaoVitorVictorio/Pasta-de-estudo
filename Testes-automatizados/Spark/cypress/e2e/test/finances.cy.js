/// <reference types="cypress"/>

import { format } from '../../support/utils'


describe.only('Dev Finances', () => {

    beforeEach(() => { //beforeEach = irá repetir um cód para todos os testes
        cy.visit('https://dev-finance.netlify.app/#')

    });

    it('Cadastrar entradas', () => {
        //Inserindo uma entrada
        cy.get('#transaction .button').click()
        cy.get('#description').type('Mesada')
        cy.get('#amount').type(150)
        cy.get('[type=date]').type('2022-12-07')
        cy.get('button').contains('Salvar').click()
        cy.get('#data-table tbody tr').should('have.length', 1)
    });

    it('Cadastrar saída', () => {
        //Inserindo uma saída
        cy.get('#transaction .button').click()
        cy.get('#description').type('Tênis')
        cy.get('#amount').type(-100)
        cy.get('[type=date]').type('2022-12-08')
        cy.get('button').contains('Salvar').click()
        //Verificando quantas tabelas tinha
        cy.get('#data-table tbody tr').should('have.length', 1)
    });

    it('Adicionando uma entrada e uma saída', () => {
        const entrada = 'Mesada'
        const saida = 'Tênis'

        //Inserindo uma entrada
        cy.get('#transaction .button').click()
        cy.get('#description').type(entrada)
        cy.get('#amount').type(150)
        cy.get('[type=date]').type('2022-12-07')
        cy.get('button').contains('Salvar').click()

        //Inserindo uma saida
        cy.get('#transaction .button').click()
        cy.get('#description').type(saida)
        cy.get('#amount').type(-100)
        cy.get('[type=date]').type('2022-12-08')
        cy.get('button').contains('Salvar').click()

        // Removendo uma entrada (1ª estratégia)
        cy.get('td.description')
        .contains(entrada)
        .parent()
        .find('img[onclick*=remove]')
        .click()

        // Removendo uma entrada (2ª estratégia)
        //cy.get('[data-index="0"] > :nth-child(4) > img').click()

        // Removendo uma entrada (3ª estratégia)
        cy.get('td.description')
        .contains(saida)
        .siblings()
        .children('img[onclick*=remove]')
        .click()
        cy.get('#data-table tbody tr').should('have.length', 0)
    });
        it('Validar saldo com diversas transações', () => {
            const entrada = 'Mesada'
            const saida = 'Tênis'
    
            //Inserindo uma entrada
            cy.get('#transaction .button').click()
            cy.get('#description').type(entrada)
            cy.get('#amount').type(100)
            cy.get('[type=date]').type('2022-12-07')
            cy.get('button').contains('Salvar').click()
    
            //Inserindo uma saída
            cy.get('#transaction .button').click()
            cy.get('#description').type(saida)
            cy.get('#amount').type(-35)
            cy.get('[type=date]').type('2022-12-08')
            cy.get('button').contains('Salvar').click()

            //Verificando saldo com diversas transações

let incomes = 0
let expenses = 0

            cy.get('#data-table tbody tr')
            .each(($el, index, $list) => {
                cy.log(index)
                cy.get($el).find('td.income, td.expense').invoke('text').then(text => {
                    if(text.includes('-')){
                        expenses = expenses + format(text)
                    } else{
                        incomes = incomes + format(text)

                    }
                    cy.log(`entradas`, incomes)
                    cy.log(`saidas`, expenses)
                })
            })

        cy.get('#TotalDisplay').invoke('text').then(text => {
            let formattedTotalDisplay = format(text)
            let expectedTotalDisplay = incomes + expenses
            expect(formattedTotalDisplay).to.eq(expectedTotalDisplay)
        })

    });
});

//npx cypress open --config viewportWidth=411, viewportHeight=823 (Abre em diferente resuluções)

