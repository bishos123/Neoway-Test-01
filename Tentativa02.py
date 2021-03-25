#Nestra outra tentavia, tentei pelo pandas converter o Json em Json lines, e tambem nao consegui, pois ele consta erro de trailing data.

import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os
from selenium.webdriver import chrome
import json
import requests


# Grab content from URL (Pegar conteúdo HTML a partir da URL)
url = "https://buscacepinter.correios.com.br/app/faixa_cep_uf_localidade/carrega-faixa-cep-uf-localidade.php?letraLocalidade=&ufaux=&pagina=/app/faixa_cep_uf_localidade/index.php&mensagem_alerta=&uf=MG&localidade=&cepaux="

driver = webdriver.Chrome()

driver.get(url)

element = driver.find_element_by_xpath("/html/body/pre")
html_element = element.get_attribute('outerHTML')


html_element_file = open("html_element_file8.php.json", "w")
html_element_file.write(html_element)
html_element_file.close()

driver.quit()


df = pd.read_json('c:/Users/denis/Desktop/html_element_file8.php.json',)
df.to_json('C:/Users/denis/Desktop/NEWFILE.jl', orient="records", lines=True)
driver.quit()

