class NumArray:
    int_list: list[int]
    ranges: list
    def __init__(self, nums: list[int]):
        self.int_list = list(nums)


    def sumRange(self, left: int, right: int) -> int:
        return sum(self.int_list[left:right+1])


"""
learned approach
class NumArray:
    int_list: list[int]
    ranges: list
    def __init__(self, nums: List[int]):
        self.int_list = [nums[0]]

        for index in range(1, len(nums)):
            self.int_list.append(nums[index]+self.int_list[index-1])


    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.int_list[right]
        return self.int_list[right] - self.int_list[left-1]
"""
