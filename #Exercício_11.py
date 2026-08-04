#Exercício_11
#Python 02
#Programa para validar um CPF
#Pede o CPF para o usuário
cpf = input("Digite um CPF (apenas números): ")
#Remove espaços entre os digitos
cpf = cpf.strip()
#Verifica se o CPF tem apenas números
if not cpf.isdigit():
    print("CPF inválido! Digite apenas números.")
    exit()
#Verifica se o CPF tem 11 dígitos
if len(cpf) != 11:
    print("CPF inválido! O CPF deve ter 11 números.")
    exit()
#Verifica se todos os números são iguais
if cpf == cpf[0] * 11:
    print("CPF inválido!")
    exit()
soma = 0
peso = 10
for i in range(9):
    soma += int(cpf[i]) * peso
    peso -= 1
resto = (soma * 10) % 11
if resto == 10:
    resto = 0
#Se o primeiro dígito estiver errado, o CPF é inválido
if resto != int(cpf[9]):
    print("CPF inválido!")
    exit()
soma = 0
peso = 11
for i in range(10):
    soma += int(cpf[i]) * peso
    peso -= 1
resto = (soma * 10) % 11
if resto == 10:
    resto = 0
# Verifica o segundo dígito
if resto != int(cpf[10]):
    print("CPF inválido!")
    exit()
#Se leu até essa linha então funciona
print("CPF válido!")