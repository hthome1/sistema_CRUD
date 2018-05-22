# -*- coding: utf-8 -*-
"""
Created on Thu May 10 18:57:17 2018

@author: abrahao de weber
"""

import pygame
import sys
from pygame.locals import *
import random




#sys.path.append('./data')

janela = pygame.display.set_mode((1200, 333), 0, 32)
pygame.display.set_caption('Batalha Naval')
imagem = pygame.image.load("batalha.jpg").convert()
imagem2 = pygame.image.load("batalha.jpg").convert()
water = pygame.image.load("agua.png").convert()
img_botao = pygame.image.load("botao.png").convert()
preto = pygame.image.load("preto.png").convert()
coord = [731,28]
quadrado = [43,39]
tam_navio = [[43,39],[86,39],[129,39],[172,39]]
coord_navio = [[18,8],[18,70],[18,176],[118,8]]
navio1 = pygame.image.load("navio1.png").convert_alpha()
navio2 = pygame.image.load("navio2.png").convert_alpha()
navio3 = pygame.image.load("navio3.png").convert_alpha()
navio4 = pygame.image.load("navio4.png").convert_alpha()
navio1 = pygame.transform.rotate(navio1, 270)
navio2 = pygame.transform.rotate(navio2, 270)
navio3 = pygame.transform.rotate(navio3, 270)
navio4 = pygame.transform.rotate(navio4, 270)

listanavio = [navio1,navio2,navio3,navio4]

def Game():
    mousepressed_up = [False,-1]
    i = 1
    while True:
        janela.blit(imagem, (180, 0))
        janela.blit(imagem2,(690,0))
        janela.blit(preto, (0,0))
        
        xx,yy = pygame.mouse.get_pos()
        print(xx,yy)
        if mousepressed_up[0]:
            coord_navio[mousepressed_up[1]]=[xx,yy]
            
                    
                
        for event in pygame.event.get():
            for i in range(len(coord_navio)):
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if xx > coord_navio[i][0] and xx < coord_navio[i][0] + 39 and yy > coord_navio[i][1] and yy < coord_navio[i][1] + tam_navio[i][0]:
                        mousepressed_up=[True,i]
                if event.type == pygame.MOUSEBUTTONUP:
                    mousepressed_up=[False,i]

                if event.type == pygame.QUIT:
                    pygame.quit()
        for i in range(len(coord_navio)):
             janela.blit(listanavio[i], (coord_navio[i][0],coord_navio[i][1]))
                    
        i = 1
        x = 1
        
        while i < 11 and x < 8:
            if xx > coord[0]+(i-1)*quadrado[0] and yy > coord[1] + (x-1)*quadrado[1]  and xx < coord[0]+i*quadrado[0] and yy < coord[1] + x*quadrado[1]:
                janela.blit(img_botao,(coord[0]+(i-1)*quadrado[0],coord[1]+(x-1)*quadrado[1]))
            i += 1
            if i == 11:
                i = 1
                x += 1
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
                            				    
					
        pygame.display.update()
Game()


                
                        
            
            
            
            