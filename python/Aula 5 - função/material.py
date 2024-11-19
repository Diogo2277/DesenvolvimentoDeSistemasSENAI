valorTotal = 0

# parametro - recebe o argumento
def somarValor():
    global valorTotal

    # valorproduto = float(input('PRECO DO PRODUTO))
    valorTotal += valorProduto

# argumento -valor entre parenteses
somarValor(30)
somarValor(5)
somarValor(47)

print(f'valor total é de R$: {valorTotal}')