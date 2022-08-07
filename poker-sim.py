# n-coin poker:
#
# A and B each toss n coins, and the dealer tosses n/2 coins: A and B then place 
# their bets on whether the dealer will have more/less heads than them, then all 
# the coins are tossed without further betting rounds
# 
# 1. As A, how much should you bet? B can view A's bets
# 2. As B, how much should you bet, given A's bets
#
# In more detail, cases that can arise are:
# 1. A < D < B: B wins pot
# 2. D < A < B: pot splits
# 3. B < D < A: A wins pot
# 4. D < B < A: pot splits
# 5. A < B < D: pot splits
# 6. B < A < D: pot splits
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
    return binom.rvs(n,0.5)

def iter(A_init_purse, B_init_purse, num_coins, N):
    # run N iterations of the simulation, and return a timeseries of A's and B's 
    # purses
    A_purse = [A_init_purse]
    B_purse = [B_init_purse]
    for i in range(N):
        
        A_flips = sim_flips(num_coins)
        B_flips = sim_flips(num_coins)
        dealer_flips = sim_flips(num_coins//2)

        A_bet = A_strat(num_coins, A_flips, dealer_flips, A_purse[-1])
        B_bet = B_strat(num_coins, B_flips, dealer_flips, B_purse[-1], A_bet)

        dealer_rem_flips = sim_flips(num_coins//2)

        dealer_tot_flips = dealer_flips + dealer_rem_flips

        if (B_flips < dealer_tot_flips < A_flips):
            A_purse.append(A_purse[-1] + B_bet)
            B_purse.append(B_purse[-1] - B_bet)
        elif (A_flips < dealer_tot_flips < B_flips):
            A_purse.append(A_purse[-1] - A_bet)
            B_purse.append(B_purse[-1] + A_bet)
        else:
            A_purse.append(A_purse[-1] - A_bet/2 + B_bet/2)
            B_purse.append(B_purse[-1] - B_bet/2 + A_bet/2)

        if (A_purse[-1] == 0 or B_purse[-1] == 0):
            break

    if (A_purse[-1] > B_purse[-1]):
        return (A_purse, B_purse, 'A')
    else:
        return (A_purse, B_purse, 'B')
    
def A_strat(num_coins, A_coins, dealer_coins, A_purse):
    # say A makes binary (all or nothing bets) with a limit of 50%
    limit = 0.5

    if (binom.sf(dealer_coins,num_coins//2,0.5) < limit):
        return A_purse
    return 0

def B_strat(num_coins, B_coins, dealer_coins, B_purse, pot):
    # say B makes spaced-out decisions, linear in probability
    limit = 0.5
    if (binom.sf(dealer_coins,num_coins//2,0.5) < limit and pot == 0):
        return B_purse #*(limit - binom.sf(dealer_coins,num_coins//2,0.5))/limit

    return 0

if __name__ == "__main__":
    winctr = 0
    n_games = 100
    A_init_purse = 20
    B_init_purse = 20
    max_iter = 100
    num_coins = 50
    for i in range(n_games):
        (ts_a, ts_b, winner) = iter(A_init_purse, B_init_purse, num_coins, max_iter)
        if (winner == 'A'):
            winctr += 1
        plt.plot(ts_a, alpha=0.1, color='red')
        plt.plot(ts_b, alpha=0.1, color='blue')

    print(f"A won {winctr} times, B won {n_games-winctr} times")
    
    plt.plot([],[], 'r', label='A')
    plt.plot([],[], 'b', label='B')
    plt.xlabel("games")
    plt.ylabel("purses")
    plt.title(f"A = {winctr} wins, B = {n_games-winctr} wins")
    plt.legend()
    plt.show()
