import random
import math
import game_framework
from pico2d import *
import main_state


class SmallBall:
    images = None

    def load_image(self):
        SmallBall.image = load_image("ball21x21.png")

    def __init__(self):
        self.x, self.y = random.randint(0, 1280), random.randint(0, 1024)
        self.load_image()
        self.hp = 50
        self.size = 21

    def get_bb(self):
        return self.x - 11, self.y - 11, self.x + 11, self.y + 11

    def draw(self):
        SmallBall.image.draw(self.x, self.y, 21, 21)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def update(self):
        pass

class BigBall:
    images = None

    def load_image(self):
        BigBall.image = load_image("ball41x41.png")

    def __init__(self):
        self.x, self.y = random.randint(0, 1280), random.randint(0, 1024)
        self.load_image()
        self.hp = 100
        self.size = 41

    def get_bb(self):
        return self.x - 21, self.y - 21, self.x + 21, self.y + 21

    def draw(self):
        BigBall.image.draw(self.x, self.y, 41, 41)
        draw_rectangle(*self.get_bb())

    def handle_event(self, event):
        pass

    def update(self):
        pass
