from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('Idle.png')
Run_User = load_image('Run.png')
Walk_User = load_image('Walking.png')

user_x = 130
user_y = 90


def basic_ground():
    clear_canvas()
    grass.draw(400, 30)


def running():
    global x
    frame = 0
    x = user_x
    y = user_y
    while x < 700 + 1:
        basic_ground()
        Run_User.clip_draw(frame * 100, 0, 100, 100, x, y - 10)
        update_canvas()
        frame = (frame + 1) % 5
        x += 6
        delay(0.04)
        get_events()

def stand():
    user_x = x
    frame = 0
    count = 0
    while count < 12:
        basic_ground()
        character.clip_draw(frame * 100, 0, 100, 100, user_x, user_y)
        update_canvas()
        frame = (frame + 1) % 4
        delay(0.2)
        get_events()
        count = count + 1


def walking():
    global x
    frame = 0
    x = 700
    while x > 50:
        basic_ground()
        Walk_User.clip_draw(frame * 100, 0, 100, 100, x, user_y - 10)
        update_canvas()
        frame = (frame + 1) % 5
        x -= 5
        delay(0.04)
        get_events()

running()
stand()
walking()
stand()

close_canvas()

# fire sprite 꼭 구현 해보기
# 함수, 지역/전역 변수 공부
