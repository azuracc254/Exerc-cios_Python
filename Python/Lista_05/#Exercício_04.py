#Exercício_04
#Lista_05
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
if numero2 == 0:
    while numero2 == 0:
        numero2 = float(input("Digite um divisor válido: "))
divisao = numero1 / numero2
print(f"O resltado da divisão é: {divisao}")
