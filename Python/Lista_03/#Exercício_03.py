#Exercício_03
#Lista_03
ano = int(365)
dias_mes = int(30)
from datetime import date
from datetime import timedelta
print("Calculo da idade em dias\n")
idade = int(input("Digite a sua idade (apenas em anos): "))
mes_atual = int(input("Digite o mês atual: "))
dia_atual = int(input("Inforome o dia atual: "))
total = (idade * ano) + (dias_mes * mes_atual) + dia_atual
print("Sua idade em dias é: ",total)