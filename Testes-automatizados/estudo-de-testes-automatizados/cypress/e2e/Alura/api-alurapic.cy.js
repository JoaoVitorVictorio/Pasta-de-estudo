describe('Buscar fotos e dados', () => {
    it('Buscar fotos', ()=> {
        cy.request({ // request faz uma requisição
            method:'GET',
            url: 'https://apialurapic.herokuapp.com/flavio/photos'
        }).then((res) => {
            expect(res.status).to.be.equal(200)
            expect(res.body).is.not.empty
            expect(res.body[0]).to.have.property('description')
            expect(res.body[0].description).to.be.equal('Farol iluminado')
        }
        )
    })
})