'''
4)Crie uma classe Aluno que tenha os atributos nome, 
notas (uma lista) e métodos para calcular a média e verificar se o aluno foi aprovado (média >= 7). 
Todo aluno criado deverá ser adicionado a um Json
'''
import json
import os

class Aluno:
    def __init__(self,nome):
        self.nome = nome
        self._notas = []

    def adicionarNotas(self,nota):
       self._notas.append(nota)

    def calcularMedia(self):
        if self._notas:
            return sum(self._notas) / len(self._notas)
        else:
            return 0
    def verificarAprovacao(self):
        media = self.calcularMedia()

        if media >= 7:
            print(f'Aluno(a) {self.nome} está aprovado')
        else:
            print(f'Aluno(a) {self.nome} está reprovado')

    def exportarAluno(self):
        dados_aluno = {
            'nome' : self.nome,
            'notas' : self._notas,
            'media' : self.calcularMedia(),
            'aprovacao' : self.verificarAprovacao()
        }

        if os.path.exists('dados.json'):
            with open('dados.json','r') as f:
                try:
                     dados = json.load(f)
                except json.JSONDecodeError:
                     dados = []  
        else:
            dados = []

        dados.append(dados_aluno)
        
        with open('dados.json','w',encoding='utf8') as arquivos:
            json.dump(dados,f,indent=2)


aluno1 = Aluno('Victor')
aluno1.adicionarNotas(8)
aluno1.adicionarNotas(7)
print(aluno1._notas)
aluno1.verificarAprovacao()

aluno2 = Aluno('Bruna')
aluno2.verificarAprovacao()

aluno3 = Aluno('Pedro')
aluno3.adicionarNotas(5)
aluno3.adicionarNotas(6)
aluno3.verificarAprovacao()

print(vars(aluno1))
print(aluno2.__dict__)
print(aluno3.__dict__)