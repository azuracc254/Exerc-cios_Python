#Exercício_01
#Lista_05
nome = input("Digite o nome do produto: ")
quantidade = int(input("Digite a quantidade: "))
preco_unitario = float(input("Digite a o preço da unidade: "))
total = preco_unitario * quantidade
if quantidade <= 5:
    desconto = total * 0.02
elif quantidade <= 10:
    desconto = total * 0.03
else:
    desconto = total * 0.05
total_desconto = total - desconto
print("Produto ----",nome)
print("Total da compra já com descontos: ",total_desconto)