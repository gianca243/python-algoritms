"""
My approach
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        cent = 0
        new_list = []
        for index, value in enumerate(nums1):
            if len(nums2) == 0 or value < nums2[cent]:
                new_list.append(value)
            else:
                while len(nums2) and value > nums2[0]:
                    new_list.append(nums2[0])
                    nums2.pop(0)
                new_list.append(value)
        new_list = new_list + nums2
        print(new_list)
        length = len(new_list)
        middle = int(length / 2)
        if length % 2 == 0:
            return (new_list[middle] + new_list[middle-1])/2
        else:
            return new_list[middle]
"""
