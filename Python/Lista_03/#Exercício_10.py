#Exercício_10
#Lista_03
#Declara as variáveis e recebe os válores
semana = int(4)
horas = int(input("Digite as horas trabalhadas: "))
valor_hora = float(input("Digite o valor da hora: "))
#Se a quantidade de horas trabalhadas for menor ou igual a 40 então o salário é calculado normalmente conforme a fórmula abaixo
if horas <= 40:
    salario = valor_hora * horas * semana
else:
#Caso contrário o valor da hora recebe um extra de cinco porcento
    extra = valor_hora + (valor_hora * 0.5)
    salario = extra * horas * semana
print("O seu salário é: ",salario)