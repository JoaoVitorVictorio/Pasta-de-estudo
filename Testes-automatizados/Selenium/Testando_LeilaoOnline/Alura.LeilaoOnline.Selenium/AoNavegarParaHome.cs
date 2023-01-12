using OpenQA.Selenium.Chrome;
using System;
using Xunit;
using OpenQA.Selenium;

namespace Alura.LeilaoOnline.Selenium
{
    public class AoNavegarParaHome
    {
        [Fact]
        public void DadoQueOChromeFoiAbertoDeveMostarOTituloLeiloesOnline()
        {
            //arrange -> Dado que preciso abrir um navegador
            IWebDriver driver = new ChromeDriver();

            //act -> Preciso acessar o site
            driver.Navigate().GoToUrl("http://localhost:5000");

            //assert -> Espero ser direcionado para a página.
            Assert.Contains("Leilões", driver.Title);
                
            //Fechando o navegador
            driver.Quit();
        }
        [Fact]
        public void DadoChromeAbertoDeveMostarProximosLeiloes()
        {
            //arrange -> Dadoque que preciso abrir um navegador
            IWebDriver driver = new ChromeDriver();

            //act -> Preciso acessar o site
            driver.Navigate().GoToUrl("http://localhost:5000");

            //assert -> Espero ser direcionado para a pagina e encontrar Proximos Leilões
            Assert.Contains("Próximos Leilões", driver.PageSource); //PageSource busca no código fonte da página

            // Fechando o navegador
            driver.Quit();

        }
    }
}
