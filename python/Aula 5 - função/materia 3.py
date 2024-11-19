def somarMuitos(*numeros):
    valorTotal = 0

    for numero in numeros:
            valorTotal += numero
    print(numeros, valorTotal)
    

somarMuitos(1,2)
somarMuitos(250,901,412,321)
somarMuitos(410, 1203)
somarMuitos(190283912, 1315789)

print(sum([1,5,7,8,9]))