# KORBY  by LastMeridian_, Ordnalessa, Cofordix, and Lelequeen
# PS: un 20/20 serait le bienvenu :)
kversion = '1.4.2'


import pygame, os, random, time, math, ctypes, csv, platform

# init
os.system('cls')
# (ctrl + k to clear vscode term)
pygame.init()
pygame.mixer.init()
print(f"Korby Dev {kversion}")
print(f"Python {platform.python_version()}")

# load
korby_rframes = [ pygame.image.load("assets/1000/korby_r1.png"), pygame.image.load("assets/1000/korby_r2.png"), pygame.image.load("assets/1000/korby_r3.png"), pygame.image.load("assets/1000/korby_r4.png"), pygame.image.load("assets/1000/korby_r5.png"), pygame.image.load("assets/1000/korby_r6.png"), pygame.image.load("assets/1000/korby_r7.png"), pygame.image.load("assets/1000/korby_r8.png") ]
korby_lframes = [ pygame.image.load("assets/1000/korby_l1.png"), pygame.image.load("assets/1000/korby_l2.png"), pygame.image.load("assets/1000/korby_l3.png"), pygame.image.load("assets/1000/korby_l4.png"), pygame.image.load("assets/1000/korby_l5.png"), pygame.image.load("assets/1000/korby_l6.png"), pygame.image.load("assets/1000/korby_l7.png"), pygame.image.load("assets/1000/korby_l8.png") ]
korby_i = pygame.image.load("assets/1000/korby_i.png")
korby_j = pygame.image.load("assets/1000/korby_j.png")
korby_f = pygame.image.load("assets/1000/korby_f.png")
korby_fl = pygame.image.load("assets/1000/korby_fl.png")
korby_fr = pygame.image.load("assets/1000/korby_fr.png")
korby_ico = pygame.image.load("assets/1000/korby_ico.png")
bg = pygame.image.load("assets/1000/bg.png")
lvl1 = pygame.image.load("assets/1000/lvl1.png")
# mouse = pygame.image.load("assets/1000/cursor.png")
pygame.mixer.music.load('assets/korby_8bit.wav')



# vars definition
user32 = ctypes.windll.user32
screensize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
print('Screen Resolution ',screensize)
print("Note that screens with low resolution or high scaling are not supported")
xd = 0
yk = 550
xk = 0
floor = 550
xd = 0
xm = 0
ym = 0
mousedwn = False
pas = 60
jpas = 40
# import csv kbctrl
jump=False
flight=False
ckorby=korby_i 
kccsv = open('kbctrl.csv', 'w', encoding='UTF8')
kpressed = pygame.key.get_pressed()
clock= pygame.time.Clock()
fps = 30
frame = 0
pause = True

korby_mask = pygame.mask.from_surface(ckorby)
level_mask = pygame.mask.from_surface(lvl1)


# functions definition
def korby_r_a(): 
    global frame
    if frame >= len(korby_rframes):
        frame = 0
    else :
        frame=frame
    korby_r = korby_rframes[frame]
def korby_l_a(): 
    global frame
    if frame >= len(korby_lframes):
        frame = 0
    else :
        frame=frame
    korby_l = korby_lframes[frame]

def drawscreen():
    window.blit(bg,(0,0))
    window.blit(ckorby,(xk,yk))
    window.blit(lvl1,(xd,0))
    pygame.display.update()
    clock.tick(fps)


# window properties
window = pygame.display.set_mode((1800,1000))
pygame.mouse.set_visible(0)
pygame.display.set_icon(korby_ico)
pygame.display.set_caption('SuperKorby ++ Ultra 3000 Premium Deluxe Remastered Edition Rebooted')

pygame.mixer.music.play(-1) 

# game loop
running=True
while running == True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    drawscreen()
    # window.blit(mouse,(xm,ym))
    ofstx = xd - xk
    ofsty = 0 - yk
    if korby_mask.overlap(level_mask,(ofstx,ofsty)):
        print(level_mask,(ofstx,ofsty))
        
        # detect mouse click
    if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        mousedwn=True
    if event.type==pygame.MOUSEBUTTONUP and event.button==1:
        mousedwn=False

    # curseur custom
    if event.type == pygame.MOUSEMOTION and pause == True:
        xm=event.pos[0]
        ym=event.pos[1]
    
    # keyboard controls
    if event.type==pygame.KEYDOWN:
        if event.key==pygame.K_RIGHT:
            if flight==True:
                xd-=pas/2
                yk+=jpas
                ckorby = korby_fr
            elif xk >= 700:
                frame+=1
                korby_r_a()
                xd-=pas
                ckorby=korby_rframes[frame]
            else:
                while xk<700:
                    frame+=1
                    xk+=pas
                    korby_r_a()
                    ckorby=korby_rframes[frame]
                    drawscreen()

        if event.key==pygame.K_LEFT:
            if flight==True:
                xd+=pas/2
                yk+=jpas
                ckorby = korby_fl
            else:
                if xd<0:
                    frame+=1
                    korby_l_a()
                    xd+=pas
                    ckorby=korby_lframes[frame]
                elif xk>0:
                    frame=frame+1
                    korby_l_a()
                    xk-=pas
                    ckorby=korby_lframes[frame]
                else:
                    ckorby=korby_i

        if event.key==pygame.K_UP:
            flight=True
            ckorby=korby_j
            if yk>-150:
                yk-=jpas*3.5

        if event.key==pygame.K_DOWN:
            # if yk>floor:
            yk+=pas*6

        if event.key==pygame.K_k:
            # press not detected, why ?
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
        ckorby=korby_i

    if event.type==pygame.KEYUP and flight==True:
        ckorby = korby_f
        
        if yk<floor:
            yk+=jpas*4
            drawscreen()


    if yk>=floor:
        flight=False
        yk = floor


pygame.quit()