
quantidade_notas = int(input("Digite a quantidade de notas que deseja calcular: "))

soma_notas = 0

for i in range(1, quantidade_notas + 1):
    nota = float(input(f"Digite a nota {i}: "))
    soma_notas += nota


media = soma_notas / quantidade_notas


print(f"\nMédia final: {media:.2f}")
if media >= 7:
    print("Resultado: Aprovado")
else:
    print("Resultado: Reprovado")