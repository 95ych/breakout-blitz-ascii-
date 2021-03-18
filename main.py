import global_var 
import utilities
import random
import config
import objects
from time import time, sleep
#from getch import KBHit


import inputs 

utilities.initialize_board()
timetrack = time()
utilities.brick_gen(global_var.level)
broken_bricks = 0

while True:
    # setting 10 fps
    if time() - timetrack >= 0.1 and global_var.pause==0:
        timetrack = time()
        if global_var.paddle.get_lives() ==0:
            break
        elif len(global_var.bricks) == 0:
            broken_bricks = 0
            global_var.level+=1
            utilities.brick_gen(global_var.level)
        utilities.initialize_board()
        global_var.paddle.clear()
        for ball in global_var.balls:
            ball.clear()
        for brick in global_var.bricks:
            brick.clear()
            brick.render()
        inputs.movedin()
        global_var.paddle.render()
        
        for ball in global_var.balls:
            ball.check_collision()
            
            if ball.paddle_grab==0:
                ball.ymove(ball.ygetspeed())
                ball.xmove(ball.xgetspeed())
            else:
                ball.xset(global_var.paddle.xget() + ball.get_x_on_paddle())
            
        for power_up in global_var.power_ups:
            power_up.clear()
            power_up.yacc(config.GRAVITY)
            power_up.ymove(power_up._yspeed)
            power_up.xmove(power_up._xspeed)
            power_up.check_collision()
        
        for power_up in global_var.power_ups:
            power_up.render()
        for ball in global_var.balls:
            ball.render()
        for brick in global_var.bricks:
            brick.check_collision()
        utilities.check_powers()
    elif global_var.pause:
        inputs.movedin()
utilities.clear_board()
if global_var.paddle.get_lives() ==0:
    print('Game Over')
else: print('Yayy you won') 
print("Time :" + str(int(time() - global_var.mp.get_start_time()))+" "*20 +"Score: " + str(global_var.paddle._score) )