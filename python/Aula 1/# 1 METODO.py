#  1 METODO
# numero[1] = input
numeros = []

for i in range(4):
    numero = int(input(f'Digite {i+1}º número'))
    numeros.append(numero)
    
print(numeros)
print(max(numeros))
print(min(numeros))