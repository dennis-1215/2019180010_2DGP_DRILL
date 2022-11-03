from pico2d import *

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')
        self.x, self.y = 400, 30

    def draw(self):
        self.image.draw(self.x, self.y )

    def update(self):
        pass

