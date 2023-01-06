describe('Buscar fotos e dados', () => {
    const tempoEsperado = Math.random() * 2000;
    it.only('Buscar fotos', ()=> {
        cy.request({ // request faz uma requisição
            method:'GET',
            url: 'https://apialurapic.herokuapp.com/flavio/photos'
        }).then((res) => {
            expect(res.status).to.be.equal(200)
            expect(res.body).is.not.empty
            expect(res.body[0]).to.have.property('description')// Verifica se tem descrição no produto.
            expect(res.body[0].description).to.be.equal('Farol iluminado')// Verifica o nome do produto.
            expect(res.duration).to.be.lte(tempoEsperado) // Testa o tempo de limite de resposta.
        }
        )
    })

    it('Fazer login', ()=> {
        cy.request({
            method:'POST',
            url: 'https://apialurapic.herokuapp.com/user/login',
            body: Cypress.env()
        }).then((res) => {
            expect(res.status).to.be.equal(200)
            expect(res.body).is.not.empty
            expect(res.body).to.have.property('id')
            expect(res.body.id).to.be.equal(1)
            expect(res.body).to.have.property('email')
            expect(res.body.email).to.be.equal("flavio@alurapic.com.br")
        }
        )
    })

}) 