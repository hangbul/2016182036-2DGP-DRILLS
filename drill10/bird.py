import game_framework
from pico2d import *
from ball import Ball

import game_world

# 1 pixel : 3cm
# bird_size : 94pixel * 95 pixel = 282cm * 285cm
# bird_speed : 0.25km/h = 0.0695m/s

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 0.25
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class IdleState:

    @staticmethod
    def enter(bird, event):
        pass

    @staticmethod
    def exit(bird, event):
        pass

    @staticmethod
    def do(bird):
        bird.frame = (bird.frame + 1) % 21
        bird.x += bird.velocity * game_framework.frame_time
        bird.x = clamp(25, bird.x, 1600 - 25)
        if bird.x >= 1600 - 700:
            bird.dir = -1
        elif bird.x <= 0 + 700:
            bird.dir = 1

    @staticmethod
    def draw(bird):
        if bird.dir == 1:
            bird.image.clip_draw(int(bird.frame) * 94, 95, 94, 95, bird.x, bird.y)
        else:
            bird.image.clip_draw(int(bird.frame) * 94, 0, 94, 95, bird.x, bird.y)


class Bird:

    def __init__(self):
        self.x, self.y = 1600 // 2, 360
        self.image = load_image('bird_animation.png')
        self.font = load_font('ENCR10B.TTF', 16)
        self.dir = 1
        self.velocity = 0
        self.frame = 0
        self.event_que = []
        self.cur_state = IdleState
        self.cur_state.enter(self, None)

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state.enter(self, event)
        if self.dir == 1:
            self.velocity += RUN_SPEED_PPS
        elif self.dir == -1:
            self.velocity -= RUN_SPEED_PPS

    def draw(self):
        self.cur_state.draw(self)
        self.font.draw(self.x - 60, self.y + 50, '(Time: %3.2f)' % get_time(), (255, 255, 0))
