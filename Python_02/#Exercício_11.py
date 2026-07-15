#Exercício_11
#Python 02
import math
verificador2 = int(0)
multiplicador = int(10)
contador = int(0)
contador2 = int(0)
digitos = int(0)
resto11 = int(0)
resto11_2 = int(0)
soma = int(0)
soma2 = int(0)
cpf = int(0)
cpf = int(input("Digite o seu CPF para realizar a validação: "))
cpf_string = str(cpf)
digitos = int(math.log10(cpf))
for i in range(len(cpf_string)):
    c = cpf_string[contador]
    c1 = int(c)
    c1 = c1 * multiplicador
    soma += c1
    multiplicador -= 1
    if contador < 11:
        contador += 1
        resto11 = soma % 11
        divisao_perfeita = int(soma // 11)
        if resto11 == 0 or resto11 == 1:
            verificador1 = int(0)
        elif resto11 in range(1,11):
            verificador1 = int(11 - resto11)
            verificador1 = abs(verificador1)
    if verificador1 == int(cpf_string[9]):
        for l in range(len(cpf_string)):
            e = cpf_string[contador2]
            e1 = int(e)
            multiplicador = int(11)
            soma2 += (e1 * multiplicador)
            multiplicador -= 1
            if contador2 < 12:
                contador2 += 1
                resto11_2 = soma2 % 11
                divisao_perfeita2 = int(soma // 11)
                if resto11_2 in range(1,12):
                    verificador2 = int(11 - resto11_2)
                    verificador2 = abs(verificador2)
        if verificador2 == int(cpf_string[10]):
            print("CPF válido")
        else: 
            print("CPF inválido")
    else:
        print("CPF inválido")