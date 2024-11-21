limite_peso = 50
multa_por_quilo = 4.00

P = float(input("Digite o peso dos peixes (em quilos): "))

E = 0
M = 0.00

if P > limite_peso:
    E = P - limite_peso
    M = E * multa_por_quilo

print(f"Excesso: {E} kg")
print(f"Multa: R$ {M:.2f}")
