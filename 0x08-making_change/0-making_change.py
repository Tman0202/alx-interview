#!/usr/bin/python3
"""
Change comes from within
"""


def makeChange(coins, total):
    """
    Return: fewest number of coins needed to meet total
        If total is 0 or less, return 0
        If total cannot be met by any
        number of coins you have, return -1
    coins is a list of the values of the coins in your possession
    """
    if total <= 0:
        # checks for invalid total amount
        return 0
    if coins == []:
        # checks for empty coins list
        return -1
    coins = sorted(coins, reverse=True) # sort and reverse the coins list
    max = coins[0] # get the largest coin value
    x = 0 # loop variable
    coins.pop(0) # remove biggest coin from coins list
    length = len(coins)
    rem = total % max # check if the biggest coin is a change
    if rem == 0:
        # if it is a change then return the total number
        # of biggest coins that will make up the change
        return total / max
    
    # if biggest coin cannot make a complete change
    # scan the coins list for the next possible coin that will make change
    quot = total // max # total possible number of biggest coin needed 
    while x < length:
        remc = rem % coins[x] # store remainder for each coin
        if remc == 0: # if coin makes up complete change
            return quot + (rem // coins[x])
        if x == length - 1:
            # if unable to make complete change after scanning
            return -1
        quotc = rem // coins[x] # total number of each coin needed
        rem = remc # update what's left of total change
        quot += quotc # update total number of coins needed
        x += 1
    return quot
