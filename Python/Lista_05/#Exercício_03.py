#Exercício_03
#Lista_05
#Recebendo os valores e dclarando variaveis
numero = input("Digite o seu número: ")
nome = input("Digite o seu nome completo: ")
nascimento = int(input("Digite o ano de seu nascimento: "))
engressamento = int(input("Digite o seu ano de engressamento na empresa: "))
#Ano atual é listado paraque seja possivel verificar as datas
#Tambem é possovel fazer isso utilizando as bibliotécas timedate() e deltatime()
ano_atual = 2026
idade = ano_atual - nascimento
anos_trabalhados = ano_atual - engressamento 
#Condições que verificam se o susario é qualificado ou não
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