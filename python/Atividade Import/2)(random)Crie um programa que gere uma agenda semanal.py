'''
2)(random)Crie um programa que gere uma agenda semanal aleatória com atividades usando o módulo random.
'''

import random


atividades = [
    "Exercício",
    "Leitura",
    "Trabalho",
    "Estudo",
    "Lazer",
    "Cozinhar",
    "Limpeza",
    "Compras",
    "Hobbies",
    "Descanso"
]

dias_semana = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]


agenda_semanal = {}

for dia in dias_semana:
    atividade = random.choice(atividades)
    agenda_semanal[dia] = atividade


print("Agenda Semanal Aleatória:")
for dia, atividade in agenda_semanal.items():
    print(f"{dia}: {atividade}")
