import pgzrun
import pygame
from random import randint

WIDTH = 600
HEIGHT = 600
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("coin")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()
    coin.draw()
    screen.draw.text(str(score) + " $", color="black", topleft=(10, 10))

    if game_over:
        screen.fill("pink")
        screen.draw.text("total: " + str(score), topleft=(HEIGHT/3.3, WIDTH/2.2), fontsize=60)

def place_coin():
    coin.x = randint(20, (WIDTH - 20))
    coin.y = randint(20, (HEIGHT - 20))

def time_up():
    global game_over
    game_over = True

def update():
    global score
    if keyboard.left:
        fox.x = fox.x - 2
    if keyboard.up:
        fox.y = fox.y - 2
    if keyboard.down:
        fox.y = fox.y + 2
    if keyboard.right:
        fox.x = fox.x + 2

    coin_collected = fox.colliderect(coin)

    if coin_collected:
        score = score + 30
        place_coin()

clock.schedule(time_up, 10.0)
place_coin()

pgzrun.go()
