from utils.input_utils import *
from universe.character import *

def introduction():
    pass

def create_character():
    pass

def receive_letter():
    pass

def meet_hagrid(character):
    choice = ask_choice("Hagrid: 'Hello {}! I’m here to help you with your shopping on Diagon Alley.\n\n\
          Do you want to follow Hagrid?".format(character['First Name']), [1, 2])
    if choice == 2:
        print("Hagrid gently insists and takes you along anyway!")
    else:
        print("You follow Hagrid to Diagon Alley!")

def buy_supplies(character):
    pass

def start_chapter_1():
    pass

#################
##### Tests #####
#################
'''
Harry = init_character("Potter", "Harry", {"Courage": 8, "Intelligence": 8, "Loyalty": 8, "Ambition": 8})
meet_hagrid(Harry)
'''