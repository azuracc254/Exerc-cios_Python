#Exercício_02
#Lista_04
quantidade_atual = int(input("Digite a quantidade atual em estoque de um produto: "))
quantidade_maxima = int(input("Digite a quantidade máxima deste produto no estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima deste produto no estoque: "))
media = (quantidade_minima + quantidade_maxima) / 2
if media >= quantidade_atual:
    print("Não efetuar compra")
else:
    print("Efetuar compra")