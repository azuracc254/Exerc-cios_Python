#Exercício_03
#Python 02
#Recebe o valor solicitado
velocidade = int(input("Digite a velocidade do carro: "))
#Verfica se a velocidade é maior que 50 se sim é aplicado a multa
if velocidade > 50:
    multa = 50 * (velocidade - 50)
    print(f"Você foi multado em: {multa}R$")
#Senão é exibida a mensagem sem cobrança
else:
    print("Você não foi multado")