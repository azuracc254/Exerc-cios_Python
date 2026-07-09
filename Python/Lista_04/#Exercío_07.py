#Exercío_07
#Lista_04
macas = int(input("Digite a quantidade de maçãs: "))
morangos = int(input("Digite a quantidade de morangos: "))
if macas >= 5:
    preco = 1.50 * macas
else:
    preco = 1.80 * macas
if macas >= 8 or preco > 25:
    preco = preco - (preco * 0.1)
print(f"O valor a ser pago pelo cliente é: {preco}")
if morangos >= 5:
    preco = 2.50 * macas
else:
    preco = 2.20 * macas
if macas >= 8 or preco > 25:
    preco = preco - (preco * 0.1)
print(f"O preço a ser pago pelo cliente é: {preco}")