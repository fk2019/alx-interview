#!/usr/bin/python3
"""Return minimum number of coins needed to for a given total
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    change_list = [float('inf')] * (total + 1)
    change_list[0] = 0

    for coin in coins:
        for amount in range(coin, total + 1):
            change_list[amount] = min(change_list[amount],
                                      change_list[amount - coin] + 1)

    if change_list[total] == float('inf'):
        return -1
    else:
        return change_list[total]
