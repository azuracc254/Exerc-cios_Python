#Exercício_12
#lista_05
apartamento = int(75)
normal = int(292)
promocional = normal - (normal * 0.25)
arrecadacao_promocional = (apartamento * 0.8) * promocional
arrecadacao_normal = (apartamento * 0.5) * normal
diferenca = arrecadacao_promocional - arrecadacao_normal
print(f"Arrecadação promocional: {arrecadacao_promocional}")
print(f"Diaria promocional: {promocional}")
print(f"Arrecadação normal: {arrecadacao_normal}")
print(f"Diferença: {diferenca}")