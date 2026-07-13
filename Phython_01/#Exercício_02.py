#Exercício_02
#Phython 01
print("Calculo de comprimento de circunfencia")
#Importa a constante pi 
from math import pi
#Lê o valor do raio da circunferencia
raio = float(input("Digite o raio da circunferencia: "))
#Com base na fórmula é calculado o comprimento
comprimento = 2 * pi * raio
print(f"O comprimento é: {comprimento:.2f}")