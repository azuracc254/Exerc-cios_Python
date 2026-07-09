#Exercício_06
#Lista_03
salario = int(1600)
comicao = int(100)
carros = float(input("Digite onúmero de carros vendidos: "))
vendas_valor = float(input("Digite o valor total das vendas: "))
salario_final = salario + (comicao * carros) + (vendas_valor * 0.05)
print(f"O seu salario é {salario_final:.2f}")