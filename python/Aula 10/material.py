def converteDolar(valor):
    valor *= 5.82
    return valor

print(converteDolar(5))

# def nome (paremetro)
#  processo
#  vs
#  lambd parametro : processo

# vantagem do lambda
# resume processos simples
#  ajuda legibilidade
#  evita chamar um def em caso de uma linha

# desvantagens 
#  não é eficaz em processos maiores
#  em falta de atenção, dificulta variaveis
converterEuro = lambda valor : valor * 6.66
converterIene = lambda valor, taxa : valor / 0.03 - taxa
print(converterEuro(20))
print(converterIene(1000,40))

# TERNARIO
condicao = False
if condicao:
    print('IF')
else:
    print('ELSE')

print('IF') if condicao else print('ELSE')

valor = 0
valor = 1 if condicao else valor
print(valor)