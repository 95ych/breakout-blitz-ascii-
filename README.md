# breakout-blitz-ascii
Implemented a terminal based breakout blitz game  with OOPS concepts
This is an terminal-based arcade game designed in python3 using OOPS concepts.

## HOW TO RUN

python3 main.py

## CONTROLS

| Key   | Action |
| ----- | ------ |
| a     | left   |
| d     | right  |

## Game Objects

### - Paddle
Paddle is under player control, it is moved around to bounce the ball, and break the breaks and has to avoid falling the ball to the bottom , where it loses lives. 

### - Ball

The ball is used to break the bricks, it bounces off the rigid objects unless destroyed. It can bounce off the upper 3 walls, but once it falls down missing the paddle, player loses a life.

### - Bricks

There are 4 different bricks, each with different strengths , white ones are unbreakable, yellow ones are the weakest followed by magenta and then red.


### - powerups

Following are the powerups implemented

| Powerup Name | Look | Functionality                              |
| ------------ | ---- | ------------------------------------------ |
| Expand       | E    | Expands the paddle              |
| Shrink       | S    |    Shrinks  the paddle                |
| Ball multiplier| B    | Ball divides into 2                |
| Thru-ball       | T    | Ball breaks through any brick |
| Paddle grab   | G   | Enables the paddle to the grab the ball                           |

## THE CODE

The classes used can be found in objects.py. 
The Global variable aka game_objects are in global_var.py.
Game Settings can found in config.py.
Input settings are in setting.py
The main game loop is in main.py
utility functions for are found in utilities.py