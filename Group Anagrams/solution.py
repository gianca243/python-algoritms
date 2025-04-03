"""My approach"""
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ana = dict()
        for value in strs:
            sort_value = list(value)
            sort_value.sort()
            sort_value = "".join(sort_value)
            if ana.get(sort_value) is None:
                ana[sort_value] = []
            ana[sort_value].append(value)
        
        return [ana[key] for key in ana]
# faster but for other reasons because compexity is O(n*(nlog(n)))
# learned way
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        ana = defaultdict(list)
        for s in strs:
            letters = [0]*26
            for c in s:
                letters[ord(c) - ord('a')] += 1
            letters = tuple(letters)
            ana[letters].append(s)

        return list(ana.values())
# better o(n) => o(n*m)