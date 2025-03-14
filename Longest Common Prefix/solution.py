"""My approach"""
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        result = strs[0]
        for index in range(1,len(strs)):
            limit = min(len(result), len(strs[index]))
            cent = 0
            while cent < limit and result[cent] == strs[index][cent]:
                cent += 1
            result = strs[index][:cent]
        return result