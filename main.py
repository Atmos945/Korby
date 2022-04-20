# KORBY  by LastMeridian_, Ordnalessa, Cofordix, and Lelequeen
# PS: un 20/20 serait le bienvenu :)
version = 'Version Dev 1.3.7'


import pygame, os, random, time, math, ctypes, csv

# init
os.system('cls')
pygame.init()
print(version)

# load images
korby_rframes = [ pygame.image.load("assets/korby_r1.png"), pygame.image.load("assets/korby_r2.png"), pygame.image.load("assets/korby_r3.png"), pygame.image.load("assets/korby_r4.png"), pygame.image.load("assets/korby_r5.png"), pygame.image.load("assets/korby_r6.png"), pygame.image.load("assets/korby_r7.png"), pygame.image.load("assets/korby_r8.png") ]
korby_lframes = [ pygame.image.load("assets/korby_l1.png"), pygame.image.load("assets/korby_l2.png"), pygame.image.load("assets/korby_l3.png"), pygame.image.load("assets/korby_l4.png"), pygame.image.load("assets/korby_l5.png"), pygame.image.load("assets/korby_l6.png"), pygame.image.load("assets/korby_l7.png"), pygame.image.load("assets/korby_l8.png") ]
korby_s = pygame.image.load("assets/korby_s.png")
korby_j = pygame.image.load("assets/korby_j.png")
korby_f = pygame.image.load("assets/korby_f.png")
korby_fl = pygame.image.load("assets/korby_fl.png")
korby_fr = pygame.image.load("assets/korby_fr.png")
korby_i = pygame.image.load("assets/korby_i.png")
bg = pygame.image.load("assets/bg.png")
# ig = pygame.image.load('ig.png')
# fg = pygame.image.load('level.png')

# vars definition
user32 = ctypes.windll.user32
screensize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
print('Screen Resolution ',screensize)
print("Note that screens with low resolution or high scaling are not supported")
xk = 900
yk = 600
xd = 0
mousedwn = False
pas = 60
jpas = 4
# import csv kbctrl
jump=False
flight=False
ckorby=korby_s 
kccsv = open('kbctrl.csv', 'w', encoding='UTF8')
kpressed = pygame.key.get_pressed()
clock= pygame.time.Clock()
frame = 0

def korby_r_a(): 
    clock.tick(12)
    global frame
    if frame >= len(korby_rframes):
        frame = 0
    else :
        frame=frame
    korby_r = korby_rframes[frame]
def korby_l_a(): 
    clock.tick(12)
    global frame
    if frame >= len(korby_lframes):
        frame = 0
    else :
        frame=frame
    korby_l = korby_lframes[frame]


# window properties
window = pygame.display.set_mode((1800,1000))
# pygame.mouse.set_visible(0)
pygame.display.set_icon(korby_i)
pygame.display.set_caption('SuperKorby 3000 premium deluxe')


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
        
        # detect mouse click
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        mousedwn=True
    if event.type==pygame.MOUSEBUTTONUP and event.button==1:
        mousedwn=False

    # curseur custom
    # if event.type == pygame.MOUSEMOTION and pause == True:
        # xm=event.pos[0]
        # ym=event.pos[1]
    
    # keyboard controls
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            if flight==True:
                    xk=xk+pas/10
                    yk=yk+jpas
                    ckorby = korby_fr
            else:
                frame=frame+1
                korby_r_a()
                xk=xk+pas
                ckorby=korby_rframes[frame]

        if event.key==pygame.K_LEFT:
            if flight==True:
                xk=xk-pas/10
                yk=yk+jpas
                ckorby = korby_fl
            else:
                frame=frame+1
                korby_l_a()
                xk=xk-pas
                ckorby=korby_lframes[frame]

        if event.key==pygame.K_UP:
            flight=True
            ckorby=korby_j
            if yk>-150:
                yk=yk-jpas*3.5

        if event.key==pygame.K_DOWN:
            # if yk>600:
            yk=yk+pas*6

        if event.key==pygame.K_SPACE:
            print('K pressed')
            # replace by input()
            kcright = 'pygame.K_RIGHT'
            kcleft = 'pygame.K_LEFT'
            kcup = 'pygame.K_UP'
            kcp = 'pygame.K_p'
            kbctrl = [kcright, kcleft, kcup, kcp]
            # export as csv
            kcwriter = csv.writer(kccsv)
            kcwriter.writerow(kbctrl)
            kccsv.close

        if event.key==pygame.K_ESCAPE:
            running=False
            pygame.quit()


    if event.type==pygame.KEYUP and flight==False:
        ckorby=korby_s

    if event.type==pygame.KEYUP and flight==True:
        ckorby = korby_f
        
        if yk<600:
            yk=yk+jpas*4
            window.blit(bg,(0,0))
            window.blit(ckorby,(xk,yk))
            pygame.display.flip()


    if yk>=600:
        flight=False
        yk = 600


pygame.quit()