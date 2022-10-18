from pico2d import *
import play_state
import logo_state
import game_framework

pico2d.open_canvas()
game_framework.run(play_state)
pico2d.close_canvas()