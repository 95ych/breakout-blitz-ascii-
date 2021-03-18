import global_var 
import utilities
import random
import config
import objects
from time import time, sleep
from getch import KBHit
from global_var import paddle, balls, bricks, power_ups, mp
import global_var

import inputs 


utilities.initialize_board()
timetrack = time()
utilities.brick_gen()


while True:
    # setting 25 fps
     if time() - timetrack >= 0.1:
        timetrack = time()
        if paddle.get_lives() ==0 or len(bricks)==0:
            break
        utilities.initialize_board()
        paddle.clear()
        for ball in balls:
            ball.clear()
        for brick in bricks:
            brick.clear()
            brick.render()
        inputs.movedin()
        paddle.render()
        for ball in balls:
            ball.check_collision()
            
            if ball.paddle_grab==0:
                ball.ymove(ball.ygetspeed())
                ball.xmove(ball.xgetspeed())
            else:
                ball.xset(paddle.xget() + ball.get_x_on_paddle())
            
        for power_up in power_ups:
            power_up.clear()
            power_up.ymove(power_up._yspeed)
            power_up.check_collision()
        
        for power_up in power_ups:
            power_up.render()
        for ball in balls:
            ball.render()
        for brick in bricks:
            brick.check_collision()
        utilities.check_powers()
utilities.clear_board()
if paddle.get_lives() ==0:
    print('Game Over')
else: print('Yayy you won') 
print("Time :" + str(int(time() - mp.get_start_time()))+" "*20 +"Score: " + str(paddle._score) )