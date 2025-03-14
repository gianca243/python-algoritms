class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        L = len(nums)
        result = []
        prev = None
        for i in range(L):
            if prev is None:
                prev = nums[i]
            if i<L-1 and nums[i] == (nums[i+1] - 1):
                continue # or pass
            elif prev != nums[i]:
                result.append(f"{prev}->{nums[i]}")
                prev = None
            else:
                result.append(f"{nums[i]}")
                prev = None
        return result
