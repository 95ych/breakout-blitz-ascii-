import game_screen
import objects
import config
import random
import utilities
mp = game_screen.Map()
level = 1
pause = 0
breakable_bricks = [8,10,15]
balls = []
bricks = []
powers = []
power_ups = []
paddle = objects.Paddle(config.paddle, 5, config.rows -3)
ball = objects.Ball(config.ball, 5 + random.randint(paddle.get_width(),paddle.get_width()), config.rows -4,1,0,1)
balls.append(ball)