class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()

        res = []
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1], i[1])

        return res
        