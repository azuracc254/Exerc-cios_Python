#Jog0_posição aleatoria
import pygame
from pygame.locals import *
from sys import exit 
from random import randint
pygame.init()

branco = (255,255,255)
azul = (0, 0, 135)
vermelho = (135, 0, 0)

largura = 600
altura = 400
x = largura / 2
y = altura / 2
tela = pygame.display.set_mode((largura,altura))
tela.fill(branco)
fonte = pygame.font.Font(None, 45)
texto = fonte.render("You Lose!",True,azul, vermelho)

relogio = pygame.time.Clock()

x_azul = randint(40, 600)
y_azul = randint(50, 430)

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
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 20, 20))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 20, 20))
    #O método "colliderect()" detecta colisão entre dois retângulos "rect"
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 580)
        y_azul = randint(50, 380)  
    if x < 0 or x + 20 > largura or y < 0 or y + 20 > altura:
        exit()
    pygame.display.update()






#Listas em Python
#Cria uma lista e define seus valores e na linha seguinte recebe um novo valor 
#lista_var = [1,2,2]
#Lista_var.append(4)
#Importa a biblioteca math 
#import maht
#A função sum() no python soma os itens de uma lista
#soma_lista = sum(Lista_var)