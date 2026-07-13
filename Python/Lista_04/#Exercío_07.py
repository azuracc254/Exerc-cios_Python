# Exercício_07
# Lista_04
# Recebe a quantidade de maçãs
macas = int(input("Digite a quantidade de maçãs: "))
# Recebe a quantidade de morangos
morangos = int(input("Digite a quantidade de morangos: "))
# Calcula o preço das maçãs conforme a quantidade
# Se comprar 5 ou mais, cada maçã custa 1.50; caso contrário, 1.80
if macas >= 5:
    preco = 1.50 * macas
else:
    preco = 1.80 * macas
# Aplica 10% de desconto se comprar 8 ou mais maçãs OU se o preço passar de 25
if macas >= 8 or preco > 25:
    preco = preco - (preco * 0.1)
# Mostra o valor calculado (até aqui, apenas das maçãs)
print(f"O valor a ser pago pelo cliente é: {preco}")
# mas está reutilizando a variável 'preco' e multiplicando por 'macas' em vez de 'morangos'.
if morangos >= 5:
    preco = 2.50 * morangos  
else:
    preco = 2.20 * morangos  
if morangos >= 8 or preco > 25:
    preco = preco - (preco * 0.1)
# Imprime novamente o preço, agora sobrepondo o valor anterior
print(f"O preço a ser pago pelo cliente é: {preco}")