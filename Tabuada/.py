from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Função para esperar até que um elemento esteja presente na página
def esperar_elemento(driver, tempo_limite, localizador):
    return WebDriverWait(driver, tempo_limite).until(
        EC.presence_of_element_located(localizador)
    )

# Função para esperar até que um elemento seja clicável na página
def esperar_elemento_clicavel(driver, tempo_limite, localizador):
    return WebDriverWait(driver, tempo_limite).until(
        EC.element_to_be_clickable(localizador)
    )

# Configurar o driver do Firefox
driver = webdriver.Firefox()

# Abrir a URL desejada
driver.get("https://page-test-selenium.s3.sa-east-1.amazonaws.com/index.html")

try:
    # Exemplo de uso das funções para interagir com um elemento
    elemento = esperar_elemento_clicavel(driver, 10, (By.ID, "some_id"))
    elemento.click()

finally:
    # Fechar o navegador ao finalizar
    driver.quit()
