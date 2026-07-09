#Exercício_08
#Lista_02
print("Realizando as quatro operações básicas\n")
numero1 = float(input("Digite o primeiro número: "))
numero2 =float(input("Digite o segundo número: "))
adicao = numero1 + numero2 
subtracao = numero1 - numero2 
multiplicacao = numero1 * numero2 
if numero2 > 0:
    divisao = numero1 / numero2
else: 
    while numero2 == 0:
        numero2 = float(input("Digite um numero maior que zero: "))
divisao = numero1 / numero2
print("Adição: ",adicao,"\n")
print("Subtração: ",subtracao,"\n")
print("Multiplicação: ",multiplicacao,"\n")
print("Divisão: ",divisao,"\n")