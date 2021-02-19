from getch import KBHit
from global_var import paddle
import global_var
import utilities
import config
from time import time
import objects

kb = KBHit()

def movedin():
    # moves the player
    char = kb.getinput()

    if char == 'd':
        if paddle.xget() <= global_var.mp.start_index + config.columns  -3- paddle.get_width() and paddle.xget() <= 1090:
            paddle.xmove(3)
        elif paddle.xget() >= global_var.mp.start_index + config.columns  -3- paddle.get_width() and paddle.xget() <= global_var.mp.start_index + config.columns -1- paddle.get_width(): 
            paddle.xmove(1)
    if char == 'a':
        if paddle.xget() > global_var.mp.start_index + 1:
            paddle.xmove(-3)

    # if char == 'w':
    #     if mando.yget() >= 5:
    #         mando.yset(-1)
    #         mando.set_air_pos(mando.yget())
    #         mando.set_air_time(time())

    # if char == ' ' and mando.get_shield_allow() == 1:
    #     mando.set_shield_allow(0)
    #     mando.set_shield_time(time())
    #     mando.set_shield(1)

    if char == 'q':
        quit()