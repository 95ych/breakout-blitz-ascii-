import game_screen
import objects
import config
import random
from numpy import inf
mp = game_screen.Map()
bricks = []
paddle = objects.Paddle(config.paddle, 5, config.rows -5)
ball = objects.Ball(config.ball, 1, config.rows -6)
for i in range(5):
    pass
    #bricks.append(objects.Brick(config.brick,i*6+5,10,random.randint(1,3)))
bricks.append(objects.Brick(config.brick,4,config.rows -9,2))