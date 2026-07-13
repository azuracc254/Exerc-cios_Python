#Exercício_01
#Lista_05
#Recebendo so valores e declarando as variaveis
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco_unitario = float(input("Digite a o preço da unidade: "))
#Calcuando o valor total
total = preco_unitario * quantidade
#Determinado o disconto a ser aplicado de acordo com o valor total
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05
total_desconto = total - desconto
print("Produto ----",nome)
print("Total da compra já com descontos: ",total_desconto)