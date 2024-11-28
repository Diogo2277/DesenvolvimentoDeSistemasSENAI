'''

4)Crie um programa que simule um caixa eletrônico. 
Peça ao usuário um valor a ser sacado e deduza de um saldo inicial. 
Caso o usuário tente sacar mais do que o saldo ou insira um valor inválido, trate o erro de forma apropriada. 
Garanta que o saldo atualizado seja sempre exibido no finally.
'''
def caixa_eletronico():
    saldo = 1000.00  # Saldo inicial

    try:
        saque = float(input("Digite o valor a ser sacado: "))

        if saque <= 0:
            raise ValueError("O valor de saque deve ser maior que zero.")
        
        if saque > saldo:
            raise ValueError("Saldo insuficiente para realizar o saque.")

        saldo -= saque
        print(f"Saque realizado com sucesso! Valor sacado: R$ {saque:.2f}")
    except ValueError as ve:
        print(f"Erro: {ve}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    finally:
        print(f"Saldo atualizado: R$ {saldo:.2f}")

if __name__ == "__main__":
    caixa_eletronico()
