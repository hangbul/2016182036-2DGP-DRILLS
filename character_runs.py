from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('run_animation.png')

x = 60
frame=0

while(True):
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame*100, 0, 100, 100, x, 90)
    update_canvas()
    frame = (frame + 1) % 8
    x = (x + 10) % 800
    delay(0.05)
    get_events()


close_canvas()

