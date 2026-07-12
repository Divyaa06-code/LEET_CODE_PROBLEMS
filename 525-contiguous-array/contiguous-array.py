class Solution(object):
    def findMaxLength(self, nums):
        d = {0: -1}
        s = ans = 0

        for i, x in enumerate(nums):
            s += 1 if x == 1 else -1

            if s in d:
                ans = max(ans, i - d[s])
            else:
                d[s] = i

        return ans