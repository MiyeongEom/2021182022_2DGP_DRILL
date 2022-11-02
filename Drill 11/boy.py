from pico2d import *

#이벤트 정의

RD, LD, RU, LU, TIMER, AD = range(6) # 0 1 2 3 4 5

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT) : RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT) : RU,
    (SDL_KEYUP, SDLK_LEFT) : LU,

    (SDL_KEYDOWN, SDLK_a) : AD,
}

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP') #디버거 용도
        self.dir = 0
        pass

    @staticmethod
    def exit(self):
        print('EXIT SLEEP')
        pass

    @staticmethod
    def do(self): #프레임 증가는 해야함
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1: #오른쪽을 바라보고 있는 상태
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.141592/2, '', self.x - 25, self.y - 25, 100, 100)
        else: #왼쪽
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x - 25 , self.y - 25, 100, 100)
        pass

# 클래스를 이용해 상태를 만듦
class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0
        # 타이머 설정
        self.timer = 100
        pass

    @staticmethod
    def exit(self):
        print('EXIT RUN')
        pass

    @staticmethod
    def do(self): #움직일 수 있도록 프레임 증가
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0: #시간이 경과하면 timer 이벤트 발생
            #self.q.insert(0, TIMER) #객체지향프로그래밍에 위배, Q를 직접 액세스 하고 있기에
            self.add_event(TIMER) #객체지향적인 방법

        pass

    @staticmethod
    def draw(self):
        if self.face_dir == 1: #오른쪽을 바라보고 있는 상태
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else: #왼쪽
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
        pass

# shift + enter
class RUN:
    def enter(self, event):
        print('ENTER RUN')
        # self.dir을 결정해야 함.
        # 왜? : 아이들에서 런 상태가 되었을 때 아이들에서 나올 떄 왼쪽키를 눌렀는지 혹은 오른쪽 키를 눌렀는지에 의해 판단됨
        # 따라서 셀프 뿐만 아니라 이벤트도 같이 전달되어야 함, 이것을 아이들도 맞춰줘야함
        if event == RD:
            self.dir += 1
        elif event == LD:
            self.dir -= 1
        elif event == RU:
            self.dir -= 1
        elif event == LU:
            self.dir += 1
        pass

    def exit(self):
        print('ENTER EXIT')
        # run을 나가서 idle로 갈 때 run의 방향을 알려줄 필요가 있다.
        self.face_dir = self.dir
        pass

    def do(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir
        self.x = clamp(0, self.x, 800) #x값을 0과 800사이로 제한
        pass

    def draw(self):
         if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
         elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)

class AUTO_RUN:
    def enter(self, event):
        print('ENTER AUTO')
        self.dir = self.face_dir
        self.y += 20


    def exit(self):
        print('EXIT AUTO')
        self.face_dir = self.dir
        self.dir = 0
        self.y -= 20


    def do(self): #움직일 수 있도록 프레임 증가
        self.frame = (self.frame + 1) % 8

        if self.x <= 0:
            self.dir = 1
        elif self.x >= 800:
            self.dir = -1
        self.x += self.dir
        self.x = clamp(0, self.x, 800)


    def draw(self):
        if self.face_dir == -1: #오른쪽을 바라보고 있는 상태
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y, 150)
        elif self.dir == 1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y, 150)


next_state = {
    SLEEP: {RD: RUN, LD: RUN, RU: RUN, LU: RUN, AD: IDLE}, #SLEEP -> SLEEP 발생한 경우 ERROR_STATE를 하나 만들어두는 것도 좋음
    IDLE: {RU: RUN, LU: RUN, RD: RUN, LD: RUN, TIMER: SLEEP, AD: AUTO_RUN},
    RUN: {RU: IDLE, LU: IDLE, RD: IDLE, LD: IDLE, AD: AUTO_RUN},
    AUTO_RUN: {RD: RUN, LD: RUN, RU: AUTO_RUN, LU: AUTO_RUN, AD: IDLE}
}


class Boy:

    def add_event(self, event):
        self.q.insert(0, event)

    def handle_event(self, event):  #소년이 스스로 이벤트를 처리할 수 있게.. ctrl + r
        # event 는 key event이기에 이것을 내무 RD 등으로 변환
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event) #변환된 내부 이벤트를 큐에 추가

        #if event.type == SDL_KEYDOWN:
        #    match event.key:
        #        case pico2d.SDLK_LEFT:
        #            self.dir -= 1
        #        case pico2d.SDLK_RIGHT:
        #            self.dir += 1
        #elif event.type == SDL_KEYUP:
        #    match event.key:
        #        case pico2d.SDLK_LEFT:
        #            self.dir += 1
        #            self.face_dir = -1
        #        case pico2d.SDLK_RIGHT:
        #            self.dir -= 1
        #            self.face_dir = 1

    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []
        self.cur_state = IDLE
        self.cur_state.enter(self, None) #맨처음에는 이벤트가 없었기에


    def update(self):
        self.cur_state.do(self)

        if self.q : #q에 뭔가 들어있다면,
            event = self.q.pop() #이벤트를 가져오고
            self.cur_state.exit(self) #현재 상태를 나가고, self에 대한 정보는 전달해주고 ^^
            self.cur_state = next_state[self.cur_state][event] #다음 상태를 계산
            self.cur_state.enter(self, event)

        #self.frame = (self.frame + 1) % 8
        #self.x += self.dir * 1
        #self.x = clamp(0, self.x, 800)

    def draw(self):
        self.cur_state.draw(self)

        #if self.dir == -1:
        #    self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        #elif self.dir == 1:
        #    self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        #else:
        #    if self.face_dir == 1:
        #        self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        #    else:
        #       self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)
