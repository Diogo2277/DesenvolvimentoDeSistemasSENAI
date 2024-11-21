
idade = int(input("Digite a sua idade: "))

if 0 <= idade < 15:
    print("Criança")
elif 15 <= idade < 30:
    print("Jovem")
elif 30 <= idade < 60:
    print("Adulto")
elif idade >= 60:
    print("Idoso")

