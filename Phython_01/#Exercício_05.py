#Exercício_05
#Python 01
print("Calculo de distancia entre pontos específicos no plano cartesiano: ")
print("Digite as posições x e y do primeiro ponto no plano cartesiano")
print("Primeiro ponto:")
x1 = float(input("Posição x: "))
y1 = float(input("Posição Y: "))
print("Sgundo ponto")
x2 = float(input("Posição x: "))
y2 = float(input("Posição Y: "))
import math
distancia = math.sqrt(((x2 - x1)**2 + (y2 - y1)**2)**2)
simplificado = math.sqrt(distancia)
print(f"A distancia entre os dois pontos no plano cartesiano é: {distancia:.2f}")
print(f"Simplificando: ~{simplificado:.2f}")