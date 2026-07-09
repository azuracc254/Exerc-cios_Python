#Exercício_08
#Lista_05
nota_maior = 1
for i in range(17):
    nome = input("Digite o nome da candidata: ")
    nota = float(input("Digite a nota da candidata: "))
    if nota > nota_maior:
        nota_maior + nota
        vencedor = nome
print(f"Vencedora: {vencedor}")
print(f"Nota: {nota}")