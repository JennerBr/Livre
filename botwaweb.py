# importar bibliotecas
from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
# abrir wahtsappweb
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(20)
# selecionar destinatario
dests = ['11 97521-1314','Quintal Vendas']
msg = 'Olá, ?cliente?! Está tudo bem? Segue lista de disponibilidades. Se quiser algo, é só pedir. Obrigado, Jenner.'

def find_dest(dest):
    search_field = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    search_field.click()
    search_field.send_keys(dest)
    search_field.send_keys(Keys.ENTER)

def send_msg(msg):
    search_field = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    search_field[1].click()
    search_field[1].send_keys(msg)
    time.sleep(0.2)
    search_field[1].send_keys(Keys.ENTER)

for dest in dests:
    find_dest(dest)
    send_msg(msg)
