import requests
import os
import zipfile
from bs4 import BeautifulSoup
from time import sleep
from io import BytesIO
from os.path import join
from datetime import datetime


# Função para realizar uma solicitação HTTP GET para a URL fornecida
def get_response(url, retries=10):
    r = requests.get(url)

    # Verifica se a resposta foi bem-sucedida (código de status < 400)
    if r.status_code == 200:
        return r
    else:
        # Tentativas de solicitação adicionais em caso de falha
        for i in range(retries):
            sleep(0.4)
            r = requests.get(url)

            # Verifica novamente se a resposta foi bem-sucedida
            if r.status_code == 200:
                return r

        print('Erro na requisição')


# Função para extrair objetos HTML com base em um seletor CSS usando BeautifulSoup
def get_objects(soup, selector):
    return soup.select(selector)


# Função para baixar arquivos da web e armazená-los localmente
def download_files_locally(files, filenames, local_directory):
    #Baixa arquivos da web e armazena-os localmente.
    os.makedirs(local_directory, exist_ok=True)  # Cria o diretório se não existir
    for file_url, filename in zip(files, filenames):
        try:
            # Realiza o download do arquivo da web
            response = requests.get(file_url, stream=True)
            if response.status_code == 200:
                # Cria um objeto BytesIO para armazenar o conteúdo do arquivo em memória
                file_obj = BytesIO(response.content)
                # Extrai o conteúdo do arquivo ZIP em memória
                with zipfile.ZipFile(file_obj, 'r') as zip_ref:
                    for file_info in zip_ref.infolist():
                        file_name = file_info.filename
                        file_content = zip_ref.read(file_name)
                        # Caminho local completo para o arquivo
                        local_file_path = os.path.join(local_directory, file_name)
                        # Salva o conteúdo do arquivo no diretório local
                        with open(local_file_path, 'wb') as local_file:
                            local_file.write(file_content)
                print(f"Arquivo '{filename}' baixado com sucesso.")
            else:
                print(f"Falha ao baixar o arquivo '{filename}'. Status code: {response.status_code}")
        except Exception as e:
            print(f"Erro ao baixar o arquivo '{filename}': {str(e)}")


# URL da página da web
url = 'https://dados.rfb.gov.br/CNPJ/'

# Obtém a resposta HTTP da URL especificada
r = get_response(url)

# Cria um objeto BeautifulSoup para analisar o conteúdo HTML da resposta
soup = BeautifulSoup(r.text, 'html.parser')

# Extrai os elementos HTML que contêm links para arquivos .zip
objetos = get_objects(soup, 'table tr a')

# Filtra apenas os links para arquivos .zip
objetos = [objeto for objeto in objetos if objeto.text.endswith('.zip')]

# Listas vazias para armazenar URLs e nomes de arquivos
files = []
filenames = []

# URL base para construir os URLs completos dos arquivos
BASEURL = 'https://dados.rfb.gov.br/CNPJ'

# Itera sobre os objetos encontrados e extrai URLs e nomes de arquivos
for objeto in objetos:
    file_url = objeto.get('href')
    # Verifica se a URL é relativa (começa sem 'http')
    if not file_url.startswith('http'):
        file_url = f"{BASEURL}/{file_url}"
    files.append(file_url)
    filenames.append(objeto.text.strip('.zip'))

# Diretório local
local_directory = "C:\\Users\\User\\Desktop\\workspace\\ETL_RF\\dados"

# Chama a função para baixar e armazenar os arquivos localmente
download_files_locally(files, filenames, local_directory)