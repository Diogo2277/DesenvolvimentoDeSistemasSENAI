#  AULA 1 - INTRODUÇÃO E VARIAVEIS

#  COMENTÁRIO

"""
DOCTRING - ANOTAÇÕES
"""

#  PRINT - ESCREVA
print("BOM DIA !!!")
print("Diogo Souza de Oliveira")
#  CRLF - caracteres que represntam a quebra de linha do sistema
#  \r return
#  \n line feed

#  end (end - fim do print)
print('Uma informação',' importante',end="\n")
#  sep (sep - separador do print)
print('Uma informação',' importante',sep='-----')

# type
print(type(111111)) # int (inteiro) ex 1, 0
print(type(1.5)) # float (numero flutuante, real) ex 1.5, -1.4
print(type('oi')) # str (string, caracter) ex 'oi', "opa"
print(type(True)) # bool (bollean, logico) ex True, False

#  variavel
#  1 - caracteres especiais
#  2 - espaço vazios
#  camelCase = umExemplo
#  snakeCase = um_exemplo
#  3 - evite numeros solos, ou começo de variavel
# *4 - evite nomes poucos descritivos 

# variaveis maiusculo são constantes
# constantes não ter seu valor mudado
TESTE = 1 
teste = "TESTE" 
print(teste, teste, teste)