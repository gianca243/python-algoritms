class Solution:
    # first = 0
    # last = 1
    # def look_pairs(self, nums: list[int], target: int):
    #     if nums[self.first] + nums[self.last] == target:
    #         return [self.first, self.last]
    #     self.last += 1
    #     if self.last == len(nums):
    #         self.first += 1
    #         self.last = self.first + 1
    #     if self.first == len(nums) - 1:
    #         return
    #     return self.look_pairs(nums, target)

    def look_pairs(self, nums: list[int], target: int):
        cent = 0
        for i in range(cent, len(nums)):
            for j in range(cent+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            cent += 1
        return

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        return self.look_pairs(nums, target)
    
solution = Solution()

print(solution.twoSum([0,4,3,0], 0))