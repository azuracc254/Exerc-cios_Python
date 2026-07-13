#Exercício_06
#Lista_03
#Declara as variaveis de salário e comição que são fixas, ou seja são como constantes
salario = int(1600)
comicao = int(100)
#Recebe os valores pedidos
carros = float(input("Digite onúmero de carros vendidos: "))
vendas_valor = float(input("Digite o valor total das vendas: "))
#Calcula o salário final com base nso valores infromados
salario_final = salario + (comicao * carros) + (vendas_valor * 0.05)
print(f"O seu salario é {salario_final:.2f}")