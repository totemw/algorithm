# For a given source string and a target string,
# you should output the first index

#basic solution
class Solution1:
    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        for i in range(len(source) - len(target) + 1):
            for j in range(len(target)):
                if source[i + j] != target[j]:
                    break
            else:
                    return i
        return -1

#O((n-m) * m)
class Solution:
    def ComputePrefixFunction(self, str):
        index = [0 for i in range(len(str))]
        l = len(str)
        index[0] = 0
        k = 0
        for i in range(1, l):
            while k > 0 and str[k] != str[i]:
                k = index[k - 1]
            if str[k] == str[i]:
                k += 1
            index[i] = k
        return index

    def strStr(self, source, target):
        if source is None or target is None:
            return -1
        n = len(source)
        m = len(target)
        if m == 0:
            return 0
        index = self.ComputePrefixFunction(target)
        q = 0
        for i in range(0, n):
            while q > 0 and target[q] != source[i]:
                q = index[q - 1]
            if target[q] == source[i]:
                q += 1
            if q == m:
                return i - m + 1
        return None

s = Solution()
print (s.strStr("abcefabcdf", "abcd"))