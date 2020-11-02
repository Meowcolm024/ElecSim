# Copyright (c) 2020 Malcolm Law
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pygame
from pygame.locals import *
from Robot import Robot

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('ElecSim')
clock = pygame.time.Clock()

background = pygame.Surface(screen.get_size())
background.fill((0, 0, 0))

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

    robot.update()

    screen.blit(background, (0, 0))
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
    
    pygame.display.update()
    clock.tick(60)
