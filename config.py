import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style
# import objects
from math import pi
import numpy as np 

MAXY_SPEED =1
MAXX_SPEED = 1
columns = 80
rows = 20
paddle = [['_','_','_','_','_','_']]
#ball = [['*']]
ball = [[Back.BLACK+ '*']]
#ball = np.full((1,1), Fore.RED + "*" + Fore.RESET )
paddle = np.full((1,9),Back.BLACK+'_' )
brick = np.full((1,5),' ')
brick1 = np.full((1,5),Back.RED +' ')
brick2 = np.full((1,5),Back.RED +' ')
brick3 = np.full((1,5),Back.RED +' ')