"""First approach"""
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort()
        return nums[len(nums)-k]
# second idea
class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        _min = min(nums)
        _max = max(nums)
        occurrencies = [0]*(_max-_min+1)
        for item in nums:
            occurrencies[item -_min] += 1
        
        arr_size = len(occurrencies)
        cent = arr_size-1
        while cent >= 0:
            while occurrencies[cent] > 0:
                occurrencies[cent] -= 1
                k -= 1
                if k == 0:
                    return cent+_min
            cent -= 1