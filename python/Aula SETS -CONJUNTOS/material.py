'''''
SETS - CONJUNTOS
- 1º NÃO TE IDINCE ( NÃO GARANTE ORDEM)
- 2º NÃO ACEITA CONTEUDO REPETIDO
'''''

#  CRIANDO SE
a = set ('VICTOR')
teste = ['OI','OI','OI']
print(a)
print (set(teste))

b = {'Victor',1,2,3,4,5,6}
print(b)

c = set()
print(c ,type(c))

# mtodos uteis 
conjunto = set()
conjunto.add(10)
conjunto.add(8)

conjunto.update((3,5,6,'BOM DIA'))

conjunto.discard('BOM DIA')  

print('*'*20)
print(conjunto)

# UNIÃO (UNION) - UNE DOIS
# INTERSECÇÃO (INSTERSECTION) - COMUM NOS DOIS
# DIFERENÇA - INTEM PRESENTES APENAS EM UM
conjuntoA = {1,2,3,4,5}
conjuntoB = {5,6,7,8,9}
conjuntoC = set()

# | union
conjuntoC = conjuntoA | conjuntoB
#  & intersection
conjuntoC = conjuntoA & conjuntoB
# - diferance = diferença em relaçao ao 
# conjunto da esquerda
conjuntoC = conjuntoB - conjuntoA
# - ^ diference = diferença em relçao a abos os conjuntos
conjuntoC = conjuntoA ^ conjuntoB
for elemento in conjuntoC:
    print(elemento)
    
print(conjuntoC)