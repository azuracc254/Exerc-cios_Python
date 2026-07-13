#Exercício_12
#Lista_02
#Recebe nome e idade de duas pessoas
nome1 = input("Digite o nome da primeira pessoa: ")
idade1 = int(input("Digite a sua iadade: "))
nome2 = input("Digite o nome da segunda pessoa: ")
idade2 = int(input("Digite a idade da segunda pessoa: "))
#Verifica quem é mais vleho e imprime seu nome
if idade1 < idade2:
    print(nome2,": É mais velho(a)")
else:
    print(nome1,": É mais velho(a)")