#Exercício_04
#Lista_04
time1 = input("Digite o nome do primeiro time: ")
gols1 = int(input("Digite a quantidade de gols: "))
time2 = input("Digite o nome do time adversário: ")
gols2 = int(input("Digite a quantidade de gols: "))
if gols1 > gols2:
    print(f"{time1} é o vencedor ")
else: 
    print(f"{time2} é o vencedor ")