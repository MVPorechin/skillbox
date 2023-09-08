import time

from pygame import *

init() """ Инициализация модуля"""
display.set_caption('MyGame')
BLACK = (0, 0, 0)
window = display.set_mode((700,500)) """задаем размер окна"""
window.fill(BLACK)
clock = time.Clock()

run = True
window.blit(path_to_background, (0,0))
while run:
    time.delay(50)
    for _ in event.get():
        if _.type == QUIT:
            run = False
    display.update()