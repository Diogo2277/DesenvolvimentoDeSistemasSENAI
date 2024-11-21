# DICIONARIO
# CHAVE E VALOR

usuario = {
    'nome' : 'Victor',
    'email' : 'emailtop@gmail.com',
    'senha' : '!123456',
    'cpf' : 9999999,
    'vipe' :True,
    'endereco' : [
        {
            'rua' : '13',
            'cidade' : 'Ceilandia',
            'estado' : 'DF'
        }
    ]
}

print(usuario['nome'])
print(usuario, type(usuario))

# arquitetura de dic facilita o gerenciamento de dados 
# e a busca por eles (Obs: Até mesmo o crud)

# pesquisa = input('Digite o que quer achar:')
# print(usuario[pesquisa])

# METODOS PARA DICIONARIO
# LEN - QUANTAS CHAVES EXISTEM NO DICIOANRIO
# KEYS - RETORNA AS CHAVES
# VALUES - RETORNA OS VALORES 
# ITEMS - RETORNA CHAVES E VALORES
# SETDEFAULT - ADICIONA VALOR SE A CHAVE NÃO EXISTE
# GET - BUSCA CHAVE
# POP - APAGA UMA CHAVE ESPECIFICA (del)
# POPITEM - APAGA A ULTIMA CHAVE
# UPDATE - ATUALIZA UM DICIONARIO 
print(len(usuario))
print(list(usuario.keys()))
print(list(usuario.values()))
print(list(usuario.items()))

usuario.setdefault('saldo', 0)
print(usuario)

print(usuario.get('nome'))

usuario.pop('nome')
print(usuario)

usuario.popitem()
print(usuario)

usuario.update({
    'nome' : 'Victor',
    'emai' : 'vitor.rohod@docente.senai.br'
})
print(usuario)