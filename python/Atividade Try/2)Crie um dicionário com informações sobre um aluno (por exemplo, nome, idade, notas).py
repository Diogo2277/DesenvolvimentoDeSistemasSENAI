'''
2)Crie um dicionário com informações sobre um aluno (por exemplo, nome, idade, notas). 
Em seguida, solicite ao usuário uma chave para acessar no dicionário. 
Caso a chave não exista, trate o erro e informe quais chaves estão disponíveis.
'''

aluno = {
    "nome": "Carlos",
    "idade": 20,
    "notas": [8.5, 7.2, 9.0]
}

chave = input("Digite a chave que deseja acessar (nome, idade, notas): ")

try:
    valor = aluno[chave]
    print(f"O valor da chave '{chave}' é: {valor}")
except KeyError:
    print("Chave inválida! As chaves disponíveis são:", list(aluno.keys()))
