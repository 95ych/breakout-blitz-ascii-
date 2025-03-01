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
level_start = timetrack
current_level = global_var.level
win=0
drop= timetrack
while True:
     
    # setting 10 fps
    if time() - timetrack >= 0.1 and global_var.pause==0:
        bpc=0 # ball-paddle-collision
        
        timetrack = time()
        if global_var.paddle.get_lives() == 0 or win:
            break
        
        if broken_bricks >= global_var.breakable_bricks[current_level-1]:
            global_var.level+=1
        
        if current_level != global_var.level:
            broken_bricks = 0
            current_level = global_var.level
            level_start = timetrack
            if current_level>3:
                win=1
            else:
                utilities.brick_gen(global_var.level)
                for i in global_var.lasers:
                    i.clear()
                for i in global_var.power_ups:
                    i.clear()
                global_var.lasers = []
                global_var.power_ups = []
                utilities.default()
        
        utilities.initialize_board()
        
        global_var.paddle.clear()
        for ball in global_var.balls:
            ball.clear()
        

        for boss in global_var.bosses:
            boss.clear()
            if timetrack - drop <= config.shoot_time:
                boss.drop_bombs(0.3)

            boss.xset(global_var.paddle.xget()+1)
            boss.check_collision()
            boss.render()
            if boss.get_health() < 0:
                win=1
        
        

        dirc = inputs.movedin() #record direction of paddle
        if dirc!=global_var.cd:
            global_var.cd = dirc
            drop=timetrack

        global_var.paddle.render()
        
        for ball in global_var.balls:
            bpc += ball.check_collision()
            
            if ball.paddle_grab==0:
                ball.ymove(ball.ygetspeed())
                ball.xmove(ball.xgetspeed())
            else:
                ball.xset(global_var.paddle.xget() + ball.get_x_on_paddle())
        
        for laser in global_var.lasers:
            laser.clear()
            laser.ymove(-1)
            broken_bricks+= laser.check_collision()
          
        for laser in global_var.lasers: 
            laser.render()
        
        for brick in global_var.bricks:
            brick.clear()
            if timetrack-level_start>config.TIME_ATTACK and bpc:
                brick.ymove(1)
                if brick.yget() == config.rows-3:
                    global_var.paddle.set_lives(0)
            brick.render()

        for power_up in global_var.power_ups:
            power_up.clear()
            power_up.yacc(config.GRAVITY)
            power_up.ymove(power_up._yspeed)
            power_up.xmove(power_up._xspeed)
            power_up.check_collision()
        
        for power_up in global_var.power_ups:
            power_up.render()
        
        

        for bomb in global_var.bombs:
            bomb.clear()
            bomb.ymove(1)
            bomb.check_collision()
          
        for bomb in global_var.bombs: 
            bomb.render()
        
        
        for ball in global_var.balls:
            ball.render()
        for brick in global_var.bricks:
            broken_bricks += brick.check_collision()
        utilities.check_powers()

        
    
    elif global_var.pause:
        inputs.movedin()
        print('\r--------------------Paused--------------------',end='')
utilities.clear_board()

if global_var.paddle.get_lives() ==0:
    print('Game Over')
else: print('Yayy you won') 
print("Time :" + str(int(time() - global_var.mp.get_start_time()))+" "*20 +"Score: " + str(global_var.paddle._score) )