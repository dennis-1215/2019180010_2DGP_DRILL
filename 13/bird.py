from pico2d import *
from random import *

import game_framework
import game_world
# 1 frame 183 pixel
# Bird Run Speed
PIXEL_PER_METER = (182.0 / 0.3) # 182 pixel = 30 cm
RUN_SPEED_KMPH = 1.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# Bird Action Speed
TIME_PER_ACTION = 1.0
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 14

class RUN:
    def enter(self, event):
        pass

    def exit(self, event):
        pass

    def do(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.dir * RUN_SPEED_PPS * game_framework.frame_time
        if self.x > 950 or self.x < 50:
            self.dir *= -1

    def draw(self):
        if self.dir == 1:
            self.image.clip_composite_draw((int(self.frame) % 5) * 182, 506 - (170 * ((int(self.frame) // 5) + 1)), 182, 170, 0, '', self.x, self.y, 182, 170)
        elif self.dir == -1:
            self.image.clip_composite_draw((int(self.frame) % 5) * 182, 506 - (170 * ((int(self.frame) // 5) + 1)), 182, 170, 3.141592, 'v', self.x, self.y, 182, 170)


#3. 상태 변환 구현
next_state = {
    RUN:   {}
}




class Bird:
    def __init__(self):
        self.x, self.y = randint(100, 200), randint(70, 500)
        self.frame = 0
        self.dir, self.face_dir = 1, 1
        self.image = load_image('bird_animation.png')

        self.timer = 100

        self.event_que = []
        self.cur_state = RUN
        self.cur_state.enter(self, None)

    def update(self):
        self.cur_state.do(self)
        if self.event_que:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            try:
                self.cur_state = next_state[self.cur_state][event]
            except KeyError:
                print(f'ERROR: State {self.cur_state.__name__}')
            self.cur_state.enter(self, event)

    def draw(self):
        self.cur_state.draw(self)


    def add_event(self, event):
        self.event_que.insert(0, event)

    def handle_event(self, event):
        pass

