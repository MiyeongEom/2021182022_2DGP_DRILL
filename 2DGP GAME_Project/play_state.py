from pico2d import*

class Stage_ONE():
    def __init__(self):
        self.stage1 = load_image('stage1_background.png')

    def draw(self):
        self.stage1.draw(1300 // 2, 600 // 2)

GAME_X = 1300 # 화면 크기
GAME_Y = 600

open_canvas(GAME_X, GAME_Y)

running = None

def enter():
    global stage1
    global running
    stage1 = Stage_ONE()
    running = True

# 게임 종료 - 객체 소멸
def exit():
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

open_canvas(GAME_X, GAME_Y)
enter()

while running:
    update()
    draw()

exit()
close_canvas()