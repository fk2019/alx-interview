#!/usr/bin/python3
"""Prime game"""


def isWinner(x, nums):
    """isWinner method"""
    def play_game(n):
        """Play game"""
        if n <= 1:
            return "Ben"
        elif n % 2 == 0:
            return "Maria"

        return "Ben"

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
