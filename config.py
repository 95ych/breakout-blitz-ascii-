import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style
# import objects
from math import pi
import numpy as np
TIME_ATTACK = 3
GRAVITY = 0.3
DAMP = 0.5
MAXY_SPEED = 1
MAXX_SPEED = 1
PADDLE_SPEED = 3
POWER_TIME = 3
columns = 70
rows = 26
#paddle = [['_','_','_','_','_','_']]
#ball = [['*']]
ball = [[Back.BLACK+ '*']]
#ball = np.full((1,1), Fore.RED + "*" + Fore.RESET )

ufo = [[Back.BLACK+' ',Back.BLACK+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.CYAN+' ',Back.BLACK+' ',Back.BLACK+' '],
        [Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' ',Back.GREEN+' '],
        [Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+'V',Back.BLACK+'V',Back.BLACK+' ',Back.BLACK+' ',Back.BLACK+' '] ]
shoot_time = 0.2
bomb = [[Fore.RED+'x']]
paddle = np.full((1,9),Back.GREEN+'_' )

brick = np.full((1,5),' ')
prob_distr = [0,0,0,0,0,0,0,0,0,0,1,2,2,2,4,4,5,5,3,6,6]
powerup = [['x']]