#Exercício_08
#Lista_03
#Recebe a quantidade de maçãs e declara as variaveis
quantidade = int(input("Digite a quantidade de maçãs: "))
#Se maior ou igual que 12 cada uma custara 1
if quantidade >= 12:
    total = 1 * quantidade
    print("O preço é: ",total)
#Senão, se menor que 12 cada uma custara 1.30
elif quantidade < 12:
    total = float(1.30 * quantidade)
    print("O preço é: ",total)
