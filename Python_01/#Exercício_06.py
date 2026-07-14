#Exercício_06
#Phython 01
delta = float(0)
print("Calculo de euquação de segundo grau ")
print("Apenas para equações que possuem os três componentes a, b, c")
print("Digite cada componete separadamente e sem o expoente")
print("Para componentes os quais são apenas letra ex: 'x', digite apenas o número '1'")
#lê os tres valores de uma equação de segundo grau
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de c: "))
#Fórmula de delta
delta = (b**2 - (4 * a * c))
#Exibe os três valores formatados para melhor entendimento
print(f"{a}x^2 + {b}x + {c}")
#Exibe o resultado
print(f"Delta = {delta}")