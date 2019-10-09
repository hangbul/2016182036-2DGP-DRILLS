from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir
    global dir_ud
    global mouse_x, mouse_y
    global to_x, to_y

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, KPU_HEIGHT - 1 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            to_x, to_y = event.x, event.y
            if (x < to_x):
                dir = 1
            elif (x > to_x):
                dir = -1
            elif (x == to_x):
                dir = 0

            if (y < to_y):
                dir_ud = -1
            elif (y > to_y):
                dir_ud = 1
            elif (y == to_y):
                dir_ud = 0

    pass

def character_move(dir, dir_ud, dir_bfor):
    global frame_x, frame_y, x,y
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
    x += dir * 2
    y += dir_ud * 2
    pass

open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')
hand_arrow = load_image('hand_arrow.png')

running = True
x, y = KPU_WIDTH // 2, KPU_HEIGHT // 2
to_x, to_y = 0, 0
mouse_x, mouse_y = KPU_WIDTH // 2, KPU_HEIGHT // 2

frame_x = 0
frame_y = 1

dir = 0
dir_ud = 0
dir_bfor = 1

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    hand_arrow.draw_now(mouse_x, mouse_y)

    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame_x = (frame_x + 1) % 8
    character_move(dir, dir_ud, dir_bfor)



    #delay(0.01)

close_canvas()

