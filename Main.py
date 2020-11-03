# Copyright (c) 2020 Malcolm Law
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import math
import pygame
from pygame.locals import *
from Robot import Robot
from config import *

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ElecSim')
clock = pygame.time.Clock()

background = pygame.image.load(MAP_IMG)

all_sprites = pygame.sprite.Group()
robot = Robot()
all_sprites.add(robot)

txt = ''
font = pygame.font.Font('freesansbold.ttf', 20) 
text1 = font.render(txt, True, (0, 255, 0), (0, 0, 0)) 
textRect1 = text1.get_rect()
textRect1.center = (250, 40) 
text2 = font.render(txt, True, (0, 255, 0), (0, 0, 0)) 
textRect2 = text2.get_rect()
textRect2.center = (250, 70) 

running = True
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

    k = pygame.key.get_pressed()
    robot.update(k)

    text1 = font.render(robot.title[0], True, (255, 255, 255), (0, 0, 0)) 
    text2 = font.render(robot.title[1], True, (255, 255, 255), (0, 0, 0))

    screen.blit(background, (0, 0))
    screen.blit(text1, textRect1) 
    screen.blit(text2, textRect2)
    for entity in all_sprites:
        rot = pygame.transform.rotate(entity.image, 360*entity.angle/(2*math.pi))
        screen.blit(rot, entity.rect)
    
    pygame.display.update()
    clock.tick(TICK_SPEED)
