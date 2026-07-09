#Exercício_14
#Lista_05
cigarros_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos = int(input("Informe quantos anos você fuma: "))
total_cigarro = cigarros_dia * 365 * anos
minutos = total_cigarro * 10
dias = minutos / 1440
print(f"Dias de vida perdidos: {dias:.2f}")