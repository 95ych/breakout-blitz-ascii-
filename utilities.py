import config
import random
import os
import global_var
from colorama import init, Fore, Back, Style
import objects
from time import time
from numpy import inf



def create_header():
    print("\033[%d;%dH" % (0, 0), end='')
    #print("\033[2;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT)
    #print(Style.RESET_ALL)

def print_board():
    create_header()
    global_var.mp.render()

def display_ending(message):
    os.system('tput reset')
   
def initialize_board():
    init()
    os.system('clear')
    print_board()

def clear_board():
    os.system('clear')

def spawn_boss():
    global_var.bosses.append(objects.Ufo(config.ufo, global_var.paddle.xget() , 4))

def spawn_lasers(x,y):
    if time() - global_var.last_laser > 0.3:
        global_var.last_laser = time()
        global_var.lasers.append(objects.Laser(config.laser, x,y))
        global_var.lasers.append(objects.Laser(config.laser, x+global_var.paddle.get_width()-1,y))


def spawn_bomb(x,y,t):
    if time() - global_var.last_bomb > t:
        global_var.last_bomb = time()
        global_var.bombs.append(objects.Bomb(config.bomb, x,y))
        global_var.bombs.append(objects.Bomb(config.bomb, x+7,y))

def spawn_defence():
    for brick in global_var.bricks:
        if brick.yget()==8:
            brick.clear()
            global_var.bricks.remove(brick)

    for i in range(16):
            global_var.bricks.append(objects.Brick(config.brick,i*5,8,1,[0]))

def brick_gen(level):
    for brick in global_var.bricks:
        brick.clear()
    for ball in global_var.balls:
        ball.clear()
    global_var.bricks = []
    
    if level==1:
        global_var.bricks.append(objects.Brick(config.brick,2,5,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,2,12,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,9,5,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,9,12,inf,config.prob_distr))
        for i in range(6):
            global_var.bricks.append(objects.Brick(config.brick,i*7+15,10,-inf,config.prob_distr))
        
        for i in range(5):
            global_var.bricks.append(objects.Brick(config.brick,i*7+18,5,2,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,39+17,5,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,39+24,5,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,39+17,12,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,39+24,12,inf,config.prob_distr))

    elif level==2:
        global_var.bricks.append(objects.Brick(config.brick,28,10,-inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,35,10,-inf,config.prob_distr))
            
        for i in range(1,4):
            r = random.randint(2,3)
            global_var.bricks.append(objects.Brick(config.brick,28-i*8,10-i*2,r,config.prob_distr))
            global_var.bricks.append(objects.Brick(config.brick,35+i*8,10-i*2,r,config.prob_distr))    
        for i in range(1,3):
            global_var.bricks.append(objects.Brick(config.brick,28-i*8,10+i*2,1,config.prob_distr))
            global_var.bricks.append(objects.Brick(config.brick,35+i*8,10+i*2,1,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,25,6,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,38,6,inf,config.prob_distr))
    elif level==3:
        spawn_boss()
        global_var.bricks.append(objects.Brick(config.brick,25,10,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,38,10,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,2,12,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,9,12,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,39+17,12,inf,config.prob_distr))
        global_var.bricks.append(objects.Brick(config.brick,39+24,12,inf,config.prob_distr))
    

def drop_power_up(power, y, x,xspeed,yspeed):
    global_var.power_ups.append(objects.PowerUp(config.powerup,x,y, power,xspeed,yspeed))

def add_powers(power):
    flag =0
    if power!=3:
        for i in global_var.powers:
            if i[0] == power:
                i[1]=time()
                flag=1
    if flag==0:
        if power == 1:
            global_var.paddle.expand()
        elif power ==2:
            global_var.paddle.shrink()
        elif power ==3:
            tempballs = global_var.balls.copy()
            for ball in tempballs:
                global_var.balls.append(objects.Ball(config.ball,ball.xget(), ball.yget(),0,-ball._xspeed,-ball._yspeed))
        elif power ==4:
            for ball in global_var.balls:
                ball.inc_speed()
        elif power ==5:
            global_var.paddle.set_thru(1)
        elif power ==6:
            global_var.paddle.set_grab(1)
        elif power ==7:
            global_var.paddle.set_laser(1)
        global_var.powers.append([power, time()])


def check_powers():
    for i in global_var.powers:
        if time() - i[1] > config.POWER_TIME:
            if i[0] == 1 or i[0] == 2:
                global_var.paddle.set_width(9)
            if i[0] == 3:
                pass
            if i[0] == 5:
                global_var.paddle.set_thru(0)
            if i[0] == 6:
                global_var.paddle.set_grab(0)
            if i[0] == 7:
                global_var.paddle.set_laser(0)
            global_var.powers.remove(i)

def default():
    global_var.powers = []
    global_var.balls = [objects.Ball(config.ball, global_var.paddle.xget() , config.rows -4,1,0,1)]
    if global_var.paddle.get_width()!=9:
        global_var.paddle.set_width(9)
    global_var.paddle.set_thru(0)
    global_var.paddle.set_grab(0)
    global_var.paddle.set_laser(0)

