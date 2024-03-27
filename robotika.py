import pgzrun
import pygame
import sys
from random import randint
WIDTH = 500
HEIGHT = 400



fix_hitbox = 0
score = 0
fix = 0
y = 0
g = 0.5

apple = Actor("apple")
coin = Actor("coin")
back = Actor("back.jfif")
back.right = WIDTH
def draw():
    

    screen.clear()
    
    
    apple.draw()
    coin.draw()
    back.draw()

    screen.draw.text("Hej tvoje skóre je: " + str(score), color="white", topleft=(10, 10))


def place_all():

    apple.pos = 50, 0
    place_all()


def place_coin():
    
    coin.x = randint(50, 450)
    coin.y = randint(50, 350)

    if coin.colliderect(apple):
        place_coin

    
        
        


place_coin()

music.play("underclocked")
def update():
    global fix_hitbox
    global y
    global score
    global fix
    global g

    if keyboard.up:
        if keyboard.right:
            if keyboard.left:
                if keyboard.p:
                    score += 100

    
    y = y + 0.5

    apple.y = apple.y + y



    if keyboard.right:
        apple.x = apple.x + 6

    if keyboard.left:
        apple.x = apple.x - 6

    if apple.x > 450:
        apple.x = 450

    if apple.x < 50:
        apple.x = 50
        

    touch_coin = apple.colliderect(coin)

    if touch_coin:
        fix_hitbox += 1
        if fix_hitbox > 5:
            place_coin()
            score += 5
            fix_hitbox = 0
    if not touch_coin:
        fix_hitbox = 0

        
      

        

    if apple.y > 350:
        apple.y = 350
        y = 0
        fix = 0


    if keyboard.up:
        if fix < 3:
            fix = fix + 1
            if g == 0.5:
                y = -10

            else:
                y = 10
    if not keyboard.up:
        fix = 0
    
    if apple.y < 50:
        apple.y = 50
        y = 0
        

    






pgzrun.go()
