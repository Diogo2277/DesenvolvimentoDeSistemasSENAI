'''
1)Implemente um sistema de gerenciamento de estoque que inclua classes Produto, 
Estoque e métodos para adicionar, remover e verificar produtos.  
'''

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, produto):
        if produto.nome in self.produtos:
            self.produtos[produto.nome].quantidade += produto.quantidade
        else:
            self.produtos[produto.nome] = produto

    def remover_produto(self, nome, quantidade):
        if nome in self.produtos:
            if self.produtos[nome].quantidade >= quantidade:
                self.produtos[nome].quantidade -= quantidade
                if self.produtos[nome].quantidade == 0:
                    del self.produtos[nome]
            else:
                print(f"Quantidade insuficiente de {nome} para remover.")
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    def verificar_produto(self, nome):
        if nome in self.produtos:
            print(self.produtos[nome])
        else:
            print(f"Produto {nome} não encontrado no estoque.")

    def exibir_estoque(self):
        if self.produtos:
            print("Estoque:")
            for produto in self.produtos.values():
                print(produto)
        else:
            print("O estoque está vazio.")
