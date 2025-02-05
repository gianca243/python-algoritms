"""
My approach
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:

        palindrome_len = 0
        r_cursor = 0
        l_cursor = 0


        for index, character in enumerate(s):
            i = len(s)
            while i != index:
                pal = s[index:i]
                if pal == pal[::-1]:
                    palindrome_len = len(pal)
                    if palindrome_len > r_cursor - l_cursor:
                        r_cursor = i
                        l_cursor = index
                i -= 1
        return s[l_cursor:r_cursor]

"""
Found solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]
"""
