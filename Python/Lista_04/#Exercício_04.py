#Exercício_04
#Lista_04
#Recebe os nomes e quantidade de gols dos times e declara as variáveis
time1 = input("Digite o nome do primeiro time: ")
gols1 = int(input("Digite a quantidade de gols: "))
time2 = input("Digite o nome do time adversário: ")
gols2 = int(input("Digite a quantidade de gols: "))
#Se gols1 maior que gols2 o time o é vencedor
if gols1 > gols2:
    print(f"{time1} é o vencedor ")
#Senão o time 2 é vencedor
else: 
    print(f"{time2} é o vencedor ")