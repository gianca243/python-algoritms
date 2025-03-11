"""My first Approach"""
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        response = [-1]*len(nums1)
        for index, num in enumerate(nums1):
            begin = nums2.index(num)
            for _index in range(begin, len(nums2)):
                if nums2[_index] > num:
                    response[index] = nums2[_index]
                    break
        return response
# second idea
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        response = [-1]*len(nums1)
        greater_list = [-1]*len(nums2)
        stack = []
        for index, num in enumerate(nums1):
            response[index] = nums2.index(num)
        
        for index in range(nums2):
            while stack and nums2[index] > nums2[stack[-1]]:
                greater_list[stack[-1]] = nums2[index]
                stack.pop()
            stack.append(index)
        
        for index, item in enumerate(response):
            response[index] = greater_list[item]
        
        return response
# third idea with monotonic stack and hashmap

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        mem = {}
        
        for index in range(len(nums2)):
            while stack and nums2[index] > nums2[stack[-1]]:
                mem.update({f"{nums2[stack[-1]]}":nums2[index]})
                stack.pop()

            mem.update({f"{nums2[index]}":-1})
            stack.append(index)
        
        for index, item in enumerate(nums1):
            nums1[index] = mem.get(f"{item}")
        
        return nums1
    

print(Solution().nextGreaterElement([2,4], [1,2,3,4]))
