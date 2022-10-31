from pico2d import *


# 이벤트 정의

#RD, LD, RU, LU = 0, 1, 2, 3
RD, LD, RU, LU, TIMER, AD = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_RIGHT): RD,
    (SDL_KEYDOWN, SDLK_LEFT) : LD,
    (SDL_KEYUP, SDLK_RIGHT)  : RU,
    (SDL_KEYUP, SDLK_LEFT)   : LU,
    (SDL_KEYDOWN, SDLK_a)    : AD,

}

class AUTO_RUN:
    def enter(self, event):

        pass
    def exit(self):

        pass
    def do(self):
        # 달리게 만들어 준다
        self.frame = (self.frame + 1) % 8
        self.x += self.face_dir * 1
        self.x = clamp(0, self.x, 800)

        pass
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.face_dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class IDLE:
    @staticmethod
    def enter(self, event):
        print('ENTER IDLE')
        self.dir = 0 # 정지 상태
        self.timer = 1000
        pass
    @staticmethod
    def exit(self):
        print('EXIT IDLE')
        pass
    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        self.timer -= 1
        if self.timer == 0:
            self.add_event(TIMER)
        pass
    @staticmethod
    def draw(self):
        if self.face_dir == 1:
            self.image.clip_draw(self.frame * 100, 300, 100, 100, self.x, self.y)
        else:
            self.image.clip_draw(self.frame * 100, 200, 100, 100, self.x, self.y)

        pass

class RUN:
    def enter(self, event):
        print('ENTER RUN')
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
        print('EXIT RUN')
        # 런 상태를 나갈때 현재방향을 저장해놓음.
        self.face_dir = self.dir
        pass
    def do(self):
        # 달리게 만들어 준다
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 1
        self.x = clamp(0, self.x, 800)
        pass
    def draw(self):
        if self.dir == -1:
            self.image.clip_draw(self.frame*100, 0, 100, 100, self.x, self.y)
        elif self.dir == 1:
            self.image.clip_draw(self.frame*100, 100, 100, 100, self.x, self.y)
        pass

class SLEEP:
    @staticmethod
    def enter(self, event):
        print('ENTER SLEEP')
        self.dir = 0  # 정지 상태
        pass

    @staticmethod
    def exit(self):
        print('EXIT SLEEP')
        pass

    @staticmethod
    def do(self):
        self.frame = (self.frame + 1) % 8
        pass

    @staticmethod
    def draw(self):
        if self.face_dir == -1:
            self.image.clip_composite_draw(self.frame * 100, 200, 100, 100, -3.141592/2, '', self.x + 25, self.y - 25, 100, 100)
        else:
            self.image.clip_composite_draw(self.frame * 100, 300, 100, 100, 3.131492/2, '', self.x - 25, self.y - 25, 100, 100)

        pass

next_state = {
    IDLE    : {RU: RUN , LU: RUN   , RD: RUN   , LD: RUN   ,AD: AUTO_RUN ,TIMER: SLEEP},
    RUN     : {RU: IDLE, LU: IDLE  , RD: IDLE  , LD: IDLE  ,AD: AUTO_RUN },
    SLEEP   : {RU: RUN , LU: RUN   , RD: RUN   , LD: RUN},
    AUTO_RUN: {RU: RUN , LU: RUN   , RD: RUN   , LD: RUN, AD: IDLE }
}

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.image = load_image('animation_sheet.png')

        self.q = []

        # 초기 상태 설정과 entry action 수행
        self.cur_state = IDLE
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)

        if self.q: # 만약 리스트 q에 값이 있다면
            event = self.q.pop() # 이벤트를 확인하고
            self.cur_state.exit(self) # 현재 상태를 나가고
            self.cur_state = next_state[self.cur_state][event] # 다음 상태를 계산하고
            self.cur_state.enter(self, event) # 다음 상태의 enter 액션을 수행





    def draw(self):
        self.cur_state.draw(self)



    def add_event(self, key_event):
        self.q.insert(0, key_event)

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)

        # if event.type == SDL_KEYDOWN:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir -= 1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir += 1
        #
        # elif event.type == SDL_KEYUP:
        #     match event.key:
        #         case pico2d.SDLK_LEFT:
        #             self.dir += 1
        #             self.face_dir = -1
        #         case pico2d.SDLK_RIGHT:
        #             self.dir -= 1
        #             self.face_dir = 1
