import pygame
from pygame.locals import *
from sys import exit 
pygame.init()

branco = (255,255,255)
largura = 600
altura = 400

tela = pygame.display.set_mode((largura,altura))
while True:
    #Basicamnete pega um evento e seu tipo o tempo todo
    for event in pygame.event.get():
        #Verifica se o seu tipo é "Quit" -> "Sair"
        if event.type == QUIT:
            #Se for o caso é executado o método "exit()" que encerra a execução
            exit()
    #"pygame.draw" é um método que desenha algo na tela neste caso o "rect" -> retângulo
    #Seus parâmetros são: tela em que será exobido, cor no espectro rgb, posição e proporção (altura e largura)
    pygame.draw.rect(tela, (255, 0, 0), (200, 305, 60, 40))
    #Dependendo da forma geométrica a forma de listar os parâmetros muda um pouco mas o prin´cioio é o mesmo
    #Primeiro escolha a tela, depois a cor, onde começa no eixo X, A altura no Y, Onde termina no X, e  altura da outra ponta no Y.
    pygame.draw.line(tela, (0, 255, 0), (0, 350), (600, 350), 5)
    #Tão como tambem acontece com o circulo, que ao invés de listar altura e largura é dito apenas o raio
    pygame.draw.circle(tela, (255, 255, 0), (305,305), 40)
    #Atualiza o que está sendo exibido, sem ele a téla ficaria sem nada
    pygame.display.update()





#Listas em Python
#Cria uma lista e define seus valores e na linha seguinte recebe um novo valor 
#lista_var = [1,2,2]
#Lista_var.append(4)
#Importa a biblioteca math 
#import maht
#A função sum() no python soma os itens de uma lista
#soma_lista = sum(Lista_var)