#nesta outra tentativa, eu tentei extrair a tabela e usar o Beautifulsoup parar arrumar o codigo HTML e transforma-lo em uma tabela.
#mas infelizmente não consegui, pois ele consta como se nao tivesse nas linhas nao estivessem nas colunas.



import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
from selenium.webdriver import chrome
import json
import requests
from bs4 import BeautifulSoup



url = "view-source:https://buscacepinter.correios.com.br/app/faixa_cep_uf_localidade/carrega-faixa-cep-uf-localidade.php?letraLocalidade=&ufaux=&pagina=/app/faixa_cep_uf_localidade/index.php&mensagem_alerta=&uf=MG&localidade=&cepaux="

driver = webdriver.Chrome()

driver.get(url)

element = driver.find_element_by_xpath("/html/body/table")
html_element = element.get_attribute('outerHTML')
print(html_element)

soup = BeautifulSoup(html_element, 'html.parser')
table = soup.find(name='table')

TB_full = pd.read_html(str(table))[0]
TB = TB_full[['uf', 'localidade', 'cepInicial', 'cepFinal']]
TB.columns = ['Estado', 'Cidade', 'cepIn', 'cepOut']

print(df)
driver.quit()