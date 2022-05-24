# KORBY  by LastMeridian_, Ordnalessa, Cofordix, and Lelequeen
# PS: un 20/20 serait le bienvenu :)
kversion = '1.6'


import os, time, ctypes, platform, pygame
from random import randint
from pygame import *

# init
os.system('cls')
#i (ctrl + k to clear vscode term)
init()
mixer.init()
print(f"Korby Beta {kversion} -- Tramunthan Edition")
print(f"Python {platform.python_version()}")

# load
korby_rframes = [ image.load("assets/images/korby_r1.png"), image.load("assets/images/korby_r2.png"), image.load("assets/images/korby_r3.png"), image.load("assets/images/korby_r4.png"), image.load("assets/images/korby_r5.png"), image.load("assets/images/korby_r6.png"), image.load("assets/images/korby_r7.png"), image.load("assets/images/korby_r8.png") ]
korby_i = image.load("assets/images/korby_i.png")
korby_j = image.load("assets/images/korby_j.png")
korby_f = image.load("assets/images/korby_fr.png")
korby_ico = image.load("assets/images/korby_ico.png")
dino_frames = [ image.load("assets/images/dino_1.png"), image.load("assets/images/dino_2.png") ]
dino = image.load("assets/images/dino_1.png") # HAN-RIZ
dino2 = image.load("assets/images/dino_1.png") # veloceraptor
dino3 = image.load("assets/images/dino_1.png") # gourmy
dino4 = image.load("assets/images/dino_1.png") # pterodactyle
bg = image.load("assets/images/bg.png")
fg = image.load("assets/images/fg.png")
pauseimg = image.load("assets/images/korby_i.png")
mixer.music.load('assets/korby_metal.wav')


# vars definition
user32 = ctypes.windll.user32
screensize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
print('Screen Resolution ',screensize)
print("Note that screens with low resolution or high scaling are not supported")

yfg = 591
xfg = 0
xfg2 = -1800
xdino = 0
xdino2 = -500
xdino4 = -600
xk = 800
yk = 600
floor = 600
floor = 591
ydino = floor-30
ydino4 = 400
pas = 60
jump = 80
inair=False
frame = 0
framed = 0
ckorby=korby_rframes[frame]
health = 30
killedby = "VOID"
#d kccsv = open('kbctrl.csv', 'w', encoding='UTF8')
kpressed = key.get_pressed()
clock= time.Clock()
fps = 30
pause = True
airtimer = 0
safetimer = 0
dangersaid  = False
gourmy = False
shift = False

korby_mask = mask.from_surface(ckorby)
dino_mask = mask.from_surface(dino)
dino2_mask = mask.from_surface(dino2)
dino4_mask = mask.from_surface(dino4)


# functions definition
def korby_r_a(): 
    global frame
    if frame >= len(korby_rframes):
        frame = 0
    else :
        korby_r = korby_rframes[frame]

def dino_a():
    global framed
    if framed >= len(dino_frames):
        framed = 0
    else :
        dino = dino_frames[framed]

def drawscreen():
    window.blit(bg,(0,0))
    window.blit(fg,(xfg,yfg))
    window.blit(fg,(xfg2,yfg))
    window.blit(ckorby,(xk,yk))
    window.blit(dino,(xdino,ydino))
    window.blit(dino2,(xdino2,ydino))
    window.blit(dino4,(xdino4,ydino4))
    display.update()
    clock.tick(fps)


# window properties
window = display.set_mode((1800,1000))
mouse.set_visible(0)
display.set_icon(korby_ico)
display.set_caption('SuperKorby ++ Ultra 3000 Premium Deluxe Remastered Edition Tramunthan Rebooted')

mixer.music.play(-1) 

# game loop
running=True
while running == True:

    drawscreen()

    # anim
    frame+=1
    framed+=1
    korby_r_a()
    #d dino_a()        -- doesn't work

    # bg move
    xfg2 -= 15
    xfg -= 15
    if xfg < -1800:
        xfg = 1700
    if xfg2 < -1800:
        xfg2 = 1700

    # dino move
    if dangersaid==True:
        xdino -= 15
        xdino2 -= 22
        xdino4 -= 30
        if xdino < -320:
            xdino = randint(1800,2400)
        if xdino2 < -320:
            xdino2 = randint(1800,2000)
        # if xdino3 < -320:
        #     xdino3 = randint(1800,2300)
        if xdino4 < -320:
            xdino4 = randint(1800,3000)
            ydino4 = randint(0,500)

    # collisions
    if korby_mask.overlap(dino_mask,(xdino - xk,ydino - yk)):
        #d print(dino_mask,(xfg - xk,0 - yk))
        print('Korby got pinched by the naughty Han-Riz :(     Game Over')
        running=False
    if korby_mask.overlap(dino2_mask,(xdino2 - xk,ydino - yk)):
        health -= 1
        killedby = "Cristobal"
    if korby_mask.overlap(dino4_mask,(xdino4 - xk,ydino4 - yk)):
        health -= 1
        killedby = "El Pterodactyl"
    
    for event in pygame.event.get():
        if event.type==QUIT:
            running=False

    # keyboard controls
    if event.type==KEYDOWN:

        if event.key==K_UP or event.key==K_SPACE:
            inair=True
            ckorby=korby_j
            if yk>0 and inair < 30:
                yk-=jump
            else:
                while yk>floor:
                    yk+=jump

        if event.key==K_DOWN:
            if inair == True:
                yk+=jump*4
            else:
                yk = floor + 70
                shift = True

        if event.key==K_ESCAPE:
            running=False
            quit()

        # pause
        if event.key==K_LEFT or event.key == K_p:
            pause = True
            while pause == True:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE or event.key == K_p:
                            pause = False
                        elif event.key == K_ESCAPE:
                            quit()
                        


    if event.type==KEYUP and inair:
        ckorby = korby_f
        if yk<floor:
            yk+=jump
        if yk>=floor:
            inair=False
            yk = floor
    if event.type==KEYUP and shift:
        yk = floor
        shift=False

    if inair == False:
        ckorby=korby_rframes[frame]
        if yk>=floor and shift == False:
            yk = floor

    # safetimer
    safetimer +=1
    if safetimer >= 60:
        if dangersaid==False:
            print("danger")
            dangersaid=True
    if safetimer >= 180:
        if gourmy==False:
            print('Caution, Gourmy is comming')
            gourmy = True
    else:
        print("Game will start in : ",round(1/safetimer*100))

    # Health
    if health<=0:
        print(f'Korby got pinched by the naughty {killedby} :(     Game Over')
        running=False



quit()