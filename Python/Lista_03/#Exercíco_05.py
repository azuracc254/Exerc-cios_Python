#Exercíco_05
#Lista_03
#Recebe o valor de fábrica de um carro e então delcara um variável 
carro_fabrica = float(input("Digite o valor de fábrica de um carro: "))
#Calcula o valor final com os juros
valor_final = carro_fabrica + (carro_fabrica * 0.45) + (carro_fabrica * 0.28)
print("O valor final do carro deve ser: ",valor_final)