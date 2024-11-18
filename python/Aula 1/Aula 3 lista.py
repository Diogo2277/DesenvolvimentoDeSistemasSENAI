'''
LISTAS
'''

#  cliente1 = 'Victor'
#  cliente2 = ' Alan'
#  cliente3 = ' Bruna'

#  CRUD - CREATE , READ , UPADTE , DELETE 

cliente = ['Vitor', 'Alan', 'Bruna']
teste = ['texto',123,True,[]]
#  clienteAlt = list()

# print(type(cliente))
# print(teste)

# metodos de uma lista 
lista = ['Copo','Banana','Kitkat','Bebida']
print(lista)

lista.append('VideoGame') # adicionar no final
print(lista)

lista.pop() # remover o final
print(lista)

lista.insert(2, 'tv') # inserir(indice,dado)
print(lista)

del lista [1] # deletar em um indice
print(lista)

# indice 0 1 2 3 4 / -5 -4 -3 -2 -1
print(lista[1]) # puxar por um indice

lista.remove('Bebida')
print(lista)

lista.clear() #deletar tudo na lista
print(lista)


