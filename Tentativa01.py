#Nesta primeira tentativa, eu tentei utilizar o Selenium (um framework que simula um navegador) para extrair a table do site e então converter ela em arquivo.
#nesta tentativa, nao consegui finalizar, pois nao conversão de Json para JSon lines não foi possivel por erro.

import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
from selenium.webdriver import chrome
import json
import requests



url = "https://buscacepinter.correios.com.br/app/faixa_cep_uf_localidade/carrega-faixa-cep-uf-localidade.php?letraLocalidade=&ufaux=&pagina=/app/faixa_cep_uf_localidade/index.php&mensagem_alerta=&uf=MG&localidade=&cepaux="

driver = webdriver.Chrome()

driver.get(url)

element = driver.find_element_by_xpath("/html/body/pre")
html_element = element.get_attribute('outerHTML')


html_element_file = open("html_element_file8.php.json", "w")
html_element_file.write(html_element)
html_element_file.close()
with open('html_element_file8.php.json', "r") as f:
    lines = f.readlines()


#aqui tentei retirar a primeira linha do documento que constava isto abaixo, e estava interferindo na conversão.
with open ('html_element_file8.php.json', 'w') as f:
    for line in lines:
        if  line.strip('\n') != '<pre style="word-wrap: break-word; white-space: pre-wrap;">':
            f.write(line)
driver.quit()



