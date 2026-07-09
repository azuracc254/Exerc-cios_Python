#Exercício_07
#Lista_01
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))
numero3 = float(input("Digite o terceiro número: "))
if numero1 > numero2 and numero2 > numero3:
    print(numero1," ",numero2," ",numero3)
else:
    if numero1 > numero2 and numero2 < numero3:
        print(numero1," ",numero3," ",numero2)
    else: 
        if numero2 > numero1 and numero1 > numero3:
            print(numero2," ",numero1," ",numero3)
        else: 
            if numero2 > numero1 and numero2 > numero3:
                print(numero2," ",numero3," ",numero1)
            else: 
                if numero3 > numero2 and numero2 > numero1:
                    print(numero3," ",numero2," ",numero1)
                else: 
                    if numero3 > numero2 and numero2 < numero1:
                        print(numero3," ",numero1," ",numero2)