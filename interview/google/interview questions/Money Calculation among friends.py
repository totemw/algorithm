"""
money balancing
"""
class Solution:

    def minTransfers(self, transactions):
        """
    :type transactions: List[List[int]]
    :rtype: int
    """
        if not transactions:
            return 0
        balance = dict()
        for trans in transactions:
            balance[trans[0]] = balance.get(trans[0], 0) - trans[2]
            balance[trans[1]] = balance.get(trans[1], 0) + trans[2]
        balance_list = []
        for p in balance:
            if balance[p] != 0:
                balance_list.append(balance[p])
        del balance
        return self.helper(sorted(balance_list))


def helper(self, balance):
    if len(balance) == 0:
        return 0
    min_trans = float("Inf")
    for i in range(1, len(balance)):
        if balance[0] * balance[i] < 0:
            if balance[0] + balance[i] == 0:
                min_trans = min(min_trans, self.helper(balance[1:i] + balance[i + 1:]) + 1)
            else:
                min_trans = min(min_trans, self.helper(balance[1:i] + balance[i + 1:] + [balance[0] + balance[i]]) + 1)
    return min_trans

"""
next: priority queue
"""