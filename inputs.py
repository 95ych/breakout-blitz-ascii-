from getch import KBHit
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
        if global_var.paddle.xget() <= global_var.mp.start_index + config.columns  -3- global_var.paddle.get_width() and global_var.paddle.xget() <= 1090:
            global_var.paddle.xmove(config.PADDLE_SPEED)
            
        elif global_var.paddle.xget() >= global_var.mp.start_index + config.columns  -3- global_var.paddle.get_width() and global_var.paddle.xget() <= global_var.mp.start_index + config.columns -1- global_var.paddle.get_width(): 
            global_var.paddle.xmove(1)
            
    if char == 'a':
        if global_var.paddle.xget() > global_var.mp.start_index + 1:
            global_var.paddle.xmove(-config.PADDLE_SPEED)
            
    if char == ' ':
        for ball in global_var.balls:
            ball.paddle_grab = 0
    
    if char == 'p':
        global_var.pause= 0 if global_var.pause==1 else 1
    
    if char == 'q':
        quit()

def paused():
    if char == 'p':
        global_var.pause= 0 if global_var.pause==1 else 1

    if char == 'q':
        quit()