# KORBY  by Gu://3m and Ordnalessa
# PS: un 20/20 serait le bienvenu :)

import pygame, os, time, math
from random import randint

# init
os.system('cls')
pygame.init()

# load images
korby_r = pygame.image.load("korby_r.gif")
korby_l = pygame.image.load("korby_l.gif")
korby_s = pygame.image.load("korby_s.gif")
korby_j = pygame.image.load("korby__j.gif")
bg = pygame.image.load("bg.png")
# ig = pygame.image.load('ig.png')
# fg = pygame.image.load('level.png')

# vars definition
mousedwn = False
pas = 3
jpas = 1
xk = 900
yk = 600
xd = 0
jump=False
ckorby=korby_r


# window properties
window = pygame.display.set_mode((1800,1000))
pygame.mouse.set_visible(0)


# game loop (whole game, to keep the window open)
running=True
while running == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    window.fill((0,0,0))
    window.blit(bg,(0,0))
    window.blit(ckorby,(xk,yk))
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
            ckorby=korby_r
        if event.key==pygame.K_LEFT:
            xk=xk-pas
            ckorby=korby_l
        if event.key==pygame.K_UP:
            jump=True
            ckroby=korby_j
            for ijp in range(5):
                yk=yk-jpas/2
        # if event.key==pygame.K_DOWN:
            # if yk>600:
                # yk=yk+pas*2
        if event.key==pygame.K_ESCAPE:
            running=False
            pygame.quit()

    # if event.type==pygame.KEYUP and jump==False:


    if event.type==pygame.KEYUP and jump==False:
        ckroby=korby_s

    if event.type==pygame.KEYUP and jump==True:
        while yk<600:
            yk=yk+jpas*2
            window.blit(bg,(0,0))
            window.blit(ckorby,(xk,yk))
            pygame.display.flip()
        jump = False



pygame.quit()