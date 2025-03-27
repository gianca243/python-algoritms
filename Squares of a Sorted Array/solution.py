from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        new_list = []
        while i <= j:
            if abs(nums[i]) < abs(nums[j]):
                new_list.append(nums[j] ** 2)
                j -= 1
            else:
                new_list.append(nums[i] ** 2)
                i += 1
        return new_list[::-1]
