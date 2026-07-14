#Exercício_06
#Python 02
#Recebe os valores solicitados
kwh = int(input("Digite a quantidade KWH de consumo de energia elétrica: "))
print("R-Residencia   I-Industrias   C-Comércios")
esc = input("Digite o tio de instalação: ")
#Transforma o text recbedido em maisculo
tipo = esc.upper()
#Verifica o tipo e o consumo e determina o valor por kwh
if tipo == 'R' and kwh <= 500:
    preco = 0.40 * kwh
elif tipo == 'R' and kwh > 500:
    preco = 0.65 * kwh
elif tipo == 'C'and kwh <= 1000:
    preco = 0.55 * kwh
elif tipo == 'C' and kwh > 1000:
    preco = 0.60 * kwh
elif tipo == 'I' and kwh <= 5000:
    preco = 0.55 * kwh
elif tipo == 'I' and kwh > 5000:
    preco = 0.60 * kwh
print(f"O preço a pagar é: {preco}R$") 