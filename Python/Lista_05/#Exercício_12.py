#Exercício_12
#lista_05
#Declaração dos valores dos apartamentos
apartamento = int(75)
normal = int(292)
#Calculo do promocional
promocional = normal - (normal * 0.25)
#Calculo da arecadação do promocional
arrecadacao_promocional = (apartamento * 0.8) * promocional
#Arrecadação normal
arrecadacao_normal = (apartamento * 0.5) * normal
#Diferença dos valores, ou seja, subtração
diferenca = arrecadacao_promocional - arrecadacao_normal
#Exibindo os resultados
print(f"Arrecadação promocional: {arrecadacao_promocional}")
print(f"Diaria promocional: {promocional}")
print(f"Arrecadação normal: {arrecadacao_normal}")
print(f"Diferença: {diferenca}")