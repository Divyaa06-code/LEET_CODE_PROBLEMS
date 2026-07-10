class Solution(object):
    def minSwaps(self, nums):
        ones = sum(nums)

        if ones <= 1:
            return 0

        arr = nums + nums

        # Count ones in the first window
        curr = sum(arr[:ones])
        max_ones = curr

        # Slide the window
        for i in range(ones, len(arr)):
            curr += arr[i] - arr[i - ones]
            max_ones = max(max_ones, curr)

        return ones - max_ones