import config
import random
import os
import global_var
from colorama import init, Fore, Back, Style
import objects
from time import time


def create_header():
    print("\033[2;1H" + Fore.WHITE + Back.BLUE + Style.BRIGHT)
    print(Style.RESET_ALL)

def print_board():
    create_header()
    global_var.mp.render()

def display_ending(message):
    os.system('tput reset')
   

def create_board():

    i = 1
    x = 10

    
    while x < global_var.mp.width - 250:

        no = random.randint(0, 3)
        y = random.randint(10, global_var.mp.height-15)
        
        # #beams
        # enemy = objects.Object(config.enemy[no], x, y)
        # global_var.beams.append(enemy)
        # enemy.render()
        
        # #dragon power up
        # if i % 10 == 0:
        #     dg_pow_up = objects.Object(config.dg_pow_up, x + 15 , y)
        #     global_var.dg_power_up.append(dg_pow_up)
        #     dg_pow_up.render()

        # #magnets
        # elif i % 5 == 0:
        #     magnet = objects.Object(config.magnet, x + 10 , y)
        #     global_var.magnets.append(magnet)
        #     magnet.render()
        
        # i += 1
        # x += random.randint(20, 30)
        # if x > global_var.mp.width - 250:
        #     break
            
        # y = random.randint(10, global_var.mp.height-15)

        # #coins
        # coin = objects.Object(config.coins, x, y)
        # global_var.coins.append(coin)
        # coin.render()


        # x += random.randint(20, 30)
        # y = random.randint(10, global_var.mp.height-15)
        
        # #boost
        # boost = objects.Object(config.boost, x, y)
        # global_var.boosts.append(boost)
        # boost.render()

        # x += random.randint(20, 50)

def initialize_board():
    global_var.paddle.render()
    print_board()