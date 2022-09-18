#throws predominantly rock - 6/8 times (1/8 times either paper or scissors)
import random

def predominantly_rock_agent():
    choice_list = [0,0,0,0,0,0,1,2]
    return random.choice(choice_list)
