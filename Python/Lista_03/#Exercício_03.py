#Exercício_03
#Lista_03
#Declara variáveis que funcionarão como constantes 
#dias do ano
#dias do mês
ano = int(365)
dias_mes = int(30)
print("Calculo da idade em dias\n")
#Recebe os valores pedidos e declras as variaveis
idade = int(input("Digite a sua idade (apenas em anos): "))
mes_atual = int(input("Digite o mês atual: "))
dia_atual = int(input("Inforome o dia atual: "))
#Fórmula que calcula a idadade em dias
total = (idade * ano) + (dias_mes * mes_atual) + dia_atual
print("Sua idade em dias é: ",total)