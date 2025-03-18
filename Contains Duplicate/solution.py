class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        existing = set()
        for num in nums:
            if num in existing:
                return True
            else:
                existing.add(num)
        return False
