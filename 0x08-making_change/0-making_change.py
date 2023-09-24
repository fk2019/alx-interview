#!/usr/bin/python3
"""change comes from within"""


def makeChange(coins, total):
    if total <= 0:
        return 0
    # Initialize an array to store the minimum number of coins needed
    dp = [float('inf')] * (total + 1)
    # Base case: 0 coins are needed to make a total of 0
    dp[0] = 0
    # Calculate the min number of coins for each total from 1 to given total
    for i in range(1, total + 1):
        for coin in coins:
            if i >= coin:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    # If dp[total] is still infinite, it means the total cannot be met
    if dp[total] == float('inf'):
        return -1

    return dp[total]
