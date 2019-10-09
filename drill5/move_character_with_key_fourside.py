from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running, dir, dir_ud, mouse_x, mouse_y, to_x, to_y, bfo_x, bfo_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            to_x, to_y = mouse_x, mouse_y
            bfo_x, bfo_y = x, y

            if (bfo_x < to_x):
                dir = 1
            elif (bfo_x > to_x):
                dir = -1
            if (bfo_y < to_y):
                dir_ud = 1
            elif (bfo_y > to_y):
                dir_ud = -1

        if x > to_x-2 and x < to_x+2:
            dir = 0
        elif y > to_y - 2 and y < to_y + 2:
            dir_ud = 0

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

def character_move():
    global x, y, to_x,to_y,bfo_x,bfo_y, t

    if (dir != 0):
        x = (1-t)*bfo_x + t*to_x
    if (dir_ud != 0):
        y = (1-t)*bfo_y + t*to_y

    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
to_x, to_y = 0, 0
bfo_x, bfo_y=0,0

t, i=0, 0

mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2

frame_x = 0
frame_y = 1

dir = 0
dir_ud = 0
dir_bfor = 1

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw_now(mouse_x + 20, mouse_y - 30)

    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)

    draw_rectangle(to_x - 10, to_y - 10, to_x + 10, to_y + 10)
    draw_rectangle(bfo_x - 10, bfo_y - 10, bfo_x + 10, bfo_y + 10)

    character_now(dir, dir_ud)
    t=i/100
    character_move()

    update_canvas()

    handle_events()
    frame_x = (frame_x + 1) % 8
    i+=1
    if i==100:
        i=0
    #delay(0.01)

close_canvas()

