#Exercício_10
#Lista_04
#Importando a constante "pi" da biblioteca math, necessário para a fórmula da area do circulo
from math import pi
raio = float(input("Digite o raio de um circulo: "))
#Fórmula pra calcular a area
area = pi * (raio ** 2)
print(f"A area do circulo é: {area:.2f}")