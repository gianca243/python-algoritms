# first idea
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result_list = []
        for k in range(n - 1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                total = nums[k] + nums[i] + nums[j]
                if total == 0:
                    if (omg := [nums[i], nums[j], nums[k]]) not in result_list:
                        result_list.append(omg)
                    i += 1
                if total > 0:
                    j -= 1
                if total < 0:
                    i += 1
        return result_list


# improvements
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result_list = []
        men = set()
        for k in range(0, n - 2):
            j = n - 1
            i = k + 1
            if (
                nums[k] > 0
            ):  # if the offset is value are greater than 0 all values can not add to 0
                break
            while i < j and nums[k] not in men:
                total = nums[k] + nums[i] + nums[j]
                if total == 0:
                    if (omg := [nums[i], nums[j], nums[k]]) not in result_list:
                        result_list.append(omg)
                    i += 1
                    j -= 1
                if total > 0:
                    j -= 1
                if total < 0:
                    i += 1
            men.add(
                nums[k]
            )  # if we already use a value as offset we do not want to re use it
        return result_list


# second improvement


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result_list = set()
        ans = []
        men = set()
        for k in range(0, n - 2):
            j = n - 1
            i = k + 1
            if nums[k] > 0:
                break
            while i < j and k not in men:
                total = nums[k] + nums[i] + nums[j]
                if total == 0:
                    omg = [nums[k], nums[i], nums[j]]
                    if (
                        gg := tuple(omg)
                    ) not in result_list:  # instead of looking inside a list i looked inside a set
                        result_list.add(gg)
                        ans.append(omg)
                    i += 1
                    j -= 1
                if total > 0:
                    j -= 1
                if total < 0:
                    i += 1
            men.add(k)
        return ans


# fix


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        men = set()
        for k in range(0, n - 2):
            j = n - 1
            i = k + 1
            if nums[k] > 0:
                break
            while (
                i < j and nums[k] not in men
            ):  # now we check the value instead the index so now we can miss the already used offsets
                total = nums[k] + nums[i] + nums[j]
                if total == 0:
                    omg = [nums[k], nums[i], nums[j]]
                    ans.append(omg)
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                if total > 0:
                    j -= 1
                if total < 0:
                    i += 1
            men.add(nums[k])
        return ans
