#Exercício_05
#Lista_04
print("A-alcool  G-gasolina")
combustivel = input("Digite o tipo de combistivel: ")
combustivel_m = combustivel.upper()
litros = int(input("Digite a quantidade desejada: "))
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