from pico2d import *


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.y = 30
    def update(self):
        pass

    def draw(self):
        self.image.draw(400, self.y)
        self.image.draw(1200, self.y)
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 0, 0, 1600 - 1, 50

