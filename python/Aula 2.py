#  Equanto condição for true, farei denovo
#  break - quebra a repetiçao

condicao = True

# while condicao:
    #  pergunta = input('DESEJA REPETIR DENOVO')
    
    # if pergunta == 'nao':
        # break

contador = 1

while contador <= 10:
    print(contador)
    # contador = contador + 1 
    contador += 1

    if contador == 5:
        print( 'Nao vou mostrar o 5 :(')
        continue
    print(contador)
      # contador = contador + 1 
