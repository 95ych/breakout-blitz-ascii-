import game_screen
import objects
import config

mp = game_screen.Map()
bricks = []
paddle = objects.Paddle(config.paddle, 5, config.rows -5)
ball = objects.Ball(config.ball, 5, config.rows -6)
for i in range(5):
    bricks.append(objects.Brick(config.brick,i*6+5,10))