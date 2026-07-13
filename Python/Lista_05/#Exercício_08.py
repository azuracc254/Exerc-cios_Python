#Exercício_08
#Lista_05
# a variavel nota maior é declarada no inicio pois não há necessidade de ficar dentro do loop 
nota_maior = 1
for i in range(17):
    nome = input("Digite o nome da candidata: ")
    nota = float(input("Digite a nota da candidata: "))
    #A nota é sempre atualizada pela maior para que possa ser exibidada no final
    if nota > nota_maior:
        nota_maior = nota
        vencedor = nome
print(f"Vencedora: {vencedor}")
print(f"Nota: {nota}")