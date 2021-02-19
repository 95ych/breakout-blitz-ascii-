import os
import sys
import termios, tty, time
from colorama import init, Fore, Back, Style
# import objects
from math import pi
import numpy as np 

columns = 80
rows = 20
paddle = [['_','_','_','_','_','_']]
ball = [['*']]
#ball = np.full((1,1),Fore.RED + '*' + Fore.RESET)
brick = np.full((1,5),'I')