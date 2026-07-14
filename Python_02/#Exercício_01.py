#Exercício_01
#Python 02
print("===Calculo de percentual de mercadoria===")
#Lê os valores solicitados
mercadoria = float(input("Digite o preço da mercadoria: "))
percentual = float(input("Digite o valor do percentual do desconto: "))
#realiza a operação que determina o valor do desconto
desconto = mercadoria * percentual / 100
#Subtrai o valor do produto pelo desconto, guarda e imprime o resultado
preco_final = mercadoria- desconto
print(f"Desconto: {desconto}\n Preço a pagar: {preco_final}")