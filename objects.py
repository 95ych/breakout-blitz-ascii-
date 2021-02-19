import global_var 
import utilities
import config
from time import time,sleep
import random
from colorama import Fore,Back,Style
from numpy import inf
class Object():
    
    def __init__(self, character, x, y):
        self._posx = x
        self._posy = y
        self._width = len(character[0])
        self._height = len(character)
        self._shape = character

    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                if global_var.mp.matrix[j+int(self._posy)][i+int(self._posx)] == Back.BLACK + " ":
                    global_var.mp.matrix[j+int(self._posy)][i+int(self._posx)] = self._shape[j][i]

    def xget(self):
        return self._posx

    def yget(self):
        return self._posy
    
    def xset(self, x):
        self._posx = x
    
    def yset(self, x):
        self._posy = x

    def xmove(self, x):
        self._posx = x+self._posx
    
    def ymove(self, x):
        self._posy = x+ self._posy

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+int(self._posy)][i+int(self._posx)] = Back.BLACK + " "

class Paddle(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self._score = 0
        self._lives = 3
        self.__bullet_time = 0
    
    def get_width(self):
        return self._width
    
    # def print_lives(self):
    #     i = 10 - 2*self.__lives        
    #     while i > 0:
    #         self._shape[0][17-i] = " "
    #         i -= 1

    # def set_pos_to_mando(self, mando):
    #     if mando.yget() <= 36:
    #         self.ydset(mando.yget())
    #     else:
    #         self.ydset(36)  


    # def collision(self):
    #     self.__lives -= 1
    #     if self.__lives == 0:
    #         global_var.mando.inc_score(30)
    #         message = "You defeated the boss! You won!"
    #         global_funct.display_ending(message)
    #         quit()

    # def drag_bullets_move(self, dragon_bullets):
    #     i = 0
    #     no_bullets = len(dragon_bullets)

    #     while i < no_bullets:
    #         dragon_bullets[i].clear()
    #         if dragon_bullets[i].xget() >= global_var.mp.start_index:
    #             dragon_bullets[i].xset(-1)
    #             i += 1

    #         else:
    #             del(dragon_bullets[i])
    #             no_bullets -=1
        
    #     i = 0
    #     while i < no_bullets:
    #         dragon_bullets[i].render()
    #         i += 1

        
    # def bullet_col(self, bullets):
    #     i = 0
    #     no_bullets = len(bullets)

    #     while i < no_bullets:
    #         if bullets[i].check_drag_collision() == 1:
    #             # print(self.__lives)
    #             self.print_lives()
    #             bullets[i].clear()
    #             del(bullets[i])
    #             no_bullets -= 1
    #         else:
    #             i += 1

    # def throw_bullet(self, dragon_bullets):
    #     ycoord = random.randint(self._posy + 5 ,self._posy + 12)
    #     drag_bullet = Dragon_Bullet(["o"], self._posx -1, ycoord)
    #     drag_bullet.render()
    #     dragon_bullets.append(drag_bullet)
    #     self.set_bullet_time(time())

class Ball(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self._xspeed = 0.3
        self._yspeed = 1
    

    def check_collision(self):

        if self._posy >= 19:
            self._yspeed = -self._yspeed
            global_var.paddle._lives-=1
        if self._posy <= 0:
            self._yspeed = -self._yspeed
        if global_var.mp.matrix[int(self._posy)][int(self._posx)] == config.paddle[0][0]:
            self._yspeed = -self._yspeed
            self._xspeed = self._xspeed + (self._posx - global_var.paddle._posx - int(global_var.paddle.get_width()/2))*0.3
            if self._xspeed > config.MAXX_SPEED:
                self._xspeed = config.MAXX_SPEED 
        if self._posx < global_var.mp.start_index + 1:
            self._xspeed = -self._xspeed
        if self._posx > global_var.mp.start_index + config.columns-1:
            self._xspeed = -self._xspeed

class Brick(Object):

    def __init__(self, character ,x, y, lives):
        super().__init__(character, x, y)
        #self._xspeed = 0
        self._lives = lives
        #self._lives = 1    
    
    def renderex(self):    
        if self._lives == 3:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+int(self._posy)][i+int(self._posx)] = Back.RED + self._shape[j][i]
        elif self._lives == 2:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+int(self._posy)][i+int(self._posx)] = Back.MAGENTA + self._shape[j][i]
        elif self._lives == 1:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+int(self._posy)][i+int(self._posx)] = Back.YELLOW + self._shape[j][i]
        elif self._lives == inf:
            for i in range(self._width):
                for j in range(self._height):
                    global_var.mp.matrix[j+int(self._posy)][i+int(self._posx)] = Back.WHITE + self._shape[j][i]
        elif self._lives == 0:
            self.clear()
        
    def check_collision(self):
        if self._lives!=0:
            
            for i in range(-1,2):
                if (global_var.mp.matrix[self._posy+i][self._posx-1] == config.ball[0][0] and global_var.ball._xspeed >0) or (global_var.mp.matrix[self._posy+i][self._posx+self._width] == config.ball[0][0] and global_var.ball._xspeed <0): 
                    self._lives -= 1
                    global_var.paddle._score+=1
                    self.renderex()
                    global_var.ball._xspeed = -global_var.ball._xspeed
            
            for i in range(self._width):
                #if global_var.mp.matrix[self._posy][i+self._posx] == global_var.ball[0][0]:
                if global_var.mp.matrix[self._posy+1][i+self._posx] == config.ball[0][0] or global_var.mp.matrix[self._posy-1][i+self._posx] == config.ball[0][0]:
                    self._lives -= 1
                    global_var.paddle._score+=1
                    self.renderex()
                    global_var.ball._yspeed = -global_var.ball._yspeed
            
            
        