# cara que cria o navegador
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

service = Service(ChromeDriverManager().install())
nav = webdriver.Chrome(service=service)
nav.get("https://web.whatsapp.com/")

# para nao ter problemas se tiver emoticons na mensagem
mensagem = "ola, essa mensagem foi escrita pelo python"
lista_contatos = ["Notas", "Isa", "Jozil"]

# enviar a mensagem para notas para poder depois encaminhar

# clicar na lupa
nav.find_element(
    'xpath', '//*[@id="side"]/div[1]/div/div[2]/button/div[2]/span').click()
# escrever "NOTAS"
nav.find_element(
    'xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys("Notas")
# das um enter
nav.find_element(
    'xpath', '//*[@id="side"]/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
# dar um tempo para parecer mais humano
time.sleep(3)

# escrever a mensagem para nós mesmos
input_box = nav.find_element(
    'xpath', '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
input_box.clear()  # Limpar qualquer conteúdo existente no campo
input_box.send_keys(mensagem)  # Digitar a mensagem diretamente
input_box.send_keys(Keys.ENTER)  # Enviar a mensagem
time.sleep(3)

contatos = len(lista_contatos)

if contatos % 5 == 0:
    blocos = contatos / 5
else:
    blocos = int(contatos / 5) + 1

for i in range(blocos):
    # codigo encamihar
    i_inicial = i*5
    i_final = (i + 1) * 5
    lista_enviar = lista_contatos[i_inicial:i_final]

    # clicar em 3 pontos vertical
    nav.find_element(
        'xpath', '//*[@id="main"]/header/div[3]/div/div[3]/div/div/span').click()
    time.sleep(2)
    # clicar em selecionar mensagem
    nav.find_element(
        'xpath', '//*[@id="app"]/div/span[5]/div/ul/div/div/li[2]/div').click()
    time.sleep(2)
    # clicar no quadrado da ultima mensagem recebida
    nav.find_element(
        'xpath', '//*[@id="main"]/div[3]/div/div[2]/div[3]/div[20]/div/div/span/div/div').click()
    time.sleep(2)
    # clicar na seta de enviar
    nav.find_element(
        'xpath', '//*[@id="main"]/span[2]/div/button[4]/span').click()
    time.sleep(2)

    for nome in lista_enviar:
        # selecionar os 5 contatos para enviar
        # escrever o nome do contato
        nav.find_element(
            'xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(nome)
        time.sleep(3)

        nav.find_element(
            'xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.ENTER)
        time.sleep(3)

        nav.find_element(
            'xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/div[1]/div/div[2]/div[2]/div/div[1]/p').send_keys(Keys.DELETE)
        time.sleep(3)

    # clicar no botao enviar
    nav.find_element(
        'xpath', '//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div/span/div/div/div/span').click()
    time.sleep(3)
