# Joker:
# 
# From an Optiver one-on-one
# Suppose there are 11 cards face-down on a table. Ten of them have the number 
# two written on them, while one has 1/2048 (2^-11) on it, called the Joker. You start with a 
# bankroll of 1000, and on picking a card, your bankroll is multiplied by the 
# number on the card. Devise an optimal strategy to play the game.
#
# The strategy I came up with involved picking the first 5 cards, then stopping.
# If we pick the joker, pick all the cards.
#
# The EV for this is 500*5/11 + 32000*6/11 = 3000+160000/11 = 163000/11 ~ 14800 sth.
# ? is this the maximum EV
# I don't think so...
# 
# 
# This gi

def simulate():
    
    n = np.random.randint(1,12)
    purse = 1000
    if n > 6:
        return 
    for i in range(1,6):
        if n != i:
            purse *= 2
        else:
            return 500

    return purse





def get_
