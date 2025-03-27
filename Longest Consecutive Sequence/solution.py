class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        a = set(nums)
        count = 0
        for num in a:
            local = 1
            if num - 1 in a:
                continue
            while num + 1 in a:
                num += 1
                local += 1
            count = max(count, local)
        return count
