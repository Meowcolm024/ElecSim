# Copyright (c) 2020 Malcolm Law
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import pygame
from pygame.sprite import Sprite
import config


class Robot(Sprite):
    def __init__(self):
        super(Robot, self).__init__()
        self.image = pygame.Surface([100, 80])  # ? robot size
        self.image.fill((255,255,255))          # color: white
        self.rect = (100, 180)                  # ? initialize the location of the robot
        self.test_map = [[]]                    # ? info of the map for the sensors (2D matrix)
        self.sensors = (0, 0)                   # left sensor and right sensor input
        self.bump_sensor = 0                    # bump sensor input
        self.motors = (0, 0)                    # motor output

    def logic(self):
        self.motors = config.logic(self.sensors, self.bump_sensor)
    
    def detect_track(self):
        x = self.rect.centerx               # robot center
        y = self.rect.centery               # robot center
        left_sensor = (x - 10, y - 10)      # ? sample loc of left sensor
        right_sensor = (x + 10, y - 10)     # ? sample loc of right sensor
        self.sensors = (                    # ! not decided 0,1 or 1,0
            self.test_map[left_sensor[0]][left_sensor[1]],
            self.test_map[right_sensor[0]][right_sensor[1]]
        )

    def move(self):
        m = self.motors
        if m == (1, 1):
            pass
        if m == (0, 0):
            pass
        if m == (1, 0):
            pass
        if m == (0, 1):
            pass

    def update(self):
        self.detect_track()
        self.logic()
        self.move()
