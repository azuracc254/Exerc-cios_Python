#Exercício_09
#Lista_03
#Declara as variaveis e recebe o valor do começo e final do jogo em horas e calcula o tempo de duração
inicio = int(input("Digite a hora de inicio do jogo: "))
fim = int(input("Digite a hora de fim do jogo: "))
#Se fim for menor ou igual a inicio, tempo recebe 24 (total de horas do dia) - fim - inicio
if fim <= inicio:
    tempo = int(24 - fim - inicio)
#Senão, se fim > que inicio tempo recebe fim menos incio
elif fim > inicio:
    tempo = fim - inicio
print(f"o tempo de jogo foi {tempo} horas")