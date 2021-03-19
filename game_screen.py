import config
import random
from colorama import init, Fore, Back, Style
import numpy as np
import global_var
import time
class Map(object):

    height = int(config.rows) 
    width = int(config.columns*8)

    def __init__(self):
        self.start_index = 0
        #self.matrix = np.array([[" " for i in range(self.width)] for j in range(self.height)])
        self.matrix = np.full((self.height, self.width),Back.BLACK+ " ")
        self.timestart = time.time()

    def render(self):
        print("Time :" + str(int(time.time() - self.timestart))+" "*12+"Lives: "+str(global_var.paddle._lives)+" "*12+"Level: "+str(global_var.level)+" "*12 +"Score: " + str(global_var.paddle._score) )
        for boss in global_var.bosses:
            h = boss.get_health()
            print("Boss :"+"["+(Back.GREEN+' ')*h +(Back.BLACK+' ')*(50-h)+Back.BLACK+"]")
        print(Back.WHITE+" "*(config.columns+2)+ Back.RESET)
        for y in range(self.height):
            pr = [Back.WHITE+ " "+Back.RESET]
            for x in range(self.start_index, self.start_index + config.columns):    
                pr.append(self.matrix[y][x] + Style.RESET_ALL)
            pr.append(Back.WHITE+ " "+Back.RESET)
            print(''.join(pr))
    
    def get_start_time(self):
        return self.timestart
