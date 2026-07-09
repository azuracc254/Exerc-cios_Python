#Exercício_10
#Lista_03
semana = int(4)
horas = int(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))
if horas <= 40:
    salario = valor_hora * horas * semana
else:
    extra = valor_hora + (valor_hora * 0.5)
    salario = extra * horas * semana
print("O seu salário é: ",salario)