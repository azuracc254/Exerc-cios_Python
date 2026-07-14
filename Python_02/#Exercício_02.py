#Exercício_02
#Python 02
print("Calculo de valor do aluguel")
#Recebe os valores solicitados
tempo = int(input("Digite a quantidade de dias alugados: "))
kilometros = int(input("Digite a kilometragem rodada durante o tempo alugado: "))
#Calcula o preço do aluguel aplicando taxa de 0,15 po kilometro e 120 por dia
aluguel = (0.15 * kilometros) + (120 * tempo)
print(f"O preço do aluguel do veículo mediante o preço do dia alugado e da taxa por km é: {aluguel}R$")