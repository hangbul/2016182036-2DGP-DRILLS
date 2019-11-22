import random
import json
import os

from pico2d import *
import game_framework
import game_world

from boy import Boy
from ground import Ground
from zombie import Zombie
from ball import SmallBall, BigBall

name = "MainState"

boy = None
zombie = None
balls = []


def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True


def get_boy():
    return boy


def get_balls():
    return balls


def enter():
    global boy
    boy = Boy()
    game_world.add_object(boy, 1)

    global balls
    balls = [BigBall() for i in range(5)] + [SmallBall() for i in range(5)]
    game_world.add_objects(balls, 1)

    global zombie
    zombie = Zombie()
    game_world.add_object(zombie, 1)

    ground = Ground()
    game_world.add_object(ground, 0)




def exit():
    game_world.clear()


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        else:
            boy.handle_event(event)


def update():
    for game_object in game_world.all_objects():
        game_object.update()

    if collide(boy, zombie):
        if zombie.Undead:
            game_world.remove_object(boy)
        else:
            game_world.remove_object(zombie)

    for ball in balls:
        if collide(ball, zombie):
            if ball.size == 21 and zombie.big_ball_count >= 5:
                game_world.remove_object(ball)
                zombie.small_ball_count += 1
            elif ball.size == 41:
                game_world.remove_object(ball)
                zombie.big_ball_count += 1

def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    update_canvas()



