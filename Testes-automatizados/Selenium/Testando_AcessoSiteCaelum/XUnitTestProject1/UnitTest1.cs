using System;
using Xunit;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;

namespace XUnitTestProject1
{
    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            //arrange -> Dado que um navegador está aberto
            IWebDriver driver = new ChromeDriver();

            //act -> Quando navego para a url https://www.caelum.com.br
            driver.Navigate().GoToUrl("https://www.caelum.com.br");

            //assert -> Eu espero que eu seja direcionado para a página da Caelum
            Assert.Contains("Caelum", driver.Title);

        }
    }
}
