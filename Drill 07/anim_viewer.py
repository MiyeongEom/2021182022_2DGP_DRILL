from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('Idle.png')
Run_User = load_image('Run.png')

x = 130
y = 90

def basic_backgruond():
    clear_canvas()
    grass.draw(400, 30)

def Stand_User():
    frame = 0
    count = 0
    while (count < 12):
        basic_backgruond()
        character.clip_draw(frame * 100, 0, 100, 100, x, y)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.2)
        get_events()
        count = count + 1

def Running_User():
    frame = 0
    dis = 0
    while (x + dis < 700):
        basic_backgruond()
        Run_User.clip_draw(frame * 100, 0, 100, 100, x+dis, y-10)
        update_canvas()
        frame = (frame + 1) % 5
        dis += 6
        delay(0.03)
        get_events()


Stand_User()
Running_User()
Stand_User()

close_canvas()