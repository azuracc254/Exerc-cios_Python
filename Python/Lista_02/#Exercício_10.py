#Exercício_10
#Lista_02
print("Determinando a classificação do triangulo: ")
#Recebe os Valores dos lados e base
base = float(input("Digite a base do triângulo: "))
lado1 = float(input("Digite o segundo lado do triângulo: "))
lado2 = float(input("Digite o terceiro lado do triângulo: "))
#Determina se é um triâmgulo e qual classificação
if base < lado1 + lado2 and lado1 < base + lado2 and lado2 < base + lado1:
    print("É um triangulo:\n")
    if lado1 == lado2 and base == lado1:
        print("Equilatero")
    elif lado1 == lado2 and base != lado1:
        print("Isórceles")
    elif lado1 != lado2 and base != lado1:
        print("Escaleno")