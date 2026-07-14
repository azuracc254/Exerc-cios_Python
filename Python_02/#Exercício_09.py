#Exercício_09
#Python 02
deposito = float(input("Digite o valor inicial da poupansa: "))
taxa = float(input("Digite a taxa de juros mensais: "))
deposito_mensal = float(input("Digite o valor depositado mensalmente"))
rendimento = int(0)
for i in range(24,0,-1):
    if rendimento == 0:
        rendimento = deposito + (deposito * taxa / 100)
        rendimento += deposito_mensal
        print(f"Mês: {i} rendimento atual: {rendimento}")
    else:
        rendimento += (deposito * taxa) / 100
        rendimento += deposito_mensal
        print(f"Mês: {i} rendimento atual: {rendimento}")
print(f"O total no final dos 24 meses é: {rendimento}")