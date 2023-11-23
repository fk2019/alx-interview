#!/usr/bin/python3
"""Change comes from within
"""
import sys


def makeChange(coins, total):
    """Return fewest number of coins needd to make toatl"""
    def minCoins(total):
        """Recursive call for sub problems"""
        if total == 0:
            return 0
        if dp[total] != -1:
            return dp[total]
        res = sys.maxsize
        for coin in coins:
            if coin <= total:
                sub_res = minCoins(total - coin)
                if sub_res != sys.maxsize and sub_res + 1 < res:
                    res = sub_res + 1
        dp[total] = res
        return res
    dp = [-1] * (total + 1)
    result = minCoins(total)
    return result if result != sys.maxsize else -1
