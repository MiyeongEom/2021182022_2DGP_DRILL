from pico2d import *
import game_framework
import game_world

from grass import Grass
from boy import Boy

boy = None
grass1 = None
grass2 = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        else:
            boy.handle_event(event)

# 초기화
def enter():
    global boy, grass1, grass2
    boy = Boy()
    grass1 = Grass()
    grass2 = Grass()
    grass1.y = 45

    game_world.add_object(grass1, 0)
    game_world.add_object(boy, 1)
    game_world.add_object(grass2, 2)


# 종료
def exit():
    game_world.clear()

def update():
    # boy.update()
    for game_object in game_world.all_objects():
        game_object.update()

def draw_world():
    for game_object in game_world.all_objects():
        game_object.draw()
    #grass.draw()
    #if ball == None:
    #    ball.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass



def test_self():
    import play_state

    pico2d.open_canvas()
    game_framework.run(play_state)
    pico2d.clear_canvas()

if __name__ == '__main__':
    test_self()
