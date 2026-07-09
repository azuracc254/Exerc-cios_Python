#Exercício_09
#Lista_02
idade = int(input("Digite a sua idade: "))
if idade <= 2:
    print("bebê")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 64:
    print("Adulto")
elif idade > 64:
    print("Idoso")