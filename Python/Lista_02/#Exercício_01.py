#Exercício_01
#Lista_02
#Lê tres notas
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
#Calcula a média das tres
media = (nota1 + nota2 + nota3) / 3
#Verifica se esta na média de media for > ou igual a 7
if media >= 7:
    print("Você foi aprovado, média: ",media)
else:
    print("Você foi reprovado, média: ",media)