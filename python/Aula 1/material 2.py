alunosPt1 = ['Carlos', 'Alessandra', 'Geraldo']
alunosPt2 = ['Guilhermer', 'Paloma', ' Natan']

alunosPt3 = alunosPt1 + alunosPt2

alunosPt1.extend(alunosPt2)
# print(alunosPt1)

#  for + array
print(len(alunoPt1))

alunosPt1.append('Bruna')

for nome in alunosPt1:
    print(f'-{nome} \n ####')