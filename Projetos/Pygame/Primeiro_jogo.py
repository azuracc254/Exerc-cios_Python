import pygame
from pygame.locals import *
from sys import exit 
pygame.init()

branco = (255,255,255)
largura = 600
altura = 400
x = largura / 2
y = altura / 2
tela = pygame.display.set_mode((largura,altura))
tela.fill(branco)

relogio = pygame.time.Clock()

while True:
    tela.fill(branco)
    relogio.tick(35)
    #Basicamnete pega um evento e seu tipo o tempo todo
    for event in pygame.event.get():
        #Verifica se uma tecla foi clicada
        if event.type == KEYDOWN:
            #Verifica qual tecla foi clicada
            if event.key == K_a:
                x = x -5
            elif event.key == K_d:
                x = x + 5
            elif event.key == K_w:
                y = y - 5
            elif event.key == K_s:
                y = y - 5
        #Verifica se a pessoa selecionou sair
        if event.type == QUIT:
            #Exercuta o metodo exit()
            exit()
    #Verifica qual tecla foi precionada
    if pygame.key.get_pressed()[K_a]:
        x = x - 5
    if pygame.key.get_pressed()[K_d]:
        x = x + 5
    if pygame.key.get_pressed()[K_w]:
        y = y - 5
    if pygame.key.get_pressed()[K_s]:
        y = y + 5
    #"pygame.draw" é um método que desenha algo na tela neste caso o "rect" -> retângulo
    #Seus parâmetros são: tela em que será exibido, cor no espectro rgb, posição e proporção (altura e largura)
    pygame.draw.rect(tela, (255, 0, 0), (x, y, 30, 30))
    pygame.display.update()






#Listas em Python
#Cria uma lista e define seus valores e na linha seguinte recebe um novo valor 
#lista_var = [1,2,2]
#Lista_var.append(4)
#Importa a biblioteca math 
#import maht
#A função sum() no python soma os itens de uma lista
#soma_lista = sum(Lista_var)