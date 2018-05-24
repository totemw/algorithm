"""
Move the blocks on tower1 to tower3.
"""


def moveDisks(n, origin, destination, buffer):
    if n <= 0:
        return
    moveDisks(n - 1, origin, buffer, destination)
    moveTop(origin, destination)
    moveDisks(n - 1, buffer, destination, origin)