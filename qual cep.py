import requests

print(20*'=')
print(' QUAL SEU CEP')
print(20*'=')

user=input('qual seu cep:').strip()

try:
    api=requests.get(f'https://viacep.com.br/ws/{user}/json/')
except:
    print('não conseguimos encontra o cep!')
else:
    print(f'o cep é da cidade de {api.json()['localidade']}')