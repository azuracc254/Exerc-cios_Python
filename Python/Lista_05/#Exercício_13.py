#Exercício_13
#Lista_05
shopps = float(input("Digite a quantidade de shops: "))
cobertura = float(input("Digite a quantidade de cobertura: "))
pessoas = float(input("Digite a quantidade de pessoas: "))
valor_shopps = float(5 * shopps)
pizza = float(50 + (cobertura * 2.25))
total = valor_shopps + pizza
total_garcom = total + (total * 0.1)
dividido = total_garcom / pessoas
print(f"Valor da compra: {total_garcom}")
print(f"O valor toal dividido entre as: {pessoas}\n {dividido:.2f}")