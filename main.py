# KORBY  by Gu://3m and Ordnalessa
# PS: un 20/20 serait le bienvenu :)

import pygame, os, time, math
from random import randint

# init
os.system('cls')
pygame.init()

# load images
korby = pygame.image.load("korby droite.png")
korby2 = pygame.image.load("korby droite 2.png")
korbyg = pygame.image.load("korby gauche.png")
korbyg2 = pygame.image.load("korby gauche 2.png")
bg = pygame.image.load("testbg1.jpg")

# window properties
window = pygame.display.set_mode((1800,1000))
pygame.mouse.set_visible(0)

# vars definition
mousedwn = False
pas = 3
jpas = 0.5
xk = 900
yk = 600
xd = 0


# game loop (whole game, to keep the window open)
running=True
while running == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    window.fill((0,0,0))
    window.blit(bg,(0,0))
    window.blit(korby,(xk,yk))
    pygame.display.flip()
        
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        mousedwn=True
        # avaler/recracher
    if event.type==pygame.MOUSEBUTTONUP and event.button==1:
        mousedwn=False

    # curseur custom
    # if event.type == pygame.MOUSEMOTION:
        # xm=event.pos[0]
        # ym=event.pos[1]
    
    # keyboard controls
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            xd=xd+pas
            # + animation
        if event.key==pygame.K_LEFT:
            xd=xd-pas
        if event.key==pygame.K_UP:
            jump=True
            for ijp in range(5):
                yk=yk-jpas/2
        if event.key==pygame.K_DOWN:
            if yk>600:
                yk=yk+pas*2
        if event.key==pygame.K_ESCAPE:
            running=False
            pygame.quit()

    if event.type==pygame.KEYUP and jump==True:
        while yk<600:
            yk=yk+jpas
            window.blit(bg,(0,0))
            window.blit(korby,(xk,yk))
            pygame.display.flip()
        jump = False



pygame.quit()