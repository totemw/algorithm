"""
Fill in the region containing the point with the given color
"""


def paintFill(screen, r, c, old, new):
    if r < 0 or r >= len(screen) or c < 0 or c >= len(screen[0]):
        return False
    if screen[r][c] == old:
        screen[r][c] = new
        paintFill(screen, r - 1, c, old, new)
        paintFill(screen, r + 1, c, old, new)
        paintFill(screen, r, c - 1, old, new)
        paintFill(screen, r, c + 1, old, new)
    return True