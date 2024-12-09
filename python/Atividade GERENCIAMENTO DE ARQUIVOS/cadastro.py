def cadastrarUsuario():
    nome = input('Digite o nome: ')
    login = input('Digite o login(email):')
    cpf = (input('Digite seu cpf(8888888): '))
    
    while True:  
        senha = input('Digite sua senha: ')
        c_senha = input('Digite a sua senha novamente: ')

        if senha == c_senha:
            break
        else:
            print('Senha não bate na confirmação tente novamente! ')

    with open('dados.json','w',encoding='uft8') as
    leitura:
        json.dump(
            dados,
            leitura,
            indent=2
    )