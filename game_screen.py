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
        #self.matrix = np.array([[" " for i in range(self.width)] for j in range(self.height)])
        self.matrix = np.full((self.height, self.width),Back.BLACK+ " ")
        
    def render(self):
        for y in range(self.height):
            pr = [Back.WHITE+ " "]*2
            for x in range(self.start_index, self.start_index + config.columns):
                
                pr.append(self.matrix[y][x] + Style.RESET_ALL)
            print(''.join(pr))