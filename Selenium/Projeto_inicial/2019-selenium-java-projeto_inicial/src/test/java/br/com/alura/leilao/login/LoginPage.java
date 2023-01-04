package br.com.alura.leilao.login;

import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;

public class LoginPage {
	
	private static final String URL_LOGIN = "http://localhost:8080/login";
	private WebDriver browser;
	
	public boolean isPaginaDeLogin() {
	    return browser.getCurrentUrl().equals(URL_LOGIN);
	}
	
	
	public LoginPage() {
		System.setProperty("webdriver.chrome.driver", "drivers/chromedriver.exe");
        this.browser = new ChromeDriver();
        this.browser.navigate().to(URL_LOGIN);
	}


	public void fechar() {
		this.browser.quit();
	}


	public void preencheFormularioDeLogin(String username, String password) {
        browser.findElement(By.id("username")).sendKeys(username);
        browser.findElement(By.id("password")).sendKeys(password);
	}


	public void efetuaLogin() {
		 browser.findElement(By.id("login-form")).submit();
		
	}


	public Object getNomeUsuarioLogado() {
	    try {
	        return browser.findElement(By.id("usuario-logado")).getText();
	    } catch (Exception e) {
	        return null;
	    }
	}


	public void navegaParaPaginaDeLances() {
		this.browser.navigate().to("http://localhost:8080/leiloes/2");
		
	}


	public boolean contemTexto(String texto) {
		return browser.getPageSource().contains(texto);
	}


	public boolean isPaginaDeLoginComDadosInvalidos() {
	    return browser.getCurrentUrl().equals(URL_LOGIN + "?error");
	}

}
		

	
