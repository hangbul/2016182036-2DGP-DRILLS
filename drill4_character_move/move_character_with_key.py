from pico2d import *


def handle_events():
    global running
    global dir

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir -= 1
            elif event.key == SDLK_LEFT:
                dir += 1
    pass


open_canvas()
grass = load_image('grass.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
frame_x = 0
frame_y = 1

dir = 0
dir_side = 1

while running:
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame_x * 100, frame_y * 100, 100, 100, x, 90)
    update_canvas()

    handle_events()
    frame_x = (frame_x + 1) % 8

    if(dir == -1):
        frame_y = 0
        dir_side = -1
    elif(dir == 1):
        frame_y = 1
        dir_side = 1

    if(dir == 0):
        if (dir_side == 1):
            frame_y = 3
        elif (dir_side == -1):
            frame_y = 2



    x +=dir * 3

    if x>= 800:
        x=0
    elif x<0:
        x=800

    #delay(0.01)

close_canvas()

