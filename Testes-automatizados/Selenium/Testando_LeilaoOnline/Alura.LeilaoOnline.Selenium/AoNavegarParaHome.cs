using OpenQA.Selenium.Chrome;
using System;
using Xunit;
using OpenQA.Selenium;

namespace Alura.LeilaoOnline.Selenium
{
    public class AoNavegarParaHome: IDisposable
    {
        //Setup
        private ChromeDriver driver;
        
        public AoNavegarParaHome()
        {
            driver = new ChromeDriver();
        }

        //TearDown
        public void Dispose()
        {
            driver.Quit();
        } 

        [Fact]
        public void DadoQueOChromeFoiAbertoDeveMostarOTituloLeiloesOnline()
        {
            //arrange -> Dado que preciso abrir um navegador
            //IWebDriver driver = new ChromeDriver(); Esse cód será chamado no public AoNavegarParaHome()

            //act -> Preciso acessar o site
            driver.Navigate().GoToUrl("http://localhost:5000");

            //assert -> Espero ser direcionado para a página.
            Assert.Contains("Leilões", driver.Title);

            //Fechando o navegador sendo chamano do public void Dispose()

        }


        [Fact]
        public void DadoChromeAbertoDeveMostarProximosLeiloes()
        {
            //arrange -> Dadoque que preciso abrir um navegador
            //IWebDriver driver = new ChromeDriver(); Esse cód será chamado no public AoNavegarParaHome()

            //act -> Preciso acessar o site
            driver.Navigate().GoToUrl("http://localhost:5000/Home/Detalhes/8");

            //assert -> Espero ser direcionado para a pagina e encontrar Proximos Leilões
            Assert.Contains("Leilão de Carro 3", driver.PageSource); //PageSource busca no código fonte da página

            //Fechando o navegador sendo chamano do public void Dispose()

        }

    }
}
