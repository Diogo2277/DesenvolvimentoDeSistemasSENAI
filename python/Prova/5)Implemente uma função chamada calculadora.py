'''
5)Implemente uma função chamada calculadora que:Receba dois números e uma operação (adição, subtração, multiplicação ou divisão).
Retorne o resultado da operação.Trate divisões por zero e exiba uma mensagem apropriada.Salve o histórico dela em um json
'''


import json


def calculadora(num1, num2, operacao):
    if operacao == "adição":
        resultado = num1 + num2
    elif operacao == "subtração":
        resultado = num1 - num2
    elif operacao == "multiplicação":
        resultado = num1 * num2
    elif operacao == "divisão":
        if num2 == 0:
            return "Erro: Divisão por zero não é permitida."
        resultado = num1 / num2
    else:
        return "Operação inválida."
    
    return resultado
def salvar_historico(historico):
    with open("historico_calculadora.json", "w") as arquivo:
        json.dump(historico, arquivo)

def carregar_historico():
    try:
        with open("historico_calculadora.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

if __name__ == "__main__":
    historico = carregar_historico()
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (adição, subtração, multiplicação, divisão): ")

    resultado = calculadora(num1, num2, operacao)

    print(f"Resultado: {resultado}")

    if isinstance(resultado, (int, float)):
        historico.append({
            "num1": num1,
            "num2": num2,
            "operacao": operacao,
            "resultado": resultado
        })
        salvar_historico(historico)
    
    print("\nHistórico de Operações:")
    for item in historico:
        print(item)
