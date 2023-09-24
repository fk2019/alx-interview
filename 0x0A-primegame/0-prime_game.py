#!/usr/bin/python3
"""Is winner method"""


def isWinner(x, nums):
    """Determine who is winner"""
    def is_prime(num):
        """is prime method"""
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num**0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def play_game(n):
        """play game method"""
        if n <= 1:
            return "Ben"  # Ben wins if n is 0 or 1
        elif n % 2 == 0:
            return "Maria"  # Maria wins if n is even

        return "Ben"  # Otherwise, Ben wins

    winners = []

    for n in nums:
        winners.append(play_game(n))

    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
