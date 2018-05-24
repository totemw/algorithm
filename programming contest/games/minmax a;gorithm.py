"""
a competitive zero-sum tow-player game:
if the first player's score is x, then the other player
gets -x
Each player tries to maximize his/her own score

MinMax Algorithm
Define f(S) - optimal score of the current player who
starts at state S
T1 T2 ... Tm be states that can be reached from S using a single move
Let T be the state that minimizes f(Ti)
Then, f(S) = -f(T)
(Minimize the opponent's score maximizes my score)

Note: Memoization + recursion VERSUS Tabulation + iteration


return value: x <- max{x, -f(T)}
memo: f(S) = x and return x

"""