import game_screen
import objects
import config
import random
import utilities
from time import time
mp = game_screen.Map()
last_bomb = 0
cd = 1
level = 1
pause = 0
breakable_bricks = [11,12,15]
bosses = []
bombs = []
balls = []
bricks = []
powers = []
power_ups = []
paddle = objects.Paddle(config.paddle, 5, config.rows -3)
ball = objects.Ball(config.ball, 5 , config.rows -4,1,0,1)
balls.append(ball)