import time
import pygame

pygame.init()

user=int(input('quando devemos lhe alerta (coloque os numeros sem separar EX: ":"):'))


while True:
    relogio=time.strftime('%H:%M:%S',time.localtime())#buscar o horario local

    #tirando os espaços
    relogio= relogio.replace(':','')
    
    #transformando em numero
    relogio=int(relogio[:4])
    
    if relogio == user:
        pygame.mixer.music.load('despertadorsamsung.mp3')
        pygame.mixer.music.play()
        pygame.event.wait()