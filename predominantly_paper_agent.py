#throws predominantly paper - 6/8 times (1/8 times either rock or scissors)
import random

def predominantly_paper_agent():
    choice_list = [0,1,1,1,1,1,1,2]
    return random.choice(choice_list)
