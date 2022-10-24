import requests 
from  re import search

url = input('\033[34mdigite a url: \033[32m')
### validação do https ##
if search('http',str(url)):
    pass
else:
    url = f'https://{url}'
requisição = requests.get(url)
#print(requisição.headers['X-Served'])

lista_servers = ['X-Served','Server']

for names in lista_servers:
    try:
        print(f"\n\n\033[31mRodando : {requisição.headers[f'{names}']} \n\n")
    except:
       pass
print('#'*50,"\n")
print(' '*15,'++ informações ++\n')
print('#'*50,'\n')


for information in requisição.headers:
    print(information, requisição.headers[information])
 
métodos = requests.options(url)
if métodos.status_code == 403:
    print('Options error < servidor bloqueor')
try:
    print(f'\n\nMétodos aceitos: {métodos.headers["allow"]}')       
except:
    print('#'*50)    