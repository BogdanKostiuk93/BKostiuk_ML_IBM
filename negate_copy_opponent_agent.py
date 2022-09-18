#throws any move at random except for the last move of the opponent
import random
def negate_copy_opponent_agent(observation, configuration):
    #in case we have information about opponent last move
    if observation.step > 0:
        result = random.randrange(0,3)
        while result == observation.lastOpponentAction:
            result = random.randrange(0,3)
        return result
    #initial step
    else:
        return random.randrange(0, configuration.signs)
