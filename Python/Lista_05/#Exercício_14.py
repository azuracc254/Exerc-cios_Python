#Exercício_14
#Lista_05
#Captando a entrada do usuário
cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Informe quantos anos você fuma: "))
#Calcula a quantidade de cigarros fumados 
#365 é a quantidade de dias do ano, a variavel anos e quantidade de anos fumando e cigarros_dia a quantidade fumada por dia
total_cigarro = cigarros_dia * 365 * anos
minutos = total_cigarro * 10
dias = minutos / 1440
print(f"Dias de vida perdidos: {dias:.2f}")