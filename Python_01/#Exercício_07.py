#Exercício_07
#Phython 01
print("Calculo de salário")
#Declaração das variaveis slario_base e comisao que serão as constantes
salario_base = int(2500)
comisao = int(200)
#Recebe os valores 
numero_vendas = int(input("Digite o número de imóveis vendidos: "))
valor_vendas = float(input("Digite o valor total das vendas: "))
#Caclcula o valor de cada venda dividindo o valor total pelo número de cada venda
cadavenda = valor_vendas / numero_vendas
#Calcula o salário final do vendedor
salario_final = salario_base + (comisao * numero_vendas + (numero_vendas * (cadavenda * 0.05)))
print(f"O salário final é {salario_final}")