"""
you have a stack of boxes (n) with widths wi, hi and di
compute the height of the tallest possible stack
"""


class Box:
    def __init__(self, height, width, depth):
        self.height = height
        self.width = width
        self.depth = depth

    def fits_on(self, base):
        return base.height > self.height and base.width > self.width \
               and base.depth > self.depth


def stackBoxes(boxes):
    sortedBoxes = sorted(boxes, lambda a, b: a.height > b.height)
    stackMap = [0] * len(sortedBoxes)
    return stackMoreBoxes(sortedBoxes, None, 0, stackMap)


def stackMoreBoxes(boxes, base, index, stackMap):
    if index >= len(boxes):
        return 0
    withoutBoxHeight = stackMoreBoxes(boxes, base, index + 1, stackMap)
    withBoxHeight = 0
    box = boxes[index]
    if (not base) or box.fits_on(base):
        if stackMap[index] == 0:
            stackMap[index] = box.height + stackMoreBoxes(boxes, box, index + 1, stackMap)
        withBoxHeight = stackMap[index]
    return max(withBoxHeight, withoutBoxHeight)

