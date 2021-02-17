import config
import random
from colorama import init, Fore, Back, Style
import numpy as np
import global_var

class Map(object):

    height = int(config.rows) 
    width = int(config.columns*8)

    def __init__(self):
        self.start_index = 0
        self.matrix = np.array([[" " for i in range(self.width)] for j in range(self.height)])

    def render(self):
        for y in range(3, self.height):
            pr = []
            for x in range(self.start_index, self.start_index + config.columns):
                if y == 3:
                    pr.append(Fore.LIGHTCYAN_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))

                elif y == self.height - 1:
                    pr.append(Fore.LIGHTMAGENTA_EX + Style.BRIGHT+(self.matrix[y][x] + Style.RESET_ALL))
                
                else:
                    pr.append(self.matrix[y][x] + Style.RESET_ALL)
            print(''.join(pr))