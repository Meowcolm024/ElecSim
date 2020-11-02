# Copyright (c) 2020 Malcolm Law
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import math
import pygame
from pygame.sprite import Sprite
from pygame.locals import K_w, K_s, K_a, K_d
import config


class Robot(Sprite):
    def __init__(self):
        super(Robot, self).__init__()
        self.image = pygame.image.load('assets/testr.png').convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()       # ? initialize the location of the robot
        self.rect.move_ip(87, 0)
        self.angle = math.pi                    # angle the car facing
        self.test_map = [[]]                    # ? info of the map for the sensors (2D matrix)
        self.sensors = (0, 0)                   # left sensor and right sensor input
        self.bump_sensor = 0                    # bump sensor input
        self.motors = (0, 0, False)             # motor output and status

    def logic(self):
        self.motors = config.logic(self.sensors, self.bump_sensor)
    
    def detect_track(self):
        x = self.rect.centerx               # robot center
        y = self.rect.centery               # robot center
        left_sensor = (x - 20, y + 10)      # ? sample loc of left sensor
        right_sensor = (x + 20, y + 10)     # ? sample loc of right sensor
        self.sensors = (                    # ! not decided 0,1 or 1,0
            self.test_map[left_sensor[0]][left_sensor[1]],
            self.test_map[right_sensor[0]][right_sensor[1]]
        )

    def move(self):        
        (l, r, s) = self.motors
        m = (l, r)
        v = 5
        (vy, vx) = (v*math.cos(self.angle), v*math.sin(self.angle))
        if not s:
            return
        if m == (1, 1):
            self.rect.move_ip(-vx, -vy)
        elif m == (0, 0):
            self.rect.move_ip(vx, vy)
        elif m == (1, 0):
            self.angle +=0.05
        elif m == (0, 1):
            self.angle -=0.05

    def update(self, k):
        # self.detect_track()
        # self.logic()
        if k[K_w]:
            self.motors = (1, 1, True)
        elif k[K_s]:
            self.motors = (0 ,0, True)
        elif k[K_a]:
            self.motors = (1, 0, True)
        elif k[K_d]:
            self.motors = (0, 1, True)
        else:
            self.motors = (0, 0, False)
        self.move()
