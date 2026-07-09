#Exercício_09
#Lista_03
inicio = int(input("Digite a hora de inicio do jogo: "))
fim = int(input("Digite a hora de fim do jogo: "))
if fim <= inicio:
    tempo = int(24 - fim - inicio)
elif fim > inicio:
    tempo = fim - inicio
print(f"o tempo de jogo foi {tempo} horas")