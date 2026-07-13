#Exercício_11
#Lista_05
#Declaração das varieveis e de seus tipos
soma = int(0)
primo = bool()
num = int(0)
#Funcção que gera uma sequencia de números de um tamnaho especificado
#Loop que determina o número de repetições
#Intenção: 1 a 100, execução: 2 a 101, isso porque o número 1 de qualquer jeito é número primo
for num in range(2,101):
    #Varivel que armazena a infromação de que um número é ou não primo
    #Para facilitar o número já é primo até que a condição que verifica isso se torne verdadeira
    primo = bool(True)
    #Loop que testara num por ele mesmo e todos os antecesores
    for i in range(2, int(num ** 0.5) + 1):
        #Condição que verifica se o resto é zero
        if num % i == 0:
            #caso seja verdadeiro, primo é falso
            primo = False
    if primo:
        #Caso seja logo a variavel soma recebe  + num
        soma += num
print(f"A soma de todos os números primos entre 1 e 100 é: {soma}") 