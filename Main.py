# Copyright (c) 2020 Malcolm Law
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import math
import pygame
from pygame.locals import *
from Robot import Robot

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ElecSim')
clock = pygame.time.Clock()

background = pygame.image.load('assets/testc.png')

all_sprites = pygame.sprite.Group()
robot = Robot()
all_sprites.add(robot)

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

    screen.blit(background, (0, 0))
    for entity in all_sprites:
        rot = pygame.transform.rotate(entity.image, 360*entity.angle/(2*math.pi))
        screen.blit(rot, entity.rect)
    
    pygame.display.update()
    clock.tick(60)
