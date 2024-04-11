import math

def coin_change_bottom_up(coins, amount):

    min_coins =  [math.inf] * (amount +1)
    min_coins[0] =  0

    for val in range(1, amount+1):
        for c in coins:
            if c <= val:
                min_coins[val] = min(min_coins[val], 1 + min_coins[val-c])

    if min_coins[amount] is math.inf:
        return -1
    else:
        return min_coins[amount]

def coin_change_top_down(coins, amount):

    min_coins_memo = [None]*(amount+1)
    min_coins = coin_change_memo(coins, amount, min_coins_memo)

    if min_coins is math.inf:
        return -1
    else:
        return min_coins

def coin_change_memo(coins, amount, memo):

    if amount == 0:
        return 0
    elif memo[amount] is None:
        min_coins = math.inf
        for c in coins:
            if c <= amount:
                min_coins = min(min_coins, 1 + coin_change_memo(coins, amount-c, memo))
        memo[amount] = min_coins
    return memo[amount]