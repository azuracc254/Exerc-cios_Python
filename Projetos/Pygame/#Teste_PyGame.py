#Teste_PyGame
import pygame
from pygame.locals import *
from sys import exit 
pygame.init()

largura = 640
altura = 480

tela = pygame.dysplay.set_mode((largura,altura))
while True:
    for event in pygame.event.get():
        if event.type == quit:
            exit()

pygame.display.pygame.display.update()