import math

def coin_change_bottom_up(coins, amount):

    min_coins =  [math.inf] * (amount +1)
    opt_coin = [None] * (amount +1)
    min_coins[0] =  0

    for val in range(1, amount+1):
        for c in coins: 
            # tries every coin and calculates the minimum number of coins needed to get amount
            # e.g. if we take c1, then coins needed is 1 + coins_needed for V-c1
            #      if we take c2, then coins needed is 1 + coins needed for V-c2
            #      we try all the possible coins and find the minimum
            if c <= val: 
                if 1 + min_coins[val-c] < min_coins[val]:
                    min_coins[val] = 1 + min_coins[val-c] 
                    opt_coin[val] = c # remembers the best/optimal coin to take at this amount for reconstruction
    
    coins_used = get_coins(amount, min_coins, opt_coin)
    
    if min_coins[amount] is math.inf:
        return -1, coins_used
    else:
        return min_coins[amount], coins_used

def coin_change_top_down(coins, amount):

    min_coins_memo = [None]*(amount+1)
    opt_coin = [None]*(amount+1)
    min_coins = coin_change_memo(coins, amount, min_coins_memo, opt_coin)

    coins_used = get_coins(amount, min_coins_memo, opt_coin)

    if min_coins is math.inf:
        return -1, coins_used
    else:
        return min_coins, coins_used

def coin_change_memo(coins, amount, memo, opt_coin):

    if amount == 0:
        return 0
    elif memo[amount] is None:
        min_coins = math.inf
        for c in coins:
            if c <= amount:
                new_coins = 1 + coin_change_memo(coins, amount-c, memo, opt_coin)
                if new_coins < min_coins:
                    min_coins = new_coins
                    opt_coin[amount] = c
        memo[amount] = min_coins
        
    return memo[amount]

def get_coins(amount, min_coins, opt_coin):
    if min_coins[amount] is math.inf:
        return -1

    coins_used = []
    while amount > 0:
        coins_used.append(opt_coin[amount])
        amount -= opt_coin[amount]
    
    return coins_used