import global_var 
import utilities
import config
from time import time,sleep
import random
from colorama import Fore,Back,Style
from numpy import inf, full

class Object():
    
    def __init__(self, character, x, y):
        self._posx = x
        self._posy = y
        self._xspeed = 0
        self._yspeed = 0
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
    
    def get_width(self):
        return self._width
    
    def get_height(self):
        return self._height

    def xset(self, x):
        self._posx = x
    
    def yset(self, x):
        self._posy = x

    def xmove(self, x):
        self._posx = x+self._posx
    
    def ymove(self, x):
        self._posy = x+ self._posy

    def xgetspeed(self):
        return self._xspeed
    
    def ygetspeed(self):
        return self._yspeed

    def clear(self):
        for i in range(self._width):
            for j in range(self._height):
                global_var.mp.matrix[j+int(self._posy)][i+int(self._posx)] = Back.BLACK + " "

class Paddle(Object):

    def __init__(self, character ,x, y):
        super().__init__(character, x, y)
        self._score = 0
        self._lives = 3
        self._grab = 0
        self._breakthru =0
    def get_width(self):
        return self._width

    def set_width(self,x):
        self.clear()
        self._shape =  full((1,x),Back.GREEN +'_' )
        self._width = x
    
    def expand(self):
        self.set_width(15 if self._width > 5 else 9)
    
    def shrink(self):
        self.set_width(5 if self._width < 15 else 9)
    
    def inc_score(self,x):
        self._score += x
    
    def inc_lives(self,x):
        self._lives += x

    def set_grab(self,x):
        self._grab=x

    def get_grab(self):
        return self._grab
    
    def set_thru(self,x):
        self._breakthru=x

    def get_thru(self):
        return self._breakthru
    def get_lives(self):
        return self._lives

class Ball(Object):

    def __init__(self, character ,x, y,grab,xspeed,yspeed):
        super().__init__(character, x, y)
        self._xspeed = xspeed
        self._yspeed = yspeed
        self.paddle_grab = grab
        self._x_on_paddle = int(global_var.paddle.get_width()/2)

    def check_collision(self):
        if self._posy >= 18:
            self.clear()
            if len(global_var.balls) == 1:    
                self.xset(global_var.paddle.xget() + int(global_var.paddle.get_width()/2))
                self.yset(global_var.paddle.yget()-1)
                self.paddle_grab=1
                global_var.paddle.inc_lives(-1)
            else:
                global_var.balls.remove(self)
                utilities.default()
        if self._posy <= 0:
            self._yspeed = -self._yspeed
        if global_var.mp.matrix[int(self._posy)+1][int(self._posx)] == config.paddle[0][0]:
            if self.paddle_grab ==1:
                pass

            elif global_var.paddle.get_grab() == 1 and self.paddle_grab==0 and self._yspeed > 0:
                self._x_on_paddle = self._posx - global_var.paddle._posx
                self.paddle_grab = 1
                self._yspeed = -self._yspeed
            else: 
                if global_var.paddle.get_grab() == 0 and self._yspeed >0 : 
                    self._yspeed = -self._yspeed
                self._xspeed = self._xspeed + (self._posx - global_var.paddle._posx - int(global_var.paddle.get_width()/2))*0.3
                if self._xspeed > config.MAXX_SPEED :
                    self._xspeed = config.MAXX_SPEED
                elif self._xspeed < -config.MAXX_SPEED :
                    self._xspeed = -config.MAXX_SPEED  
        if self._posx < global_var.mp.start_index + 1:
            self._xspeed = -self._xspeed
        if self._posx > global_var.mp.start_index + config.columns-1:
            self._xspeed = -self._xspeed
    
    def inc_speed(self):
        self._xspeed = config.MAXX_SPEED if self._xspeed > 0 else -config.MAXX_SPEED  
        self._yspeed = config.MAXY_SPEED if self._yspeed > 0 else -config.MAXY_SPEED
    def yreflect(self):
        self._yspeed = - self._yspeed
    def xreflect(self):
        self._xspeed = - self._xspeed
    def get_x_on_paddle(self):
        return self._x_on_paddle


class Brick(Object):

    def __init__(self, character ,x, y, lives):
        super().__init__(character, x, y)
        #self.powerup = random.choice([0,0,0,0,0,0,0,0,0,0,1,2,2,2,4,4,5,5,3,6,6])
        self.powerup = random.choice([3])
        self._lives = lives
    def inc_lives(self,x):
        self._lives+=x
    def get_lives(self):
        return self._lives
    def set_lives(self,x):
        self._lives = x

    
    def render(self):    
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
            global_var.paddle.inc_score(1)
            global_var.bricks.remove(self)
        elif self._lives < 0:
            self.clear()
            global_var.bricks.remove(self)
        
    def check_collision(self):
        if self._lives>=0:
            for ball in global_var.balls:
                ball_x = int(ball.xget())
                ball_y = int(ball.yget())
                for i in range(-1,2):
                    if ( (self._posy+i,self._posx-1) == (ball_y,ball_x) and ball._xspeed >0): 
                        if global_var.paddle.get_thru() ==0:
                            self._lives -= 1
                            global_var.paddle._score+=1
                            ball.xreflect()
                        else:
                            global_var.paddle._score+= self._lives if self._lives < 4 else 5
                            self._lives =0
                        
                        if self._lives==0:
                            utilities.drop_power_up(self.powerup,self._posy+i,self._posx-1)
                        
                    if  ((self._posy+i,self._posx+self._width) == (ball_y,ball_x) and ball._xspeed <0): 
                        if global_var.paddle.get_thru() ==0:
                            self._lives -= 1
                            ball.xreflect()
                        else:
                            global_var.paddle._score+= self._lives if self._lives < 4 else 5
                            self._lives =0
                        if self._lives==0:
                            utilities.drop_power_up(self.powerup,self._posy+i,self._posx+self._width)    
                
                for i in range(self._width):
                    #if global_var.mp.matrix[self._posy][i+self._posx] == ball[0][0]:
                    if (self._posy+1,i+self._posx) == (ball_y,ball_x) or (self._posy-1,i+self._posx) == (ball_y,ball_x):
                        if global_var.paddle.get_thru() ==0:
                            self._lives -= 1
                            ball.yreflect() 
                        else:
                            global_var.paddle.inc_score(self._lives if self._lives < 4 else 5)
                            self._lives =0
                        if self._lives==0:
                            utilities.drop_power_up(self.powerup,self._posy,self._posx+i)
            
class PowerUp(Object):

    def __init__(self, character ,x, y, power):
        super().__init__(character, x, y)
        self._yspeed = 1
        self._power = power        
    
    def render(self):    
        if self._power == 1:
            for i in range(self._width):
                global_var.mp.matrix[int(self._posy)][i+int(self._posx)] = Back.BLACK + 'E'
        elif self._power == 2:
            for i in range(self._width):
                global_var.mp.matrix[int(self._posy)][i+int(self._posx)] = Back.BLACK + 'S'
        elif self._power == 3:
            for i in range(self._width):
                global_var.mp.matrix[int(self._posy)][i+int(self._posx)] = Back.BLACK + 'B'
        elif self._power == 4:
            for i in range(self._width):
                global_var.mp.matrix[int(self._posy)][i+int(self._posx)] = Back.BLACK + 'F'
        elif self._power == 5:
            for i in range(self._width):
                global_var.mp.matrix[int(self._posy)][i+int(self._posx)] = Back.BLACK + 'T'
        elif self._power == 6:
            for i in range(self._width):
                global_var.mp.matrix[int(self._posy)][i+int(self._posx)] = Back.BLACK + 'G'

    def check_collision(self):
        if global_var.mp.matrix[int(self._posy)+1][int(self._posx)] == config.paddle[0][0]:
            utilities.add_powers(self._power)
            self.clear()
            global_var.power_ups.remove(self)
        
        elif self._posy >= 17:
            self.clear()
            global_var.power_ups.remove(self)