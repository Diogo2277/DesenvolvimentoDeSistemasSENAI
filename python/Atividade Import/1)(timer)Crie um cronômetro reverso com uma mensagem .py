'''
1)(timer)Crie um cronômetro reverso com uma mensagem final personalizada usando o módulo time.
'''
# import time
from time import sleep as timer 

segundos = int(input('Quantos segundos tem o time: '))

for i in range(segundos,0,-1):
    timer(1)
    print(f'{i} segundos')

print('TEMPO ESGOTADO')