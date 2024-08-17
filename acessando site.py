
import pyautogui
from time import sleep
from urllib import request
from ex97 import escreva
def automatico():
            pyautogui.PAUSE=0.3
            pyautogui.press('win')
            pyautogui.write('edge')
            pyautogui.press('enter')
            pyautogui.write(user)
            pyautogui.press('enter')
while True:
    user=input('escreva um endereço de internet:').strip()

    if not user == 'lista':
        try:
            site=request.urlopen(user)
        except:
            print('não encontramos o endereço!')
        else:
            print('site estar acessivel!')
            sleep(1)
            automatico()
      
            
            ad_site=open('save_site.txt','at+')
            try:
                ad_site.write(f'\n{user}')    
            except:
                print('erro nos arquivo de save')
            finally:   
                ad_site.close()
    else:
        ad_site=open('save_site.txt','rt')
        escreva('lista de sites acessados'.upper())
        print(ad_site.read())