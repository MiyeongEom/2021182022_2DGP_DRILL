from pico2d import*

import game_framework
import game_world

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14


PIXEL_PER_METER = (10.0 / 0.4)
BIRD_SPEED_KPH = 30 # MH/H 새의 속도
BIRD_SPEED_MPM = BIRD_SPEED_KPH * 1000.0 / 60
BIRD_SPEED_MPS = BIRD_SPEED_MPM / 60.0
BIRD_SPEED_PPS = BIRD_SPEED_MPS * PIXEL_PER_METER

from random import randint

class Bird:
    image = None
    def __init__(self):
        self.x = randint(0, 800)
        self.y = randint(150, 500)
        self.frame = 0
        self.dir = 1
        if (Bird.image == None):
            Bird.image = load_image('bird_animation.png')

    def update(self):
        self.x += self.dir * BIRD_SPEED_PPS * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 14

        if self.x >= 770:
            self.dir = -1
        elif self.x <= 30:
            self.dir = 1

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, 338 - (int(self.frame) // 5 * 168), 183, 168, 0, '', self.x, self.y, 80, 60)
        else:
            self.image.clip_composite_draw(int(self.frame) % 5 * 183, 338 - (int(self.frame) // 5 * 168), 183, 168, 0, 'h', self.x, self.y, 80, 60)
