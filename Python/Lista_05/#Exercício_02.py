#Exercício_02
#Lista_05
media1 = float(input("Digite a média de sua primeira nota: "))
media2 = float(input("Digite a média da sua segunda nota: "))
media3 = float(input("Digite a média da sua terceira nota: "))
exercícios = float(input("Digite média do sexercícios: "))
media_aproveitamento = media1 + media2 * 2 + media3 * 3
if media_aproveitamento < 6.0:
    print("Conceito: D")
elif media_aproveitamento < 7.5:
    print("Conceito: C")
elif media_aproveitamento < 9:
    print("Conceito: B")
else:
    print("Conceito: A")