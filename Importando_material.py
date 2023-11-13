import requests
from bs4 import BeautifulSoup

link = 'https://ge.globo.com/futebol/brasileirao-serie-a/'

requisicao = requests.get(link)
#print(requisicao) verificar se está respondendo o link (200)
print(requisicao.text)

site = BeautifulSoup(requisicao.text, "html.parser")

#TAG html para fazer a busca
print(site.find_all(".classificacao__equipes--nome"))
