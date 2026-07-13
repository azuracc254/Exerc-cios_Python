#Exercício_09
#Lista_02
#Receb um aidade e verifica qual o valor 
idade = int(input("Digite a sua idade: "))
#Determina faixa etária
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