#Exercício_10
#Lista_05
#Capatando os valores listados pelo usuario e declarando variaveis
print("Calculo apenas com  multiplicações ")
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = int(1)
#calcula o potencia do número sem finções apenas com multiplicações
#Multiplica o número por ele mesmo pela quantidade de vezes listadas na variavel expoente 
for i in range(expoente):
    resultado = resultado * base
print("O resultado é: ",resultado)