from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s) // 2
        for l in range(n):
            r = -1 - (l)
            s[l], s[r] = s[r], s[l]
