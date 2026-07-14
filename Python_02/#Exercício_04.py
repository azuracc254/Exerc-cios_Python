#Exercício_04
#Python 02
print("Calculo de cobrança de passagem: ")
#Recebe o valor solicitado 
distancia = int(input("Digite a distancia da viagem: "))
#Verfica se o valor é menor que 200 se sim é cobrado 0.50 por km 
if distancia <= 200:
    valor = float(0.50 * distancia)
#Senão é cobrado 0.45 por km
else:
    valor = float(0.45 * distancia)
print(f"O valor da passagem é: {valor}R$")