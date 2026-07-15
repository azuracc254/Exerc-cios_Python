#Exercício_10
#Python 02
#Variavel que conta quantos números foram digigtados
contador = 0
#Variável que soma os números
soma = float(0)
#Variável que recebe a média aritimética
media_aritimetica = float(0)
#Variável que sempre recebe o número digitado 
i = int(1)
print("=====Digite quantos número inteiros quiser=====")
#Loop que sempre recebe um novo valor enquanto o mesmo não for zero
while i != 0:
    i = int(input("Digite o número: "))
    contador += 1
    if soma == 0:
        soma = i
    else:
        soma += i
media_aritimetica = soma / contador
print(f"A soma de todos os número digitados é: {soma}")
print(f"A quantidade de número inteiros digitados: {contador}")
print(f"A média aritimética é: {media_aritimetica}")