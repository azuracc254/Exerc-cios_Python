#Exercício_03
#Lista_05
numero = input("Digite o seu número: ")
nome = input("Digite o seu nome completo: ")
nascimento = int(input("Digite o ano de seu nascimento: "))
engressamento = int(input("Digite o seu ano de engressamento na empresa: "))
ano_atual = 2026
idade = ano_atual - nascimento
anos_trabalhados = ano_atual - engressamento 
if idade >= 65:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Tempo de trabalho: {anos_trabalhados}")
    print("Qualificado para aposentadoria!")
elif anos_trabalhados >= 30:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Tempo de trabalho: {anos_trabalhados}")
    print("Qualificado para aposentadoria!")
elif idade>= 60 and anos_trabalhados >= 25:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Tempo de trabalho: {anos_trabalhados}")
    print("Qualificado para aposentadoria!")
else:
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Anos trabalhados: {anos_trabalhados}")
    print("Desqualificado para aposentadoria!")