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

pontos_final = int(0)
pontos = int(0)

fonte_derrota = pygame.font.Font(None, 45)
fonte_durante = pygame.font.Font(None, 25)

relogio = pygame.time.Clock()

x_azul = randint(40, 600)
y_azul = randint(50, 430)

while True:
    tela.fill(branco)
    relogio.tick(35)
    texto_durante = fonte_durante.render(f"Score: {pontos}", True, azul)
    tela.blit(texto_durante, (10, 10))
    #Basicamente pega um evento e seu tipo o tempo todo
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
                y = y + 5
        #Verifica se a pessoa selecionou sair
        if event.type == QUIT:
            #Executa o método exit()
            exit()
    #Verifica qual tecla foi pressionada
    if pygame.key.get_pressed()[K_a]:
        x = x - 5
    if pygame.key.get_pressed()[K_d]:
        x = x + 5
    if pygame.key.get_pressed()[K_w]:
        y = y - 5
    if pygame.key.get_pressed()[K_s]:
        y = y + 5
    #"pygame.draw" é um método que desenha algo na tela, neste caso o "rect" -> retângulo
    #Seus parâmetros são: tela em que será exibido, cor no espectro RGB, posição e proporção (altura e largura)
    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 20, 20))
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 20, 20))
    #O método "colliderect()" detecta colisão entre dois retângulos "rect"
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(40, 580)
        y_azul = randint(50, 380)
        pontos = pontos + 1
        pontos_final = pontos

    #Verifica se o player encostou nas bordas da tela
    if x < 0 or x + 20 > largura or y < 0 or y + 20 > altura:
        #Exibe um texto de derrota na tela
        texto_derrota = fonte_derrota.render(f"You Lose!\n Score: {pontos_final}", True, azul, vermelho)
        tela.fill(branco)
        tela.blit(texto_derrota, (100, 180))
        pygame.display.update()
        #Pega o evento que acabou de ocorrer
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                #Verifica se é a tecla Enter
                if event.type == KEYDOWN:
                    if event.key == K_RETURN or event.key == K_KP_ENTER:
                        exit()

    pygame.display.update()




#Listas em Python
#Cria uma lista e define seus valores e na linha seguinte recebe um novo valor
#lista_var = [1,2,2]
#lista_var.append(4)
#Importa a biblioteca math
#import math
#A função sum() no Python soma os itens de uma lista
#soma_lista = sum(lista_var)