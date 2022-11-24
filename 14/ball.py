from pico2d import *
import game_world
import server
from random import *

class Ball:
    image = None

    def __init__(self):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x, self.y = randint(50, 900), randint(50, server.background.h - 50)

    def draw(self):
        sx, sy = self.x - server.background.window_left, self.y - server.background.window_bottom
        self.image.draw(sx, sy)

    def get_bb(self):
        return self.x - 6, self.y - 6, self.x + 6, self.y + 6

    def handle_collision(self, other, group):
        if group == 'boy:ball':
            other.ball_count += 1
            game_world.remove_object(self)

    def update(self):
        pass