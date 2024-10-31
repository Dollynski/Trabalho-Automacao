# Imports necessários para o funcionamento do script

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import os
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env

load_dotenv()

cpf = os.getenv('BLACKBOARD_CPF')
senha = os.getenv('BLACKBOARD_SENHA')

# Verifica se as variáveis de ambiente foram carregadas corretamente

if not cpf or not senha:
    raise ValueError("Erro: O CPF e Senha do arquivo .env não foram carregados corretamente.")

# Inicializa o navegador e acessa a página de login do Blackboard

nav = webdriver.Firefox()
nav.maximize_window()
nav.get('https://senac.blackboard.com')

# Preenche os campos de CPF e Senha e clica no botão de login

textCpf = WebDriverWait(nav, 10).until(
    EC.presence_of_element_located((By.NAME, 'user_id_tmp'))
)

textSenha = WebDriverWait(nav, 10).until(
    EC.presence_of_element_located((By.NAME, 'password'))
)

textCpf.send_keys(cpf)
textSenha.send_keys(senha)

nav.find_element(By.ID, 'entry-login').click()