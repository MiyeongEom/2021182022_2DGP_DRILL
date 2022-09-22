from pico2d import *
open_canvas()
grass = load_image('grass.png')
character = load_image('Idle.png')

def basic_backgruond():
    clear_canvas()
    grass.draw(400, 30)

frame = 0
count = 0
while(count < 15):
    basic_backgruond()
    character.clip_draw(frame * 100, 0, 100, 100, 300, 90)
    update_canvas()
    frame = (frame + 1) % 4
    delay(0.2)
    get_events()
    count = count + 1

close_canvas()