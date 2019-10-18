from pico2d import *
from random import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def character_stat(p1, p2):
    if (p1.x < p2.x):
        dir = 1
    elif (p1.x > p2.x):
        dir = -1
    if (p1.y < p2.y):
        dir_ud = 1
    elif (p1.y > p2.y):
        dir_ud = -1

    pass

def character_now(dir, dir_ud):
    global frame_x, frame_y, dir_bfor

    if (dir == -1):
        frame_y = 0
        dir_bfor = -1
    elif (dir == 1):
        frame_y = 1
        dir_bfor = 1

    if (dir_ud != 0):
        if (dir_bfor == -1):
            frame_y = 0
        elif (dir_bfor == 1):
            frame_y = 1
    elif (dir == 0):
        if (dir_bfor == 1):
            frame_y = 3
        elif (dir_bfor == -1):
            frame_y = 2

    pass

def character_move(p1, p2, p3, p4, i):
    global x, y


    # draw p1-p2

    if(i<3000):
        t = i / 3000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2

    # draw p2-p3

    elif(i>=3000 and i<6000):
        t = (i - 3000)/ 3000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2


    # draw p3-p4

    elif(i>=6000 and i<9000):
        t = (i - 6000)/ 3000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2


    # draw p4-p1
    else:
        t = (i - 9000) / 3000
        x = ((-t ** 3 + 2 * t ** 2 - t) * p3[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p1[0] + (t ** 3 - t ** 2) * p2[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p3[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p4[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p1[1] + (t ** 3 - t ** 2) * p2[1]) / 2

    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
to_x, to_y = 0, 0
bfo_x, bfo_y=0,0

point = [(randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1)), (randint(0,KPU_WIDTH+1), randint(0,KPU_HEIGHT+1))]

t, i=0, 0
a=0
frame_x = 0
frame_y = 1

dir = 0
dir_ud = 0
dir_bfor = 1

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)

    #character_now(dir, dir_ud)


    character_move(point[a], point[a+1], point[a+2], point[a+3], i)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)

    update_canvas()

    frame_x = (frame_x + 1) % 8
    i+=1
    if i==12000:
        i=0
        dir = 0
        dir_ud = 0

    #delay(0.01)

close_canvas()

