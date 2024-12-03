'''
1)Crie um ambiente virtual chamado calculadora_bolos e, dentro dele, 
um programa que calcule a quantidade de ingredientes necessários para assar 5 bolos, 
a partir de uma receita padrão. A receita padrão é:

Farinha: 200g por bolo

Açúcar: 100g por bolo

Ovos: 2 por bolo
'''

bolos = 5
farinha = 200 * bolos
acucar = 100 * bolos
ovos = 2 * bolos

print(f'Para {bolos} bolos precisará de : \n')
print(f'farinha - {farinha}g \n')
print(f'açucar - { acucar}g \n')
print(f'ovos - {ovos} \n')