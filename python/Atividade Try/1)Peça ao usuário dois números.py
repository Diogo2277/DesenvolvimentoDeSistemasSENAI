"""
 1)Peça ao usuário dois números e uma operação matemática (+, -, *, /). 
 Execute a operação e trate erros como divisão por zero e operação inválida.

"""

num1 = int(input('Digite o 1º número: '))
operador = input('Digite o operador')
num2 = int(input('Digite o 2º número: '))

match operador:
    case '+':
        resultado = num1 + num2
    case '-':
        resultado = num1 - num2
    case '*':
        resultado = num1 * num2
    case '/':
        resultado = num1 / num2
    case _:
        print('Digite um operador válido')

print(f'RESULTADO : {resultado}')