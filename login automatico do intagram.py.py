from selenium import webdriver
from time import sleep
from pyautogui import press

#pedido do telefone nome ou email do user
email=input('Coloque o nome,telefone ou email do usuario:').strip()
#senha do user
senha=input('coloque sua senha instagram:').strip()

#selecionando navegador
nav=webdriver.Firefox()

#acessando site
nav.get('https://www.instagram.com/')
#maximizando a tela
nav.maximize_window()

sleep(3)

#colocando o nome no login
nav.find_element('xpath','/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[1]/div/label/input').send_keys(email)

sleep(3)

#colocando senha no login
nav.find_element('xpath','/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/section/main/article/div[2]/div[1]/div[2]/div/form/div/div[2]/div/label/input').send_keys(senha)

#apertando o botão enter
press('enter')