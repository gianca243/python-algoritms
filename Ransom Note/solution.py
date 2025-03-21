class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        store = {}
        for char in magazine:
            if store.get(char) is None:
                store.update({f"{char}": 0})
            store[char] += 1

        for char in ransomNote:
            if store.get(char) is None:
                return False
            store[char] -= 1
            if store[char] < 0:
                return False
        return True
