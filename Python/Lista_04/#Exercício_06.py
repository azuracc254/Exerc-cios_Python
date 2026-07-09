#Exercício_06
#Lista_04
homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))
mulher1 = int(input("Digite a idade da priemira mulher: "))
mulher2 = int(input("Digite a idade da segunda mulher: "))
if homem1 > homem2:
    homem_velho = homem1
    homem_novo = homem2
else:
    homem_velho = homem2
    homem_novo = homem1
if mulher1 > mulher2:
    mulher_velha = mulher1
    mulher_nova = mulher2
else:
    mulher_velha = mulher2
    mulher_nova = mulher1
soma = homem_velho + mulher_nova
produto = mulher_velha * homem_novo
print(f"A soma do homem velho com a mulher nova é: {soma}")
print(f"O produto do home novo com a mulher velha é: {produto}")