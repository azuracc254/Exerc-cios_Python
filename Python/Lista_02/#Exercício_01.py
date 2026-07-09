#Exercício_01
#Lista_02
nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
if media >= 7:
    print("Você foi aprovado, média: ",media)
else:
    print("Você foi reprovado, média: ",media)