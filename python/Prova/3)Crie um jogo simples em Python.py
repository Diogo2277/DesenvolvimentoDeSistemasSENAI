'''
Crie um jogo simples em Python:Um número secreto entre 1 e 100 é gerado aleatoriamente.
O jogador tem 5 tentativas para adivinhar o número.Após cada tentativa, o programa deve informar:
"Muito alto!" se o palpite for maior que o número.
"Muito baixo!" se o palpite for menor que o número.
"Parabéns, você acertou!" se o palpite for igual ao número.
Caso o jogador não acerte após 5 tentativas, exiba "Game Over! O número era X".
Utilize a biblioteca random para gerar o número secreto.
'''

import random

numero_secreto = random.randint(1, 100)

tentativas = 5

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número secreto entre 1 e 100.")
print(f"Você tem {tentativas} tentativas.")

for tentativa in range(1, tentativas + 1):
    palpite = int(input(f"Tentativa {tentativa}: Digite seu palpite: "))

    if palpite == numero_secreto:
        print("Parabéns, você acertou!")
        break
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Muito baixo!")

    if tentativa == tentativas:
        print(f"Game Over! O número era {numero_secreto}")

print("Fim do jogo!")
