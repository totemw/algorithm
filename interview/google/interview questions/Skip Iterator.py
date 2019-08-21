"""
Design a SkipIterator that supports a method skip(int val).
When it is called the next element equals val in iterator sequence should be skipped.

class SkipIterator implements Iterator<Integer> {

	public SkipIterator(Iterator<Integer> it) {
	}

	public boolean hasNext() {
	}

	public Integer next() {
	}

	/**
	* The input parameter is an int, indicating that the next element equals 'val' needs to be skipped.
	* This method can be called multiple times in a row. skip(5), skip(5) means that the next two 5s should be skipped.
	*/
	public void skip(int val) {
	}
}

"""
from collections import defaultdict, deque


class SkipIterator:
    def __init__(self, nums):
        self.nums = deque(nums)
        self.cnt = defaultdict(int)

    def hasNext(self):
        self._skip()
        return len(self.nums) > 0

    def skip(self, i):
        self.cnt[i] += 1

    def next(self):
        if not self.hasNext():
            return None

        return self.nums.popleft()

    def _skip(self):
        while len(self.nums) > 0 and self.nums[0] in self.cnt:
            self.cnt[self.nums[0]] -= 1

            if self.cnt[self.nums[0]] == 0:
                del self.cnt[self.nums[0]]

            self.nums.popleft()