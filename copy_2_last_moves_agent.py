#randomly selects a figure from two of his opponents last throws
import random
saved_obs = {'last':None,'before_last':None }

def copy_2_last_moves(observation, configuration):
    global saved_obs
    
    if observation.step == 1:
        saved_obs['before_last'] = observation.lastOpponentAction
        return random.randrange(0, configuration.signs)

    elif observation.step > 1:
        if observation.step % 2 == 0:
            saved_obs['last'] = observation.lastOpponentAction
        else:
            saved_obs['before_last'] = observation.lastOpponentAction
        return random.choice(list(saved_obs.values()))
    
    #initial step
    else:
        return random.randrange(0, configuration.signs)
