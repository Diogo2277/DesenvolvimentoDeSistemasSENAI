'''
4)(random)Use o módulo random para sortear um nome de uma lista de participantes.
'''
import random

lista_alunos = ['Paloma','Victor','João','Geraldo']

sorteado = random.choices(lista_alunos)

print(sorteado)