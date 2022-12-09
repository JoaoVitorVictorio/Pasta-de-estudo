/// <reference types="cypress"/>

describe('Dev Finances', () => {

    beforeEach(() => { //beforeEach = irá repetir um cód para todos os testes
        cy.visit('https://dev-finance.netlify.app/#')
        cy.get('#data-table tbody tr').should('have.length', 0)
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
});

//npx cypress open --config viewportWidth=411, viewportHeight=823 (Abre em diferente resuluções)

