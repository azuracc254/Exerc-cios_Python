#Exercício_05
#Lista_04
print("A-alcool  G-gasolina")
#Recebe a escolha dos combustiveis
combustivel = input("Digite o tipo de combistivel: ")
#Transforma o que for minusculo e maiusculo para simplificar a lógica
combustivel_m = combustivel.upper()
#Lê quantidade
litros = int(input("Digite a quantidade desejada: "))
#Verifica a quantidade e tipo e calcula o preço desconto de cordo
if combustivel_m == "A" and litros <= 20:
    preco = 3.90 * litros
    preco = preco - (preco * 0.03)
    print(f"O preço é: {preco:.2f}")
elif combustivel_m == "A" and litros > 20:
    preco = 3.90 * litros
    preco = preco - (preco * 0.05)
    print(f"O preço é: {preco:.2f}")
elif combustivel_m == "B"  and litros <= 20:
    preco = 6.30 * litros
    preco = preco - (preco * 0.04)
    print(f"O preço é: {preco:.2f}")
elif combustivel_m == "b" and litros > 20:
    preco = 6.30 * litros
    preco = preco - (preco * 0.06)
    print(f"O preço é: {preco:.2f}")