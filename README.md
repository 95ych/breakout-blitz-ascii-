# breakout-blitz-ascii
 A terminal-based arcade game designed in python3 using OOPS concepts.



## HOW TO RUN

```bash
foo@bar$./python3 main.py
```



#### Instructions

Destroy the bricks and make your way to the final boss.

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


### - Powerups

Following are the powerups implemented

| Powerup Name | Look | Functionality                              |
| ------------ | ---- | ------------------------------------------ |
| Expand       | E    | Expands the paddle              |
| Shrink       | S    |    Shrinks  the paddle                |
| Ball multiplier| B    | Ball divides into 2                |
| Thru-ball       | T    | Ball breaks through any brick |
| Paddle grab   | G   | Enables the paddle to the grab the ball |
| Lasers |  L   |Enables the paddle to shoot lasers continously |

### - Enemy Boss

Enemy boss appears in the final level in a UFO, level 3, he isnt as bad as you think :') ,but he creepily keeps following you :(, he attacks when he gets hurt by the ball or when or you change ur movement direction  alerting suspiciousness. The UFO has some weak points, the glass and the boosters, which cause extra damage. So he gets really mad and starts firing furiously when you send the ball over his head. He attacks by dropping bombs. The UFO can  activate a barrier upto 2 times , after getting enough damage.

## Code

The classes used can be found in objects.py. 
The game objects are in global_var.py.
Game Settings can found in config.py.
Input settings are in inputs.py
The main game loop is in main.py
utility functions for are found in utilities.py