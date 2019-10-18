from pico2d import *
import  random


# Game object class here
class Small_ball:
    def __init__(self):
        self.image = load_image('ball21x21.png')
        self.x, self.y = random.randint(0, 600),599
        self.down = random.randint(10, 50)

    def draw(self):
        self.image.clip_draw(0,0,21,21, self.x, self.y)
        self.y -= self.down


class Big_ball:
    def __init__(self):
        self.image = load_image('ball41x41.png')
        self.x, self.y = random.randint(0, 600), 599
        self.down = random.randint(10, 50)

    def draw(self):
        self.image.clip_draw(0,0,41,41, self.x, self.y)
        self.y -= self.down


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100, 700), 90
        self.frame = random.randint(0, 7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1 ) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame*100, 0, 100, 100,self.x, self.y)

open_canvas()

running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
team = [Boy() for i in range(11)]
grass = Grass()

balls = random.randint(0, 20)

big_balls = [Big_ball() for i in range(0, balls)]
small_balls = [Small_ball() for i in range(0, 20-balls)]

# game main loop code
while running:
    handle_events()


    for boy in team:
        boy.update()

    clear_canvas()
    grass.draw()

    for big_ball in big_balls:
        big_ball.draw()

    for small_ball in small_balls:
        small_ball.draw()

    for boy in team:
        boy.draw()


    update_canvas()

    delay(0.05)

# finalization code
close_canvas()