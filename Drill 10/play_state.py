from pico2d import *
import game_framework
import item_state
import random

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = random.randint(10,790), 90
        self.frame = 0
        self.dir = 1
        self.image = load_image('animation_sheet.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0 :
            self.dir = 1
            self.x = 0

    def draw(self):
        if self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        elif self.dir == -1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                #game_framework.change_state(title_state)
                game_framework.quit()
            if event.key == SDLK_b:
                game_framework.push_state(item_state)

boys = []
boy = None
grass = None

#게임 초기화 : 객체들 생성
def enter():
    global boy,grass
    boy = Boy()
    boys.append(boy)
    grass = Grass()

#게임 종료 코드 - 객체 소멸 /
def exit():
    global boy,grass,boys
    del boy
    del grass
    del boys

    # 게임월드 객체 업데이트
def update():
    for b in boys:
        b.update()

    # 게임월드 렌더링
def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def draw_world():
    grass.draw()
    for b in boys:
        b.draw()


def pause():
    pass

def resume():
    pass

def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__':# 만약 단독실행 상태라면
    test_self()
