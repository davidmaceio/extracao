#Importando apenas o módulo WEBDRIVER do selenium
from selenium import webdriver

#Informando ao navegador que utilizaremos o navegador Google Chrome(Drive igual ao navegador)

navegador = webdriver.Chrome()
#Informando a URL para acessar automático.

navegador.get("https://cortecloud.com.br/")

#Através do XPATH da página HTML, inspecionando.
navegador.find_element_by_xpath('')


