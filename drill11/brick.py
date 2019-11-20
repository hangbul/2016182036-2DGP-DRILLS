from pico2d import *


class Brick:
    def __init__(self):
        self.image = load_image('brick180x40.png')
        self.x, self.y = 600, 200
        self.dir = 3

    def update(self):
        self.x += self.dir
        if self.x > 1600 - 1:
            self.dir *= -1
        elif self.x - 90< 0:
            self.dir *= -1

    def draw(self):
        self.image.draw(self.x, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 90, self.y - 20, self.x + 90, self.y + 20

