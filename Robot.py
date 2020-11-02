# Copyright (c) 2020 Malcolm Law
# 
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

import math
import pygame
from pygame.sprite import Sprite
from pygame.locals import K_SPACE
from config import *
import cv2
import numpy as np


class Robot(Sprite):
    def __init__(self):
        super(Robot, self).__init__()
        self.image = pygame.image.load(ROBOT_IMG).convert_alpha()
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()       # ? initialize the location of the robot
        self.rect.move_ip(INIT_LOC[0], INIT_LOC[1])
        self.angle = math.pi                    # angle the car facing
        self.test_map = cv2.imread(MAP_IMG, cv2.IMREAD_GRAYSCALE)  # info of the map for the sensors (2D matrix)
        self.title = ('', '')
        # internal output
        self.sensors = (0, 0)                   # left sensor and right sensor input
        self.bump_sensor = 0                    # bump sensor input
        # user accessible
        self.motors = (0, 0, False)             # motor output and status

    def logic(self):
        left_dir = 0    # left dir output
        right_dir = 0   # right dir output
        motor = False   # motor status
        LOW = 0
        HIGH = 1

        (leftSensor, rightSensor) = self.sensors
        motor = self.bump_sensor

        if not leftSensor:
            left_dir = LOW
            right_dir = HIGH
        else:
            left_dir = HIGH
            if rightSensor:
                right_dir = HIGH
            else:
                right_dir = LOW

        # left_dir = leftSensor//255
        # right_dir = rightSensor//255

        motor = True
        
        self.motors = (left_dir, right_dir, motor)
    
    def detect_track(self):
        def shift(x):
            return 255 if x == 0 else 0

        x = self.rect.centerx               # robot center
        y = self.rect.centery               # robot center
        l = 20
        a = math.pi/2.1
        left_sensor = (int(x + l*math.sin(a+self.angle)), int(y + l*math.cos(a+self.angle)))   # !!!
        right_sensor = (int(x + l*math.sin(-a+self.angle)), int(y + l*math.cos(-a+self.angle)))  # !!!
        ls = shift(self.test_map[left_sensor[1]][left_sensor[0]])
        rs = shift(self.test_map[right_sensor[1]][right_sensor[0]])
        self.title = (f'Center: {(x,y)} Dir: {int(360*self.angle/(2*math.pi))} L: {left_sensor} R: {right_sensor}',
            f'L_Sensor: {ls}  R_Sensor: {rs}')   
        self.sensors = (ls, rs)

    def move(self):        
        (l, r, s) = self.motors
        m = (l, r)
        v = 3
        (vy, vx) = (v*math.cos(self.angle), v*math.sin(self.angle))
        if not s:
            return
        if m == (1, 1):
            self.rect.move_ip(-vx, -vy)
        elif m == (0, 0):
            self.rect.move_ip(vx, vy)
        elif m == (1, 0):
            self.angle += math.pi/10
        elif m == (0, 1):
            self.angle -= math.pi/10

    def update(self, k):
        self.detect_track()
        self.logic()

        # if k[K_w]:
        #     self.motors = (1, 1, True)
        # elif k[K_s]:
        #     self.motors = (0 ,0, True)
        # elif k[K_a]:
        #     self.motors = (1, 0, True)
        # elif k[K_d]:
        #     self.motors = (0, 1, True)
        # else:
        #     self.motors = (0, 0, False)
        
        self.move()
