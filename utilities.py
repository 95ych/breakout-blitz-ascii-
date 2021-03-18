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

def brick_gen(level):
    if level==1:
        for i in range(8):
            global_var.bricks.append(objects.Brick(config.brick,i*7+7,10,random.randint(1,3)))
        for i in range(9):
            global_var.bricks.append(objects.Brick(config.brick,i*7+3,8,random.randint(1,3)))
        global_var.bricks.append(objects.Brick(config.brick,10,5,inf))
        for i in range(5):
            global_var.bricks.append(objects.Brick(config.brick,i*7+17,5,random.randint(1,3)))
        global_var.bricks.append(objects.Brick(config.brick,5*7+17,5,inf))


def drop_power_up(power, y, x):
    global_var.power_ups.append(objects.PowerUp(config.powerup,x,y, power))

def add_powers(power):
    flag =0
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
        global_var.powers.append([power, time()])


def check_powers():
    for i in global_var.powers:
        print(i[0])
        if time() - i[1] > config.POWER_TIME:
            if i[0] == 1 or i[0] == 2:
                global_var.paddle.set_width(9)
            if i[0] == 3:
                pass
            if i[0] == 5:
                global_var.paddle.set_thru(0)
            if i[0] == 6:
                global_var.paddle.set_grab(0)
            
            global_var.powers.remove(i)

def default():
    global_var.powers = []
    if global_var.paddle.get_width()!=9:
        global_var.paddle.set_width(9)
    global_var.paddle.set_thru(0)
    global_var.paddle.set_grab(0)