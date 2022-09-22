from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

x = 0
y = 90
radian = 180
while(True):
    
# 사각형 운동
    while (x < 779):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x = x+2
        delay(0.01)
    while (y <554):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y = y+2
        delay(0.01)
    while (x > 21):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x = x-2
        delay(0.01)
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        y = y-2
        delay(0.01)
    while (x < 400):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        x = x+2
        delay(0.01)
        
# 원 운동
    if radian == 540:
        radian = 180

    while (radian < 540):
        x = 400 + math.sin(radian / 360 * 2 * math.pi)* 210
        y = 300 + math.cos(radian / 360 * 2 * math.pi)* 210

        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x, y)
        radian += 1
        delay(0.01)
        
    

        
close_canvas()
