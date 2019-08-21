"""
The idea is you have a grid with people (upper case) and cars (lower case),
there are exactly the same amount of people as cars. You must assign a person to the closest car.

Criterias:
- Closest person to the car, get the car at the first priority.
- Single car can't be assigned to 2 individuals
- Distance of a car from one individual will never be equal to distance of the same car from a different individual.
- Distances can be equal, but 2 different bikes and 2 different individuals

Note that this doesn't mean you'll assign the closest person to the closest car
because someone else might be closer to that car.
"""

import heapq

def assignBikes(self, workers, bikes):
    distances = []  # distances[worker] is tuple of (distance, worker, bike) for each bike

    for i, (x, y) in enumerate(workers):
        distances.append([])
        for j, (x_b, y_b) in enumerate(bikes):
            distance = abs(x - x_b) + abs(y - y_b)
            distances[-1].append((distance, i, j))
        distances[-1].sort(reverse=True)  # reverse so we can pop the smallest distance

    result = [None] * len(workers)
    used_bikes = set()
    queue = [distances[i].pop() for i in range(len(workers))]  # smallest distance for each worker
    heapq.heapify(queue)

    while len(used_bikes) < len(workers):
        _, worker, bike = heapq.heappop(queue)
        if bike not in used_bikes:
            result[worker] = bike
            used_bikes.add(bike)
        else:
            heapq.heappush(queue, distances[worker].pop())  # bike used, add next closest bike