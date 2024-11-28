'''
3)Solicite ao usuário que insira seu peso e altura. 
Calcule o IMC, mas trate possíveis erros, como entradas inválidas ou divisões por zero. 
Garanta que o programa sempre informe o status do processo no finall
'''
def calcular_imc(peso, altura):
    try:
        imc = peso / (altura ** 2)
        return imc
    except ZeroDivisionError:
        print("Erro: Altura não pode ser zero.")
        return None

def main():
    try:
        peso = float(input("Digite seu peso (em kg): "))
        altura = float(input("Digite sua altura (em metros): "))

        if altura == 0:
            raise ValueError("Altura não pode ser zero.")
        
        imc = calcular_imc(peso, altura)
        
        if imc:
            print(f"Seu IMC é: {imc:.2f}")
        else:
            print("Não foi possível calcular o IMC devido a um erro.")
    except ValueError as ve:
        print(f"Erro de valor: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        print("Processo finalizado.")

if __name__ == "__main__":
    main()
