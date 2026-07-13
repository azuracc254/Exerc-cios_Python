#Exercício_03
#Lista_02
#Recebe um valor
print("Verificando se é maior, menor ou igual a zero: \n")
numero = float(input("Digite o número que deseja verificar: "))
#Determina se é maior, igual ou menor que zero
if numero == 0:
    print(numero," É igual a zero!")
elif numero > 0:
    print(numero," É maior que zero!")
elif numero < 0:
    print(numero," É menor que zero!")