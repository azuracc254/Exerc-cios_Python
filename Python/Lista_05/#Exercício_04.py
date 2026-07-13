#Exercício_04
#Lista_05
#Capatandos os valores e declarando variaveis
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
#Verifica se o segundo número é igua a zero, pois caso seja, é pedido ao usuario que passe outro
#Pouis caso o segundo número seja zero não é possivel realizar a operação de divisão
if numero2 == 0:
    while numero2 == 0:
        numero2 = float(input("Digite um divisor válido: "))
divisao = numero1 / numero2
print(f"O resltado da divisão é: {divisao}")
