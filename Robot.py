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
        self.rect = self.image.get_rect()
        self.rect.move_ip(INIT_LOC[0], INIT_LOC[1])  # move to initial position
        self.angle = math.pi  # angle the car facing
        # info of the map for the sensors (2D matrix)
        self.test_map = cv2.imread(MAP_IMG, cv2.IMREAD_GRAYSCALE)
        self.title = ('', '')
        # internal output
        self.sensors = (0, 0)  # left sensor and right sensor input
        self.bump_sensor = 0  # bump sensor input
        # user accessible
        self.motors = (0, 0, False)  # motor output and status

    def logic(self):
        left_dir = 0  # left dir output
        right_dir = 0  # right dir output
        motor = False  # motor status
        LOW = 0  # output LOW
        HIGH = 1  # output HIGH
        (leftSensor, rightSensor) = self.sensors
        bumpSensor = self.bump_sensor

        ##### CODE STARTS HERE #####

        if not leftSensor:
            left_dir = LOW
            right_dir = HIGH
        else:
            left_dir = HIGH
            if rightSensor:
                right_dir = HIGH
            else:
                right_dir = LOW

        motor = True

        ##### CODE ENDS HERE #####

        self.motors = (left_dir, right_dir, motor)

    def detect_track(self):
        def sample(p, q):
            # take 9x9 sample
            t = self.test_map
            tmp = 0
            for i in range(-2,3):
                for j in range(-2,3):
                    tmp += t[p+i][q+1]
            tsu = tmp / (25*255)
            return 255 if tsu > 0.5 else 0

        def shift(x):
            # as we are using greysccale, it is inverted
            return 1 if x < 100 else 0

        x = self.rect.centerx  # robot center
        y = self.rect.centery  # robot center
        l = 25  # sensor off set
        a = math.pi/4  # off-set angle
        right_sensor = (int(x + l*math.cos((3*math.pi/2)+a-self.angle)),
                       int(y + l*math.sin((3*math.pi/2)+a-self.angle)))
        left_sensor = (int(x + l*math.cos((3*math.pi/2)-a-self.angle)),
                        int(y + l*math.sin((3*math.pi/2)-a-self.angle)))
        ls = shift(sample(left_sensor[1], left_sensor[0]))
        rs = shift(sample(right_sensor[1], right_sensor[0]))
        self.title = (f'Center: {(x,y)} Dir: {int(360*self.angle/(2*math.pi))} L: {left_sensor} R: {right_sensor}',
                      f'L_Sensor: {ls}  R_Sensor: {rs}')
        self.sensors = (ls, rs)

    def move(self):
        (l, r, s) = self.motors
        m = (l, r)
        v = 4  # velocity
        (vy, vx) = (v*math.cos(self.angle), v*math.sin(self.angle))
        if not s:
            return
        if m == (1, 1):
            self.rect.move_ip(-vx, -vy)
        elif m == (0, 0):
            self.rect.move_ip(vx, vy)
        elif m == (1, 0):
            self.angle -= math.pi/96
        elif m == (0, 1):
            self.angle += math.pi/96

    def update(self, k):
        self.detect_track()
        self.logic()
        self.move()
