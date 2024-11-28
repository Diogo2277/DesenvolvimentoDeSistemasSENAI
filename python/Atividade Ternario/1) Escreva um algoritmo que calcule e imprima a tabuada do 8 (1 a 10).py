# https://www.w3schools.com/python/default.asp


'''
1) Escreva um algoritmo que calcule e imprima a tabuada do 8 (1 a 10).
'''
def ex1():
    # metodo com lambda
    # for i
    # lambda 8 : 8 * i

    # metodo com list compreentions
    tabuada = [i * 8 for i in range(1,11)]
    print(tabuada)

