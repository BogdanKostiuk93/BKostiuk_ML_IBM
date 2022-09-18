#throws predominantly scissors - 6/8 times (1/8 times either rock or paper)
import random

def predominantly_scissors_agent():
    choice_list = [0,1,2,2,2,2,2,2]
    return random.choice(choice_list)
