#Exercício_06
#Lista_02
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
if numero1 > numero2 and numero2 > numero3:
    print(numero1," É maior")
elif numero1 > numero2 and numero2 < numero3:
    print(numero3," É maior")
elif numero2 > numero1 and numero1 > numero3:
    print(numero2," É maior")
elif numero2 > numero1 and numero2 > numero3:
    print(numero2," È maior")
elif numero3 > numero2 and numero2 > numero1:
    print(numero3," É maior")
elif numero3 > numero2 and numero2 > numero1:
    print(numero3," É maior") 