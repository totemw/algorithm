"""
Given a two-dimensional graph with points on it, find a line
which passes the most number of points

"""


def best_line(points):
    average_x = float(sum([p.x for p in points])) / len(points)
    average_y = float(sum([p.y for p in points])) / len(points)
    shifted_points = [Point(p.x - average_x, p.y - average_x) for p in points]
    slope = best_slope_through_origin(shifted_points)
    intercept = average_y - slope * average_x
    if not slope:
        return None
    return lambda x: slope * x + intercept


def best_slope_through_origin(points):
    denominator = sum([p.x * p.x for p in points])
    if denominator == 0:
        return None
    numerator = sum([p.x * p.y for p in points])
    return float(numerator) / denominator


class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
