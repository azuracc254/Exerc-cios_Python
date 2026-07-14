#Exercício_09
#Python 01
#Declara as variaveis e guarda laranja e suco
suco1 = 'laranja'
suco2 = 'acerola'
print(suco1," ",suco2)
#A variavel troca recebe suco1 para servir como backup
#Em seguida a variavel suco 1 recebe suco2 e suco2 recebe troca, assim trocando as variaveis 1 e 2
troca = suco1
suco1 = suco2
suco2 = troca
print(suco1," ",suco2)