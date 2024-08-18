
from selenium import webdriver

from urllib import request
from ex97 import escreva

while True:
    user=input('escreva um endereço de internet:').strip()

    if not user == 'lista':
        try:
            site=request.urlopen(user)
        except:
            print('não encontramos o endereço!')
        else:
            print('site estar acessivel!')
            navegador=webdriver.Firefox()
            site=navegador.get(user)
            
      
            
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