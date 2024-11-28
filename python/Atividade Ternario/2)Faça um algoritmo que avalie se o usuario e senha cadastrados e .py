'''
2)Faça um algoritmo que avalie se o usuario e senha cadastrados e 
se não tiver, printe uma falha
senao printe que deu tudo certo
(considerar que usuario e senha sejam ''ADM')
'''
def ex2():

    usuario_cadastrado = 'ADM'
    senha_cadastrada = 'ADM'

    usuario = input('Qual é o usuário: ')
    senha = input('Qual é a senha: ')
    
    v_usuario = usuario == usuario_cadastrado
    v_senha = senha == senha_cadastrada

    msgSucesso = 'CONTA LOGADA'
    msgErro = 'USUARIO OU SENHA INCORRETOS'

    print('USUARIO CORRETO! ') if v_usuario else print ('USUARIO INCORRETO')

    print('SENHA CORRETA!') if v_senha else print ('SENHA INCORRETA')

ex2()
