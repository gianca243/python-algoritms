class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        current = intervals.pop(0)
        ans = []
        i = 0

        while intervals:

            if current[1] >= intervals[i][0] and intervals[i][1] >= current[0]:
                current[0] = min(intervals[i][0], current[0])
                current[1] = max(intervals[i][1], current[1])
                intervals.pop(i)
                i = 0
            else:
                i += 1

            if i > len(intervals) - 1:
                ans.append(current)
                current = None
                i = 0

            if current is None and intervals:
                current = intervals.pop(0)

        if current is not None:
            ans.append(current)

        return ans


omg = Solution().merge
print(omg([[1, 3], [2, 6], [8, 10], [15, 18]]))

# improvement


class BSolution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: x[0])
        ans = []
        ans.append(intervals.pop(0))
        for interv in intervals:
            if interv[0] <= ans[-1][1]:
                ans[-1][1] = max(interv[1], ans[-1][1])
            else:
                ans.append(interv)
        return ans
