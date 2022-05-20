# KORBY  by LastMeridian_, Ordnalessa, Cofordix, and Lelequeen
# PS: un 20/20 serait le bienvenu :)
kversion = '1.5.2'


import os, time, ctypes, platform, pygame
from pygame import *

# init
os.system('cls')
#i (ctrl + k to clear vscode term)
init()
mixer.init()
print(f"Korby Dev {kversion} -- Tramunthan Edition")
print(f"Python {platform.python_version()}")

# load
korby_rframes = [ image.load("assets/bw/korby_r1.png"), image.load("assets/bw/korby_r2.png"), image.load("assets/bw/korby_r3.png"), image.load("assets/bw/korby_r4.png"), image.load("assets/bw/korby_r5.png"), image.load("assets/bw/korby_r6.png"), image.load("assets/bw/korby_r7.png"), image.load("assets/bw/korby_r8.png") ]
korby_i = image.load("assets/bw/korby_i.png")
korby_j = image.load("assets/bw/korby_j.png")
korby_f = image.load("assets/bw/korby_fr.png")
korby_ico = image.load("assets/bw/korby_ico.png")
bg = image.load("assets/bw/bg.png")
fg = image.load("assets/bw/fg.png")
fg_rect = fg.get_rect()
mixer.music.load('assets/korby_metal.wav')


# vars definition
user32 = ctypes.windll.user32
screensize = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]
print('Screen Resolution ',screensize)
print("Note that screens with low resolution or high scaling are not supported")

yfg = 591
xfg = 0
xfg2 = -1800
xk = 800
yk = 550
floor = 550
pas = 60
jump = 80
inair=False
frame = 0
ckorby=korby_rframes[frame]
#d kccsv = open('kbctrl.csv', 'w', encoding='UTF8')
kpressed = key.get_pressed()
clock= time.Clock()
fps = 30
pause = True
airtimer = 0
safetimer = 60
dangersaid  = False

korby_mask = mask.from_surface(ckorby)
crab_mask = ""#mask.from_surface(lvl1)


# functions definition
def korby_r_a(): 
    global frame
    if frame >= len(korby_rframes):
        frame = 0
    else :
        frame=frame
    korby_r = korby_rframes[frame]

def drawscreen():
    window.blit(bg,(0,0))
    # window.blit(fg,fg_rect)
    window.blit(fg,(xfg,yfg))
    window.blit(fg,(xfg2,yfg))
    window.blit(ckorby,(xk,yk))
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
    korby_r_a()

    # bg move
    xfg2 -= 15
    xfg -= 15
    if xfg < -1800:
        xfg = 1800
    if xfg2 < -1800:
        xfg2 = 1800

    #d collisions
    # ofstx = xfg - xk
    # ofsty = 0 - yk
    # if korby_mask.overlap(crab_mask,(ofstx,ofsty)):
    #     print(crab_mask,(ofstx,ofsty))
    #     print('Korby got pinched by craby : Game Over')
    
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
            yk+=jump

        if event.key==K_ESCAPE:
            running=False
            quit()


    if inair == False:
        ckorby=korby_rframes[frame]
        if yk>=floor:
            yk = floor

    if event.type==KEYUP and inair==True:
        ckorby = korby_f
        if yk<floor:
            yk+=jump*4
        if yk>=floor:
            inair=False
            yk = floor

    # safetimer
    if safetimer <= 0:
        if dangersaid == True:
            continue
        else:
            print("danger")
            dangersaid=True
    else:
        safetimer -=1
        print("Safetimer : ",safetimer)

quit()