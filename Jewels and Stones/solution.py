class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels = set(jewels)
        count = 0
        for char in stones:
            if char in jewels:
                count += 1
        return count
