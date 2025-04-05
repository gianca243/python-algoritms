# def insert_min_heap(heap, value):
#     # Add the new element to the end of the heap
#     heap.append(value)
#     # Get the index of the last element
#     index = len(heap) - 1
#     # Compare the new element with its parent and swap if necessary
#     while index > 0 and heap[(index - 1) // 2] > heap[index]:
#         heap[index], heap[(index - 1) // 2] = heap[(index - 1) // 2], heap[index]
#         # Move up the tree to the parent of the current element
#         index = (index - 1) // 2


# heap = []
# values = [10, 7, 11, 5, 4, 13]
# for value in values:
#     insert_min_heap(heap, value)
#     print(f"Inserted {value} into the min-heap: {heap}")

# values.sort(reverse=True)
# print(values)
# def findKthLargest(nums: list[int], k: int) -> int:
#     _min = min(nums)
#     _max = max(nums)
#     occurrencies = [0]*(_max-_min+1)
#     for item in nums:
#         occurrencies[item -_min] += 1

#     for index in range(len(occurrencies)-1, 0,-1):
#         while occurrencies[index] > 0:
#             occurrencies[index] -= 1
#             k -= 1
#             if k == 0:
#                 return index+_min

# print(findKthLargest([1], 1))


# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         nums.sort()
#         n = len(nums)
#         ans = []
#         men = set()
#         for k in range(0, n - 2):
#             j = n - 1
#             i = k + 1
#             if nums[k] > 0:
#                 break
#             while i < j and nums[k] not in men:
#                 total = nums[k] + nums[i] + nums[j]
#                 if total == 0:
#                     omg = [nums[k], nums[i], nums[j]]
#                     ans.append(omg)
#                     i += 1
#                     j -= 1
#                     while i < j and nums[i] == nums[i - 1]:
#                         i += 1
#                     while i < j and nums[j] == nums[j + 1]:
#                         j -= 1
#                 if total > 0:
#                     j -= 1
#                 if total < 0:
#                     i += 1
#             men.add(nums[k])
#         return ans


# print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
