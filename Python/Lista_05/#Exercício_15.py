#Exercício_15
#Lista_05
acima5 = 0
divisivel3 = 0
import random
#Gera uma sequência de números de tamamho e intrvalo especificado e armazena em i
for i in range(21):
    #Método random.randrange( ) que gera um número aleatório num intervalo específico 
    num = int(random.randrange(0,20))
    print(num)
    if num > 5:
        acima5 += 1
        if num % 3 == 0:
            #Verifica se o resto da divisão é zero, caso verdadeiro significa que num é divisivel por três
            divisivel3 += 1
            #Caso a condição acima for verdadeira o contador divisicvel3 recebe ele mesmo mais o valor um
print(f"Quantidade de números acima de cinco: {acima5}")
print(f"Quantidade de números divisiveis por três: {divisivel3}")