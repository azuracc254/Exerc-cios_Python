#Exercício_15
#Lista_05
acima5 = 0
divisivel3 = 0
import random
for i in range(21):
    num = int(random.randrange(0,20))
    print(num)
    if num > 5:
        acima5 += 1
        if num % 3 == 0:
            divisivel3 += 1
print(f"Quantidade de números acima de cinco: {acima5}")
print(f"Quantidade de números divisiveis por três: {divisivel3}")