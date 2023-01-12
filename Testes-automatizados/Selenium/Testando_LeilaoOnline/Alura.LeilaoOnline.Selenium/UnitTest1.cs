using OpenQA.Selenium.Chrome;
using System;
using Xunit;
using OpenQA.Selenium;

namespace Alura.LeilaoOnline.Selenium
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            //arrange -> Dado que preciso abrir um navegador
            IWebDriver driver = new ChromeDriver();

            //act -> Preciso acessar o site
            driver.Navigate().GoToUrl("http://localhost:5000");

            //assert -> Espero ser direcionado para a página.
            Assert.Contains("Leilões", driver.Title);
        }
    }
}
