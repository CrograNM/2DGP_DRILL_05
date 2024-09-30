from pico2d import *


open_canvas()
ground = load_image('TUK_GROUND.png')
character = load_image('sprite_sheet.png')

def handle_events():
    global playing, running, Xdir, Ydir, isLeft
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            playing = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                isLeft = False
                Xdir += 1
            elif event.key == SDLK_LEFT:
                isLeft = True
                Xdir -= 1
            if event.key == SDLK_UP:
                Ydir += 1
            elif event.key == SDLK_DOWN:
                Ydir -= 1
            elif event.key == SDLK_ESCAPE:
                playing = False

        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                Xdir -= 1
            elif event.key == SDLK_LEFT:
                Xdir += 1
            if event.key == SDLK_UP:
                Ydir -= 1
            elif event.key == SDLK_DOWN:
                Ydir += 1
    pass

playing = True
running = False
isLeft = False
x = 800 // 2
y = 170
Xdir = 0
Ydir = 0
frame_run = 0
frame_idle = 0


# fill here
while playing:
        #캔버스 초기화, 배경 그리기
        clear_canvas()
        ground.draw(400, 300, 800, 600)
        #running 판단
        if Xdir == 0 and Ydir == 0:
            running = False
        else:
            running = True
        #좌우판단 후 버퍼에 그리기
        if running:
            if isLeft:
                character.clip_composite_draw(frame_run * 50, 0, 50, 80, 0, 'h', x, y, 50, 80)
            else:
                character.clip_draw(frame_run * 50, 0, 50, 80, x, y, 50, 80)
            frame_run = (frame_run + 1) % 4
        else:
            if isLeft:
                character.clip_composite_draw(frame_idle * 38, 80, 38, 80, 0, 'h', x, y, 38, 80)
            else:
                character.clip_draw(frame_idle * 38, 80, 38, 80, x, y, 38, 80)
            frame_idle = (frame_idle + 1) % 6
        #dir에 따라 좌표변환 -> 캔버스를 벗어나면 이동불가
        if 20 <= x <= 780:
            x += Xdir * 7
        else:
            if x < 20:
                x = 20
            elif x > 780:
                x = 780

        if 40 <= y <= 560:
            y += Ydir * 5
        else:
            if y < 40:
                y = 40
            elif y > 560:
                y = 560

        #그리기 및 이벤트 입력
        update_canvas()
        handle_events()
        delay(0.08)

close_canvas()

