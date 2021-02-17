import global_var 
import utilities
import config
from time import time,sleep
import random
from colorama import Fore,Back,Style

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
                if global_var.mp.matrix[j+self._posy][i+self._posx] == " ":
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]


    def xget(self):
        return self._posx

    def yget(self):
        return self._posy
    
    def xset(self, x):
        self._posx = x
    
    def yset(self, x):
        self._posy = x

    def xmove(self, x):
        self._posx += x
    
    def ymove(self, x):
        self._posy += x

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx] = " "

class Paddle(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self.__bullet_speed = 3
        self.__lives = 5
        self.__bullet_time = 0
    
    def get_width(self):
        return self._width

    def get_height(self):
        return self._height
        
    def render(self):
        for i in range(self._width):
            for j in range(self._height):
                if global_var.mp.matrix[j+self._posy][i+self._posx] == " ":
                    global_var.mp.matrix[j+self._posy][i+self._posx] = self._shape[j][i]

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+self._posy][i+self._posx] = " "
    
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
