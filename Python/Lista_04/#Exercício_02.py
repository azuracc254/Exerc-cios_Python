#Exercício_02
#Lista_04
#Recebe os valores da quantidade máxima, atual e mínima e declara as variaveis
quantidade_atual = int(input("Digite a quantidade atual em estoque de um produto: "))
quantidade_maxima = int(input("Digite a quantidade máxima deste produto no estoque: "))
quantidade_minima = int(input("Digite a quantidade mínima deste produto no estoque: "))
#Calcula a méida da quantidade máxima e mínima
media = (quantidade_minima + quantidade_maxima) / 2
#Verfica se media é ou não maior que a atual
#Se for maior que a quantidade atual então deve efetuar a compra
if media <= quantidade_atual:
    print("Não efetuar compra")
    #senão, não a faça
else:
    print("Efetuar compra")