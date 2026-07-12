class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        d = {}

        for n in nums2:
            while stack and stack[-1] < n:
                d[stack.pop()] = n
            stack.append(n)

        return [d.get(x, -1) for x in nums1]