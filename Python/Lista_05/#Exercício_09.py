#Exercício_09
#Lista_05
#Captando os valores e declarando as variaveis
numero = int(input("Digite um número inteiro: "))
divisor = int(0)
#Função range que gera um sequencia de 1 até a variavel numero
#O loop que sempre gurada o valor gerado em i
for i in range(1,numero):
    #numero que sera verificado e determinado ou não primo
    if numero % i == 0:
        #Verifica o resto da divisão exata entre i e numero
        #Isso acontecera ate que i se equipare a numero pois está sendo contado seus divisores 
        divisor = divisor + 1
if divisor == 1:
    #Matematicamente a quantidade de divisores deveria ser 2 para que o número seja primo
    #Mas neste caso a lista já começa por um, logo se fosse 2 o número nunca seria primo
    print(f"{numero} é primo")
else:
    print(f"{numero} não é primo")
    print(f"{numero} é dividivel por: ")
    #Loop que mostra por quais números o valor é divisivel caso o primeira condição fora do primeiro loop seja falsa
    for i in range(1,numero):
        if numero % i == 0:
            print(i)