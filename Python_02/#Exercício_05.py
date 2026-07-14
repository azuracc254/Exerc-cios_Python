#Exercício_05
#Python 02
#Lê os valores solicitados
casa_valor = float(input("Digite o valor  da casa: "))
salario = float(input("Digite o valor do salário: "))
anos_pagando = float(input("Digite a quantidade de anos de prestação: "))
#Calcula a quantidade de parcelas
parcelamento = 12 * anos_pagando
#Calcula o valor das prestações
valor_prestacao = casa_valor / parcelamento
#Verifica se o valor da prestação excede 30% do salario se sim a compra é recusada
if valor_prestacao > salario* 0.3:
    print("Não é possivel efetuar a compra da casa")
#Senão a compra é aprovada
else:
    print("Compra aprovada")