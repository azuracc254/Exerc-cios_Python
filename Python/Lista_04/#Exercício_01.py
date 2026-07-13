#Exercício_01
#Lista_04
#Pega o saldo, débito e crédito para determinar o saldo final
#Declara as variáveis
print("======Banco Bradesco======")
numero = int(input("Digite o número do seu cartão: "))
saldo = float(input("Informe o seu saldo: "))
debito = float(input("Informe o seu débito: "))
credito = float(input("Digite o seu crédito: "))
#Fórmula que determina o saldo 
saldo_atual = saldo + credito - debito
print("O seu saldo atual é: ",saldo_atual)