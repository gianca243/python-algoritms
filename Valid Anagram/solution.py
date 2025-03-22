from collections import defaultdict


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for i in range(n):
            s_dict[s[i]] += 1
            t_dict[t[i]] += 1

        t_keys = t_dict.keys()
        for key in s_dict:
            if key not in t_keys:
                return False
            if s_dict[key] != t_dict[key]:
                return False

        return True
