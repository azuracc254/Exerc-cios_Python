#Exercício_07
#Lista_02
print("Calculo de IMC")
altura = float(input("Infrome a sua altura: "))
peso = float(input("Infrome o seu peso: "))
imc = peso / altura**2
if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso ideal")
elif imc < 30:
    print("Sobre-peso")
elif imc < 35:
    print("Obeso")
elif imc >= 35:
    print("Obeso morbido")