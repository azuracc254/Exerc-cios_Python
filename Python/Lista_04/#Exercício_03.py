#Exercício_03
#Lista_04
#Recebe a distancia e quantidade de combustivel e declara as variáveis
distancia = float(input("Digite a distancia percorrida em km: "))
combustivel = float(input("Digite a quantidade de combistivel gasto: "))
#Fórmula que calcula a média de consumo por km
media = distancia / combustivel
print(f"A média de consumo é: {media:.2f} km/L")
