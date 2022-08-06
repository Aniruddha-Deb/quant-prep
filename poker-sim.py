# n-coin poker:
#
# A and B each toss n coins, and the dealer tosses n/2 coins: A and B then place 
# their bets on whether the dealer will have more/less heads than them, then all 
# the coins are tossed without further betting rounds
# 
# 1. As A, how much should you bet? B can view A's bets
# 2. As B, how much should you bet, given A's bets
#
# Repeat for two, three betting rounds rather than just one

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

def sim_flips(n):
    # return an array of n coin flips
    # ? should I return an array of coin flips, or just sample from scipy's 
    # binom distribution....
    # yeah, latter is faster + easier
    # but don't know how to do it :'(
    rv = binom(n,0.5)
    return rv

def iter(A_init_purse, B_init_purse, num_coins, N):
    # run N iterations of the simulation, and return a timeseries of A's and B's 
    # purses
    for i in range(N):
        
        A_flips = sim_flips(num_coins)
        B_flips = sim_flips(num_coins)
        dealer_flips = sim_flips(num_coins//2)

        A_bet = A_strat(A_flips, dealer_flips, A_init_purse)
        B_bet = B_strat(B_flips, dealer_flips, B_init_purse, A_bet)

        dealer_rem_flips = sim_flips(num_coins//2)


    return ([A_init_purse]*N, [B_init_purse]*N)
    
def A_strat(A_coins, dealer_coins, A_purse):
    pass

def B_strat(B_coins, dealer_coins, B_purse, pot):
    pass

if __name__ == "__main__":
    (ts_a, ts_b) = iter(20, 10, 10, 100)
    plt.plot(ts_a)
    plt.plot(ts_b)
    plt.show()
