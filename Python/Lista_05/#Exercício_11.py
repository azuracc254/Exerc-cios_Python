#Exercício_11
#Lista_05
soma = int(0)
primo = bool()
num = int(0)
for num in range(2,101):
    primo = bool(True)
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            primo = False
    if primo:
        soma += num
print(f"A soma de todos os números primos entre 1 e 100 é: {soma}") 