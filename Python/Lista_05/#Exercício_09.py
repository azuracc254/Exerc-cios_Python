#Exercício_09
#Lista_05
numero = int(input("Digite um número inteiro: "))
divisor = int(0)
for i in range(1,numero):
    if numero % i == 0:
        divisor = divisor + 1
if divisor == 1:
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
    print(f"{numero} é dividivel por: ")
    for i in range(1,numero):
        if numero % i == 0:
            print(i)