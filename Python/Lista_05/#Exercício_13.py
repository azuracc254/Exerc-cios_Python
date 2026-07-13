#Exercício_13
#Lista_05
#CapatandO a entrada do usuário
shopps = float(input("Digite a quantidade de shops: "))
cobertura = float(input("Digite a quantidade de cobertura: "))
pessoas = float(input("Digite a quantidade de pessoas: "))
#Linha que calcula o valor do shops
valor_shopps = float(5 * shopps)
pizza = float(50 + (cobertura * 2.25))
#Linha que calcula o valor da pizza
total = valor_shopps + pizza
#Linha que calcula o valor total junto a goerjeta do garçom
total_garcom = total + (total * 0.1)
#Linha que divide o valor total pela quantidade de pessoas
dividido = total_garcom / pessoas
#Exibe os resultados
print(f"Valor da compra: {total_garcom}")
print(f"O valor toal dividido entre as: {pessoas}\n {dividido:.2f}")