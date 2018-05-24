"""
How likely is it that ants on a polygon will run into each other if they
walk at constant speed but start in a random direction.

no collision: clockwise or counter clockwise
"""


def artsOnPloygon(n):
    return 1 - 0.5 ** (n - 1)
