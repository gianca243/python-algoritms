"""
first approach
class Solution:
    def check_sub_string(self, s: str) -> int:
        existing_chars = []
        for character in s:
            if character in existing_chars:
                break
            else:
                existing_chars.append(character)
        return len(existing_chars)

    def lengthOfLongestSubstring(self, s: str) -> int:
        cent = 0
        for index, character in enumerate(s):
            _cent = self.check_sub_string(s[index:])
            cent = _cent if _cent >= cent else cent
        return cent   
"""
# learned approach
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        left: Marks the start of the current substring.
        max_length: Tracks the length of the longest substring without repeating characters. Initialized to 0.
        char_set: Keeps track of unique characters encountered so far, initialized as an empty set.
        """
        left = max_length = 0
        char_set = set()
        
        # right: Represents the end of the current substring. It moves from 0 to the end of the string.
        for right in range(len(s)):
            while s[right] in char_set:
                """
                This loop executes when the character at the 'right' index is already in the char_set, meaning we have encountered a repeating character.
                it removes characters from the char_set and adjusts the 'left' pointer until the current character at 'right' is no longer in the char_set. 
                This effectively removes the characters from the substring that are causing the repetition.
                """
                char_set.remove(s[left])
                left += 1

            """
            Adds the current character to char_set since it's unique now.
            Updates max_length by taking the maximum between the current max_length and the length of the current substring (right - left + 1).
            """
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length