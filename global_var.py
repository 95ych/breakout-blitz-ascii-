import game_screen
import objects
import config
import random
import utilities
mp = game_screen.Map()
level = 1
pause = 0
breakable_bricks = [[1,5],[2,10],[3,15]]
balls = []
bricks = []
powers = []
power_ups = []
paddle = objects.Paddle(config.paddle, 5, config.rows -5)
ball = objects.Ball(config.ball, 5 + int(paddle.get_width()/2), config.rows -6,1,0,1)
balls.append(ball)