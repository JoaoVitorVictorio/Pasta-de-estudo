describe('Buscador de curso', () => {   // Descrição do teste

    beforeEach(() => {
            cy.visit('https://www.youtube.com/') // O site que quero visitar no teste.
        })

      it('Buscar por curso ', () => {
        cy.get('#search-form > #container').type('Curso em Video - Python'); // Escreve no campo selecionado
        cy.get('#search-icon-legacy > yt-icon.style-scope').click(); // Clica no campo selecionado
        cy.get('span#video-title.style-scope.ytd-playlist-renderer') // Acessa o campo selecionado
            .should('contain', 'Curso em vídeo - Python'); // Busca pelo conteudo descrito no contain
      })
    })