"""
A variant of the max-flow problem

Each edge e has capacity c(e) and cost cost(e)

Find the maximum flow that has the minimum totao cost

Code:
1. Just find the max-flow graph
2. Repeat:
    - Take the residual graph
    - Find a negative cost cycle using Bellman-Ford
        - If there is none, finish
    - Circulate flow through the cycle to decrease the total
      cost, until one of the edges is saturated
        - The total amount of flow doesn't change
Note: very slow


"""