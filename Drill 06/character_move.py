from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')

while(1):
    x = 0
    while (x < 780):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 90)
        x = x + 2
        delay(0.01)
       
    y=0
    while (y < 470):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(780, y+90)
        y = y + 2
        delay(0.01)

    x = 780
    while (x > 0):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(x, 560)
        x = x - 2
        delay(0.01)

    y = 560
    while (y > 90):
        clear_canvas_now()
        grass.draw_now(400, 30)
        character.draw_now(10, y)
        y = y - 2
        delay(0.01)


    x = 400
    y = 300
    n = -90
    r = 210
    
    while (n < 270):
      clear_canvas_now()
      grass.draw_now(400, 30)
      character.draw_now(x + r * math.cos(n / 360 * 2 * math.pi), y + r * math.sin(n / 360 * 2 * math.pi))
      n += 1
      delay(0.01)
     
    
