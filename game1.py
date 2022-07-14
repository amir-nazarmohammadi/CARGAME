import pygame
import time
import random

pygame.init()

crash_sound = pygame.mixer.Sound("lose-m.wav")
pygame.mixer.music.load("world-m.ogg")
icon = pygame.image.load('car2.png')
pygame.display.set_icon(icon)
background = pygame.image.load("back.jpg")

width = 800
height = 600


game_display= pygame.display.set_mode((width , height))

pygame.display.set_caption("Car Rice")

Clock = pygame.time.Clock()

carimg = pygame.image.load("car.png")

x = (width * 0.45)
y = (height * 0.8)
x_change = 0
car_width = 80


black = (0,0,0)
white= (255,255,255)
red = (200,0,0)
red1 = (255,0,0)
orang = (239,116,0)
purple = (184,116,242)
green = (0,200,0)
green1 = (0,255,0)
blue = (68,140,251)

color_random = ["r","b","w","o","g","p"]
choice = random.choice(color_random)
if choice == "r":
    color1 = (200,0,0)
if choice == "b":
    color1 = (68,140,251)
if choice == "w":
    color1 = (255,255,255)
if choice ==  "o":
    color1 = (239,116,0)
if choice == "g":
    color1 =  (0,200,0)
if choice == "p":
    color1 = (184,116,242)
            
def button(msg,x,y,w,h,ic,ac,action=None):
    mous = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mous[0] > x and y + h > mous[1] > y:
        pygame.draw.rect(game_display,ac,(x,y,w,h))
        if click[0] == 1 and action != None:
            if action == "Play":
                game_loop()
            elif action == "Quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(game_display,ic,(x,y,w,h))

    if 550 + w > mous[0] > 550 and y + h > mous[1] > y:
        pygame.draw.rect(game_display,ac,(550,y,w,50))
    else:
        pygame.draw.rect(game_display,ic,(550,y,w,h))

    smalltext = pygame.font.Font("freesansbold.ttf",20)
    textsurf , textrect = text_objects(msg,smalltext)
    textrect.center = ((x+(w/2)), (y+(h/2)))
    game_display.blit(textsurf,textrect)

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_display.fill(orang)
        largetext = pygame.font.Font("freesansbold.ttf",90)
        textsurf , textrect = text_objects("let's play game",largetext)
        textrect.center = (( width/2 ),( height/2 ))
        game_display.blit(textsurf,textrect)
        button("Play!",150,450,100,50,green,green1,"Play")
        button("Quit!",550,450,100,50,red,red1,"Quit")
        pygame.display.update()

def stuff_score(count):
    font = pygame.font.SysFont(None , 25)
    text = font.render("score: "+str(count), True , orang)
    game_display.blit(text ,(10,10))


def stuff(stuffx,stuffy,stuffw,stuffh,color):
    pygame.draw.rect(game_display,color,[stuffx , stuffy , stuffw , stuffh])
    


def car(x,y):
    game_display.blit(carimg,(x,y))

def text_objects(text,font):
    textsurface = font.render(text , True , black)
    return textsurface, textsurface.get_rect()

def messamge_display(text):
    largetext = pygame.font.Font("freesansbold.ttf",85)
    textsurf , textrect = text_objects(text,largetext)
    textrect.center = (( width/2 ),( height/2 ))
    game_display.blit(textsurf,textrect)
    pygame.display.update()

    time.sleep(2)
    game_loop()

def crash():
    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_sound)

    largetext = pygame.font.Font("freesansbold.ttf",85)
    textsurf , textrect = text_objects("You crashed",largetext)
    textrect.center = (( width/2 ),( height/2 ))
    game_display.blit(textsurf,textrect)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Try again",150,450,100,50,green,green1,"Play")
        button("Quit!",550,450,100,50,red,red1,"Quit")
        pygame.display.update()

def game_loop():
    pygame.mixer.music.play(-1)
    x = (width * 0.45)
    y = (height * 0.8)
    x_change = 0

    stuff_startx = random.randrange(0,width)
    stuff_starty = -600
    stuff_speed = 7
    stuff_width = 100
    stuff_height = 100
    score = 0

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        #game_display.fill(white)
        game_display.blit(background,[0,0])
        

        #stuffx,stuffy,stuffw,stuffh,color
        stuff(stuff_startx, stuff_starty, stuff_width, stuff_height,color1)
        stuff_starty += stuff_speed

        car(x,y)
        stuff_score(score)

        if x > width - car_width or x < 0:
            crash()
        if stuff_starty > height:
            stuff_starty = 0 - stuff_height
            stuff_startx = random.randrange(0,height)
            score += 1
            if (score % 5 ==0):
                stuff_speed +=1
                stuff_width +=10
                stuff_height +=10
                
            
        if y < stuff_starty + stuff_height:
            if x > stuff_startx and x < stuff_startx + stuff_width or x + car_width > stuff_startx and x + car_width < stuff_startx + stuff_width:
                crash()

        pygame.display.update()
        Clock.tick(60)
game_intro()        
game_loop()
pygame.quit()
quit() 