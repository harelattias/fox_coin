import pgzrun
import pygame

WIDTH = 400
HEIGHT = 400
score = 0
game_over = False

fox = Actor("fox")
fox.pos = 100, 100

coin = Actor("fox")
coin.pos = 200, 200

def draw():
    screen.fill("green")
    fox.draw()

pgzrun.go()
