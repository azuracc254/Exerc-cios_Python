#Exercício_08
#Lista_03
quantidade = int(input("Digite a quantidade de maçãs: "))
if quantidade >= 12:
    total = 1 * quantidade
    print("O preço é: ",total)
elif quantidade < 12:
    total = float(1.30 * quantidade)
    print("O preço é: ",total)
