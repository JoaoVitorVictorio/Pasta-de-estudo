Cypress.Commands.add('login', (nome, senha) => {
    cy.get('input[formcontrolname="userName"]').type(nome);
    cy.get('input[formcontrolname="password"]').type(senha, {log: false});
    cy.get('button[type="submit"]').click();
})

Cypress.Commands.add('registro', (email, nomeCompleto, nomeUsuario, senha) => {
    cy.get('input[formcontrolname="email"]').type(email)
    cy.get('input[formcontrolname="fullName"]').type(nomeCompleto)
    cy.get('input[formcontrolname="userName"]').type(nomeUsuario)
    cy.get('input[formcontrolname="password"]').type(senha, {log: false})
})