#Exercício_13
#Lista_02
#Recebe o valor da compra e valor a ser pago 
valor_compra = float(input("Digite o valor da compra: "))
valor_pago = float(input("Digite o valor pago: "))
#Subtrai o valor pago pelo da compra assim obtendo o troco
troco = valor_pago - valor_compra
print("O troco do cliente é: ",troco)