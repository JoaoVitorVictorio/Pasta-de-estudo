describe('Buscador de curso', () => {   // Descrição do teste

    beforeEach(() => {
            cy.visit('https://www.youtube.com/') //  Indicar a URL que será carregada antes de cada novo caso de teste.
        })

      it('Buscar por curso ', () => { // Criar um novo caso de teste.
        cy.get('#search-form > #container').type('Curso em Video - Python'); // Escreve no campo selecionado.
        cy.get('#search-icon-legacy > yt-icon.style-scope').click(); // Clica no campo selecionado.
        cy.get('span#video-title.style-scope.ytd-playlist-renderer') //  Identificar o elemento html da página.
            .should('contain', 'Curso em vídeo - Python'); // Busca pelo elemento identificado pelo DevTools.
      })
    })