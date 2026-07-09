#Exercício_10
#Lista_05
print("Calculo apenas com  multiplicações ")
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = int(1)
for i in range(expoente):
    resultado = resultado * base
print("O resultado é: ",resultado)