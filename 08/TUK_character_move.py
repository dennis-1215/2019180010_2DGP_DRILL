from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024


def handle_events():
    global  running
    global x, y
    global dir

    global L_R_check
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir = 1
                L_R_check = 1
            elif event.key == SDLK_LEFT:
                dir = 2
                L_R_check = 2
            elif event.key == SDLK_UP:
                dir = 3
            elif event.key == SDLK_DOWN:
                dir = 4
             
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT or SDLK_LEFT or SDLK_UP or SDLK_DOWN:
                dir = 0
                


open_canvas(TUK_WIDTH, TUK_HEIGHT)
kpu_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x, y = TUK_WIDTH // 2, TUK_HEIGHT // 2
frame = 0
hide_cursor()
L_R_check = 1

while running:
    clear_canvas()
    kpu_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    if L_R_check == 1 and dir != 0:
        character.clip_draw(frame * 100, 100 * 1, 100, 100, x, y)
    elif L_R_check == 2 and dir != 0:
        character.clip_draw(frame * 100, 100 * 0, 100, 100, x, y)
    elif L_R_check == 1 and dir == 0:
        character.clip_draw(frame * 100, 100 * 3, 100, 100, x, y)
    elif L_R_check == 2 and dir == 0:
        character.clip_draw(frame * 100, 100 * 2, 100, 100, x, y)

    update_canvas()
    frame = (frame + 1) % 8
    if dir == 1:
        if x < TUK_WIDTH:
            x += 5
    elif dir == 2:
        if x > 0:
            x -= 5
    elif dir == 3:
        if y < TUK_HEIGHT:
            y += 5
    elif dir == 4:
        if y > 0:
            y -= 5
    delay(0.01)
    handle_events()

close_canvas()




