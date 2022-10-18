from pico2d import*
import game_framework
import title_state
import logo_state

# 화면 크기
GAME_X = 1300
GAME_Y = 600

class Stage_ONE():
    def __init__(self):
        self.stage1 = load_image('stage1_background.png')

    def draw(self):
        self.stage1.draw(650, 300)

class Hero():
    def __int__(self):
        self.Idle = load_image('MC_Idle.png')

    def draw(self):
        pass

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)


stage1 = None
running = None

def enter():
    global stage1, running
    stage1 = Stage_ONE()
    running = True

# 게임 종료 - 객체 소멸
def exit():
    global stage1
    del stage1

#게임 객체 업데이트 - 게임 로직
def update():
    pass

def draw():
    # 개암 월드 렌더림
    clear_canvas()
    stage1.draw()
    update_canvas()

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

if __name__ == '__main__': # 만약 단독 실행 상태이면,
    test_self()
