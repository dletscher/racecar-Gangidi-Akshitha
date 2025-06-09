import random
import math

class Agent:
    def chooseAction(self, observations, possibleActions):
        lidar = observations['lidar']
        velocity = observations['velocity']

        
        lidar = [d if math.isfinite(d) else 10.0 for d in lidar]
        left, fleft, front, fright, right = lidar

        
        if front < 0.7:
            if fleft < fright:
                direction = 'right'
            else:
                direction = 'left'
        elif fright < 0.4:
            direction = 'left'
        elif fleft < 0.4:
            direction = 'right'
        elif right > left + 0.5:
            direction = 'right'
        elif left > right + 0.5:
            direction = 'left'
        else:
            direction = 'straight'

        
        if front < 0.6 or fleft < 0.3 or fright < 0.3:
            motion = 'brake'
        elif velocity < 0.2 and front > 1.0:
            motion = 'accelerate'
        else:
            motion = 'coast'

        action = (direction, motion)

        if action not in possibleActions:
            action = random.choice(possibleActions)

        return action