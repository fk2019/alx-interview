#!/usr/bin/python3
"""Determine the winner"""


def check_prime(n):
    """Check for prime n"""
    for i in range(2, int(n ** 0.5) + 1):
        if not n % i:
            return False
    return True


def add_prime(n, primes):
    """Add prime"""
    last_prime = primes[-1]
    if n > last_prime:
        for i in range(last_prime + 1, n + 1):
            if check_prime(i):
                primes.append(i)
            else:
                primes.append(0)


def isWinner(x, nums):
    """Checks for winner"""
    score = {"Maria": 0, "Ben": 0}
    primes = [0, 0, 2]
    add_prime(max(nums), primes)
    for round in range(x):
        _sum = sum((i != 0 and i <= nums[round])
                   for i in primes[:nums[round] + 1])
        if (_sum % 2):
            winner = "Maria"
        else:
            winner = "Ben"
        if winner:
            score[winner] += 1

    if score["Maria"] > score["Ben"]:
        return "Maria"
    elif score["Ben"] > score["Maria"]:
        return "Ben"
    return None
