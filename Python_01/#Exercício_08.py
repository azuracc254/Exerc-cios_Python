#Exercício_08
#Python 01
print("Calculo do cubo de um número e a média geométrica de dois números: ")
#Recebe os dois valores 
numero1 = float(input("Digite o valor do primeiro número: "))
numero2 = float(input("Digite o valor do segundo número: "))
#A variavel cubo recbe o numero1 elevado a 3
cubo = numero1** 3
#A biblioteca math é importada para que e o método math.sqrt() possa ser utilizado
import math
print(f"O cubo de {numero1} é {cubo}")
#Media_geometrica recebe a raiz de numero1 multiplicado pelo numero2
media_geometrica = math.sqrt(numero1 * numero2)
print(f"A média geométrica entre {numero1} e {numero2} é {media_geometrica:.2f}") 