class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_list = []
        for c in s:
            if c.isalnum():
                new_list.append(c)
        i = 0
        j = len(new_list) - 1
        while i <= j:
            if new_list[i].lower() != new_list[j].lower():
                return False
            i += 1
            j -= 1
        return True