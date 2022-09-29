from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1200, 1024
dir_x = 0;
dir_y = 0;
image = 1;

def handle_events():

    global dir_x, dir_y, image;
    global running

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir_x += 1
                image = 1
            elif event.key == SDLK_LEFT:
                dir_x -= 1
                image = 2
            elif event.key == SDLK_DOWN:
                dir_y += 1
            elif event.key == SDLK_UP:
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                dir_x -= 1
            elif event.key == SDLK_LEFT:
                dir_x += 1
            elif event.key == SDLK_DOWN:
                dir_y -= 1
            elif event.key == SDLK_UP:
                dir_y += 1

def outline():
    global x, y
    if x < 30: x = 0 + 30
    if x > TUK_WIDTH - 30 : x = TUK_WIDTH - 30
    if y < 30: y = 0 + 30
    if y >  TUK_HEIGHT  - 30: y =  TUK_HEIGHT  - 30

open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
frame = 0

while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)
    character.clip_draw(frame * 100, 100*image, 100, 100, x, y)
    update_canvas()
    frame = (frame + 1) % 8
    outline()
    delay(0.01)

    handle_events()
    x += dir_x * 5
    y += dir_y * 5

close_canvas()




