"""first approach T: O(n) S: O(n)"""
from collections import defaultdict
class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = defaultdict(int)
        n = len(nums)
        for num in nums:
            count[num] += 1
            if count[num] > n//2:
                return num
        return

# learned way
# T: O(n)
# S: O(1)

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        count = 0
        ans = -1
        for num in nums:
            if count == 0:
                ans = num
            if num == ans:
                count += 1
            else:
                count -= 1
        return ans