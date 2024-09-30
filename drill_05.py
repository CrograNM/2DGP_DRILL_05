from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character_run = load_image('RunSheet.png')
character_idle = load_image('IdleSheet.png')

def handle_events():
    global playing, running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            playing = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            playing = False
    pass

playing = True
running = True
x = 800 // 2
frame = 0
dir = 0

# fill here
while playing:
        clear_canvas()
        ground.draw(400, 300, 800, 600)

        if running:
            character_run.clip_draw(frame * 32, 0, 32, 32, x, 90, 60, 60)
        else:
            character_idle.clip_draw(frame * 32, 0, 32, 32, x, 90, 60, 60)

        update_canvas()
        handle_events()
        frame = (frame + 1) % 8
        delay(0.05)

close_canvas()

