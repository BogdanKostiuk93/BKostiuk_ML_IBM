#cycles rock-paper-scissors
counter = 0

def cycle_agent(observation, configuration):
    #shift steps by one
    global counter
    step = observation.step

    if step == counter:
        return 0
    if step == counter + 1:
        return 1
    elif step == counter + 2:
        counter = step + 1
        return 2
