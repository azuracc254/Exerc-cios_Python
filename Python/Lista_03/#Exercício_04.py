#Exercício_04
#Lista_03
#Recebe o número de eleitores e votos sendo eles,brancos,nulos ou validos e delclara as variáveis
eleitores = int(input("Digite o total de eleitoes: "))
brancos = int(input("Digite o total de votos brancos: "))
nulos = int(input("Digite o total de votos nulos: "))
validos = int(input("Digite o total de votos validos: "))
#Calcula o percentual de cada um e os imprime na tela
brancos_percentual = (brancos * 100) / eleitores
print("Percentual de votos brancos: ",brancos_percentual)
nulos_percentual = (nulos * 100) / eleitores
print("Percentual de votos nulos: ",nulos_percentual)
validos_percentual = (validos * 100) / eleitores
print("Percentual de votos validos:",validos_percentual)