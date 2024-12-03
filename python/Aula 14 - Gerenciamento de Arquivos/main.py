arquivo = 'main.txt'
# MODOS DO TEXTIOWRAPPER
# w (escrita)
# r (read)
# x (criação)
# t (modo texto)
# w+,r+ (escrita e leitura)
# b (binario)

# METODO 1
# leitura = open (arquivo,'w')
# leitura.close()

# metodo 2
with open (arquivo,'w+') as leitura:
    # write - escreve uma linha
    # writelines - escreve multiplas linhas
    #  seek - move cursor
    leitura.write('QUE TOP \n')
    leitura.write('LINA 2 \n')
    leitura.seek(0,0)
    leitura.writelines(
        ('LINHA3\n','LINHA4\n','LINHA5\n')
    )

with open (arquivo,'r') as leitura:
    print(leitura.read())
    print(leitura.readline().strip())


print(type(leitura))
print(arquivo)

leitura = open(arquivo,'w')
    
leitura.close()
