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
rows = 20
paddle = [['_','_','_','_','_','_']]
#ball = [['*']]
ball = [[Back.BLACK+ '*']]
#ball = np.full((1,1), Fore.RED + "*" + Fore.RESET )
paddle = np.full((1,9),Back.GREEN+'_' )
brick = np.full((1,5),' ')
powerup = [['x']]