import time
import os
import shutil
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Diretório de destino para onde o arquivo será movido
diretorio_destino = r'C:\Users\guilh\Downloads\teste2'  

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
navegador.get('https://www.rpachallenge.com/')
time.sleep(2)
navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/a').click()
time.sleep(3)

# Abrindo o diretório de downloads
diretorio_downloads = r'C:\Users\guilh\Downloads'  

# Obtendo a lista de arquivos no diretório de downloads
arquivos = os.listdir(diretorio_downloads)

# Filtrando apenas arquivos com extensão .xlsx
arquivos_xlsx = [arquivo for arquivo in arquivos if arquivo.endswith('.xlsx')]

# Verificando se existem arquivos .xlsx baixados
if arquivos_xlsx:
    # Encontrando o arquivo Excel mais recente
    arquivo_mais_recente = max(arquivos_xlsx, key=lambda x: os.path.getctime(os.path.join(diretorio_downloads, x)))
    caminho_arquivo = os.path.join(diretorio_downloads, arquivo_mais_recente)
    
    # Movendo o arquivo Excel para o diretório de destino
    shutil.move(caminho_arquivo, diretorio_destino)
    
    # Carregando o arquivo Excel com pandas
    dados_excel = pd.read_excel(os.path.join(diretorio_destino, arquivo_mais_recente))
    dados_usuarios = dados_excel.to_dict('records')
else:
    print("Nenhum arquivo .xlsx foi encontrado no diretório de downloads.")

time.sleep(2)

navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[1]/div[6]/button').click()

for usuario in dados_usuarios:
    first_name = usuario.get("First Name", "")
    last_name = usuario.get("Last Name ", "") 
    address = usuario.get("Address", "")
    phone_number = usuario.get("Phone Number", "")
    email = usuario.get("Email", "")
    company_name = usuario.get("Company Name", "")
    role_in_company = usuario.get("Role in Company", "")
    

    navegador.find_element(By.XPATH, '//input[@ng-reflect-name="labelFirstName"]').send_keys(first_name)
    navegador.find_element(By.XPATH, '//input[@ng-reflect-name="labelLastName"]').send_keys(last_name)
    navegador.find_element(By.XPATH, '//input[@ng-reflect-name="labelCompanyName"]').send_keys(company_name)
    
    navegador.find_element(By.XPATH, '//input[@ng-reflect-name="labelRole"]').send_keys(role_in_company)
    navegador.find_element(By.XPATH, '//input[@ng-reflect-name="labelAddress"]').send_keys(address)
    navegador.find_element(By.XPATH, '//input[@ng-reflect-name="labelEmail"]').send_keys(email)
    navegador.find_element(By.XPATH, '//input[@ng-reflect-name="labelPhone"]').send_keys(phone_number)
    
    
    time.sleep(1)
    

    navegador.find_element(By.XPATH, '/html/body/app-root/div[2]/app-rpa1/div/div[2]/form/input').click()
