'''
2)Escreva um programa para um sistema de controle de estoque de uma loja. 
O programa deve:Usar um para armazenar os itens no estoque, 
onde as chaves são os nomes dos produtos e os valores são as quantidades disponíveis.Permitir que o usuário escolha uma das opções:
Adicionar um novo produto ao estoque.
Atualizar a quantidade de um produto existente.
Verificar se um produto está disponível (quantidade maior que 0).
Continuar exibindo o menu até que o usuário escolha sair.
'''
def adicionar_produto(estoque):
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    if nome in estoque:
        estoque[nome] += quantidade
    else:
        estoque[nome] = quantidade
    print(f"Produto '{nome}' adicionado com sucesso!")

def atualizar_produto(estoque):
    nome = input("Digite o nome do produto: ")
    if nome in estoque:
        quantidade = int(input("Digite a nova quantidade do produto: "))
        estoque[nome] = quantidade
        print(f"Quantidade do produto '{nome}' atualizada para {quantidade}.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

def verificar_produto(estoque):
    nome = input("Digite o nome do produto: ")
    if nome in estoque and estoque[nome] > 0:
        print(f"O produto '{nome}' está disponível com {estoque[nome]} unidades.")
    else:
        print(f"O produto '{nome}' não está disponível ou está fora de estoque.")

def menu():
    print("\nSistema de Controle de Estoque")
    print("1. Adicionar produto")
    print("2. Atualizar quantidade de produto")
    print("3. Verificar disponibilidade de produto")
    print("4. Sair")
    return input("Escolha uma opção: ")

def main():
    estoque = {}
    while True:
        opcao = menu()
        if opcao == '1':
            adicionar_produto(estoque)
        elif opcao == '2':
            atualizar_produto(estoque)
        elif opcao == '3':
            verificar_produto(estoque)
        elif opcao == '4':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
