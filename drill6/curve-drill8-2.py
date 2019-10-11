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

def character_move(p1, p2, p3, p4, t):
    global x, y

    # draw p1-p2
    if(t>=0 and t<200):
        x = ((-t ** 3 + 2 * t ** 2 - t) * p4[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[0] + (t ** 3 - t ** 2) * p3[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p4[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p1[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p2[1] + (t ** 3 - t ** 2) * p3[1]) / 2


    # draw p2-p3

    elif(t>=200 and t<400):
        x = ((-t ** 3 + 2 * t ** 2 - t) * p1[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[0] + (t ** 3 - t ** 2) * p4[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p1[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p2[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p3[1] + (t ** 3 - t ** 2) * p4[1]) / 2


    # draw p3-p4

    elif(t>=400 and t<600):
        x = ((-t ** 3 + 2 * t ** 2 - t) * p2[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[0] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[0] + (t ** 3 - t ** 2) * p1[0]) / 2
        y = ((-t ** 3 + 2 * t ** 2 - t) * p2[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * p3[1] + (-3 * t ** 3 + 4 * t ** 2 + t) * p4[1] + (t ** 3 - t ** 2) * p1[1]) / 2


    # draw p4-p1

    elif (t >= 600 and t < 800):
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

point=[(random()%KPU_WIDTH+1,random()%KPU_HEIGHT+1), (random()%KPU_WIDTH+1,random()%KPU_HEIGHT+1), (random()%KPU_WIDTH+1,random()%KPU_HEIGHT+1), (random()%KPU_WIDTH+1,random()%KPU_HEIGHT+1)]
t, i=0, 0

frame_x = 0
frame_y = 1

dir = 0
dir_ud = 0
dir_bfor = 1

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)


    #character_now(dir, dir_ud)
    t=i/800
    character_move((100,100),(200,200),(500, 500),(1000, 1000), t)

    update_canvas()

    frame_x = (frame_x + 1) % 8
    i+=1
    if i==800:
        i=0
        dir = 0
        dir_ud = 0
    #delay(0.01)

close_canvas()

