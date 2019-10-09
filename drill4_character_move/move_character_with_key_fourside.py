from pico2d import *

KPU_WIDTH, KPU_HEIGHT = 1280, 1024

def handle_events():
    global running
    global dir
    global dir_ud

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_UP:
                dir_ud += 1
            elif event.key == SDLK_DOWN:
                dir_ud -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
            elif event.key == SDLK_UP:
                dir_ud -= 1
            elif event.key == SDLK_DOWN:
                dir_ud += 1
    pass


open_canvas(KPU_WIDTH, KPU_HEIGHT)
kpu_ground = load_image('KPU_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y = 90
frame_x = 0
frame_y = 1

dir = 0
dir_ud = 0
dir_bfor = 1

while running:
    clear_canvas()
    kpu_ground.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, y)
    update_canvas()

    handle_events()
    frame_x = (frame_x + 1) % 8

    if (dir == -1):
        frame_y = 0
        dir_bfor = -1
    elif (dir == 1):
        frame_y = 1
        dir_bfor = 1

    if(dir_ud != 0):
        if (dir_bfor == -1):
            frame_y = 0
        elif (dir_bfor == 1):
            frame_y = 1
    elif(dir == 0):
        if (dir_bfor == 1):
            frame_y = 3
        elif (dir_bfor == -1):
            frame_y = 2



    x +=dir * 2
    y +=dir_ud *2

    if x >= KPU_WIDTH:
        x = 0
    elif x < 0:
        x = KPU_WIDTH
    if y >= KPU_HEIGHT:
        y = 0
    elif y < 0:
        y = KPU_HEIGHT

    #delay(0.01)

close_canvas()

