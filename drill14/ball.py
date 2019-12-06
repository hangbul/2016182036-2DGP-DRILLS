import random
from pico2d import *
import game_world
import game_framework
from background import FixedBackground as fx
class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(400, 1400 - 1), random.randint(300, 800 - 1)
        self.canvas_width = get_canvas_width()
        self.canvas_height = get_canvas_height()

    def get_bb(self):
        return -10 - self.window_left  + self.x, -10 - self.window_bottom + self.y, 11 - self.window_left  + self.x, 11 - self.window_bottom + self.y

    def set_center_object(self, boy):
        self.center_object = boy


    def draw(self):
        self.image.draw(0 - self.window_left  + self.x, 0 - self.window_bottom + self.y)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.window_left = clamp(0, int(self.center_object.x)-self.canvas_width//2, 1830-self.canvas_width)
        self.window_bottom = clamp(0, int(self.center_object.y)-self.canvas_height//2, 1100 -self.canvas_height)

