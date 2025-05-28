"""first approach"""


class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        l = 0
        r = 1
        n = len(height)
        accu = 0
        while r < n:
            if height[l] <= height[r]:
                water += accu
                accu = 0
                l = r
                r = l + 1
            elif height[l] > height[r]:
                accu += height[l] - height[r]
                r += 1
            if r >= n:
                accu = 0
                l += 1
                r = l + 1
        return water


# brute solution
class Solution:
    def trap(self, height: list[int]) -> int:
        water = 0
        l = 0
        r = 1
        n = len(height)
        diff = {}
        temp_diff = {}
        while r < n:
            if height[l] <= height[r]:
                diff.update(temp_diff)
                temp_diff.clear()
                l = r
                r = l + 1
            elif height[l] > height[r]:
                temp_diff[r] = height[l] - height[r]
                r += 1
            if height[r] > height[r - 1]:
                possible = r - 2
            if r >= n:
                temp_diff.clear()
                l += 1
                r = l + 1
        r = n - 1
        l = r - 1
        temp_diff.clear()
        while l > -1:
            if height[r] <= height[l]:
                diff.update(temp_diff)
                temp_diff.clear()
                r = l
                l = r - 1
            elif height[r] > height[l]:
                temp_diff[l] = height[r] - height[l]
                if diff.get(l):
                    temp_diff[l] = max(temp_diff[l], diff[l])
                l -= 1
            if l <= -1:
                temp_diff.clear()
                r -= 1
                l = r - 1
        for item in diff.values():
            water += item
        return water


# learned solution


class Solution:
    def trap(self, height: list[int]) -> int:
        n = len(height)
        r_columns = [0] * n
        l_columns = [0] * n
        l_wall = 0
        r_wall = 0
        l = 0
        while l < n:
            r = -l - 1
            r_columns[r] = r_wall
            l_columns[l] = l_wall
            l_wall = max(l_wall, height[l])
            r_wall = max(r_wall, height[r])
            l += 1

        water = 0
        for index in range(n):
            curr_min = min(r_columns[index], l_columns[index])
            if (diff := curr_min - height[index]) > 0:
                water += diff
        return water
