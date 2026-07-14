#Exercício_04
#Python 01
print("Conversão de km\h para n\s")
print("Digite apenas números")
#Lê o valor recebido
kilomestros = float(input("Digite o valor em km\h: "))
#Divide por 3,6 pois a razão de km\h para m\s é 3,6
mestros = kilomestros / 3.6
print(f"A conversão de {kilomestros}km\h em m/s é {mestros:.2f}m\s")
