from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global playing, running, dir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            playing = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                dir += 1
            elif event.key == SDLK_LEFT:
                dir -= 1
            elif event.key == SDLK_ESCAPE:
                playing = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                running = False
                dir -= 1
            elif event.key == SDLK_LEFT:
                running = False
                dir += 1
    pass

playing = True
running = False
x = 800 // 2
y = 170
frame_run = 0
frame_idle = 0
dir = 0

# fill here
while playing:
        clear_canvas()
        ground.draw(400, 300, 800, 600)

        if running:
            character.clip_draw(frame_run * 50, 0, 50, 80, x, y, 50, 80)
            frame_run = (frame_run + 1) % 4
        else:
            character.clip_draw(frame_idle * 38, 80, 38, 80, x, y, 38, 80)
            frame_idle = (frame_idle + 1) % 6
        x += dir * 5
        update_canvas()
        handle_events()
        delay(0.1)

close_canvas()

