class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        big_answer = 1
        zeros = 0
        ans = []
        for num in nums:
            if num != 0:
                big_answer *= num
            else:
                zeros += 1
        if zeros > 1:
            return [0] * len(nums)
        for num in nums:
            if zeros == 1 and num == 0:
                ans.append(big_answer)
            elif zeros == 1:
                ans.append(0)
            else:
                ans.append(big_answer // num)
        return ans
