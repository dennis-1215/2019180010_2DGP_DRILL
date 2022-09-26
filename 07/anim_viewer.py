from pico2d import *
import math

open_canvas()
character = load_image('character.png')
character2 = load_image('character2.png')

def die_animation(x, y):
    frame, count = 0, 0
    while (count < 9):
        clear_canvas()
        character.clip_draw(2 + frame * 71, 252, 67, 59, x, y)
        update_canvas()
        frame = (frame + 1) % 9
        count += 1
        delay(0.1)
        get_events()

def idle_animation(x, y):
    frame, count = 0, 0
    while(count < 30):
        clear_canvas()
        character.clip_draw(203, 615 - frame * 75, 63, 72, x, y)
        update_canvas()
        frame = (frame + 1) % 5
        count += 1
        delay(0.05)
        get_events()

def move_right_animation(start_x, end_x, y):
    frame = 0
    for x in range(start_x, end_x, 10):
        clear_canvas()
        character.clip_draw(203, 615 - frame * 75, 63, 72, x, y)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.05)
        get_events()

def move_left_animation(start_x, end_x, y):
    frame = 0
    for x in range(start_x, end_x, -10):
        clear_canvas()
        character2.clip_draw(333, 615 - frame * 75, 63, 72, x, y)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.05)
        get_events()

def move_up_animation(start_y, end_y, x):
    frame = 0
    for y in range(start_y, end_y, 10):
        clear_canvas()
        character.clip_draw(2, 615 - frame * 75, 63, 72, x, y)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.05)
        get_events()

def move_down_animation(start_y, end_y, x):
    frame = 0
    for y in range(start_y, end_y, -10):
        clear_canvas()
        character.clip_draw(538, 615 - frame * 75, 63, 72, x, y)
        update_canvas()
        frame = (frame + 1) % 5
        delay(0.05)
        get_events()

def move_circle():
    radian = -90
    frame = 0
    while (radian < 270):
        x = 400 + math.cos(radian / 360 * 2 * math.pi) * 100
        y = 300 + math.sin(radian / 360 * 2 * math.pi) * 100
        clear_canvas()
        if (radian < -60):
            character.clip_draw(136, 615 - frame * 75, 63, 72, x, y)
        elif (radian < -30):
            character.clip_draw(69, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 0):
            character.clip_draw(2, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 30):
            character2.clip_draw(534, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 60):
            character2.clip_draw(467, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 90):
            character2.clip_draw(400, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 120):
            character2.clip_draw(266, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 150):
            character2.clip_draw(199, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 180):
            character2.clip_draw(132, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 210):
            character.clip_draw(471, 615 - frame * 75, 63, 72, x, y)
        elif (radian < 240):
            character.clip_draw(404, 615 - frame * 75, 63, 72, x, y)
        else:
            character.clip_draw(337, 615 - frame * 75, 63, 72, x, y)

        update_canvas()
        frame = (frame + 1) % 5
        radian += 3
        delay(0.05)
        get_events()

while True:
    move_right_animation(200, 600, 300)
    move_left_animation(600, 400, 300)
    move_up_animation(300, 500, 400)
    move_down_animation(500, 200 , 400)
    move_circle()
    idle_animation(400, 200)
    die_animation(400, 200)

close_canvas()
