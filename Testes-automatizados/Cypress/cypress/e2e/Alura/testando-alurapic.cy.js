describe('Login e registro de usuario alurapic', () => {

    beforeEach(() => {
        cy.visit('https://alura-fotos.herokuapp.com') // Entrou no site da Alurapic.
        cy.intercept('POST', 'https://apialurapic.herokuapp.com/user/login', {
            statusCode: 400
        }).as('stubPost')
    })

    it('Verificando mensagem de validação', () => {
        cy.contains('a', 'Register now').click(); // Clicou no botão de novo registro.
        cy.contains('button', 'Register').click(); // Clicou no botão de Registrar.
        cy.contains('ap-vmessage', 'Email is required!').should('be.visible'); // Vai verifica se a mensagem de (e-mail é obrigatório) está visivel.
        cy.contains('button', 'Register').click(); // Clicou novamente no botão de Registrar para aparecer os demais erros de requerimento.
        cy.contains('ap-vmessage', 'Full name is required!').should('be.visible'); //Vai verifica se a mensagem de (nome completo) é obrigatório está visivel.
        cy.contains('ap-vmessage', 'User name is required!').should('be.visible'); //Vai verifica se a mensagem de (nome de usuário) é obrigatório está visivel.
        cy.contains('ap-vmessage', 'Password is required!').should('be.visible'); //Vai verifica se a mensagem de (senha requerida) está visivel.
    })

    it('Verificando mensagem de email inválido', () => {
        cy.contains('a', 'Register now').click(); // Clicou no botão de novo registro.
        cy.contains('button', 'Register').click(); // Clicou no botão de Registrar.
        cy.get('input[formcontrolname="email"]',).type('joaovitorvictorio') // Vai tentar validar o campo de e-mail, com um e-mail incorreto. Portanto como digitei um e-mail inválido terá que verificar se possui uma mensagem de e-mail inválido.
        cy.contains('ap-vmessage', 'Invalid e-mail').should('be.visible'); // Vai verifica se a mensagem de (e-mail é obrigatório) está visivel.
    })

    it('Verificando mensagem de nome completo obrigátorio', () => {
        cy.contains('a', 'Register now').click(); // Clicou no botão de novo registro.
        cy.contains('button', 'Register').click(); // Clicou no botão de Registrar.
        cy.get('input[formcontrolname="fullName"]',).type('João Vitor Victorio') // Vai digitar o nome no campo de nome obrigátorio.
    })

    it('Verificando mensagem de nome usuario com letra ser minúscula', () => {
        cy.contains('a', 'Register now').click(); // Clicou no botão de novo registro.
        cy.contains('button', 'Register').click(); // Clicou no botão de Registrar.
        cy.get('input[formcontrolname="userName"]',).type('Vitor') // Vai digitar o nome no campo de usuario obrigátorio.
        cy.contains('button', 'Register').click(); // Clicou no botão de Registrar.
        cy.contains('ap-vmessage', 'Must be lower case').should('be.visible'); // Verifica se possui a mensagem de (Deve ser minúscula) está visivel.

    })

    it('Verificando mensagem de senha com menos de 8 caracteres', () => {
        cy.contains('a', 'Register now').click(); // Clicou no botão de novo registro.
        cy.contains('button', 'Register').click(); // Clicou no botão de Registrar.
        cy.get('input[formcontrolname="password"]',).type('12345') // Vai digitar a senha com 5 caracteres, sendo que o minimo são 8 caracteres.
        cy.contains('button', 'Register').click(); // Clicou no botão de Registrar para verificar se irá aparecer a mensagem de (O comprimento mínimo é 8).
        cy.contains('ap-vmessage', 'Mininum length is 8').should('be.visible'); // Verifica se a mensagem de (e-mail é obrigatório) está visivel.
    })

    it('Verificando login com usuário válido', () => {
        cy.visit('https://alura-fotos.herokuapp.com')
        cy.login(Cypress.env('userName'), Cypress.env('password'));
        cy.wait('@stubPost')
        cy.contains('a', '(Logout)').should('be.visible');
    })

    it('Verificando login com usuário inválido', () => {
        cy.visit('https://alura-fotos.herokuapp.com')
        cy.login('joao', '321');
        cy.on('window:alert', (str) => {
            expect(str).to.equal('Invalid user name or password')
        })
    
    })

    //it.only('Cadastrando novo usuário', () => { //only roda somente este cód
    //    cy.visit('https://alura-fotos.herokuapp.com')
    //    cy.contains('a', 'Register now').click();
    //    cy.registro('teste@gmail.com', 'teste automatizado', 'automatizando', '123654789');
    //    cy.contains('button', 'Register').click();
    //})

    const usuarios = require('../../fixtures/usuarios.json');
    usuarios.forEach(usuario => {
        it(`Registrando novo usuário ${usuario.userName}`, () => { //only roda somente este cód
            cy.visit('https://alura-fotos.herokuapp.com')
            cy.contains('a', 'Register now').click();
            cy.get('input[formcontrolname="email"]').type(usuario.email);
            cy.get('input[formcontrolname="fullName"]').type(usuario.fullName);
            cy.get('input[formcontrolname="userName"]').type(usuario.userName);
            cy.get('input[formcontrolname="password"]').type(usuario.password);
            cy.contains('button', 'Register').click();
        })
    })
})
