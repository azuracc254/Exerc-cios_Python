#Exercício_08
#Lista_02
#Lê os valores informados
print("Realizando as quatro operações básicas\n")
numero1 = float(input("Digite o primeiro número: "))
numero2 =float(input("Digite o segundo número: "))
#Realiza as tres operações básicas
adicao = numero1 + numero2 
subtracao = numero1 - numero2 
multiplicacao = numero1 * numero2 
#Verifica se o número 2 é maior que zero, se sim e quarta operação é realizada
if numero2 > 0:
    divisao = numero1 / numero2
else: 
#Senão é gerado um loop que pede ouyto valor sempre que o mesmo é zero
    while numero2 == 0:
        numero2 = float(input("Digite um numero maior que zero: "))
#Aos sair do loop a quarta operação tambem é realizada
divisao = numero1 / numero2
print("Adição: ",adicao,"\n")
print("Subtração: ",subtracao,"\n")
print("Multiplicação: ",multiplicacao,"\n")
print("Divisão: ",divisao,"\n")