class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)
        i = nums.index(min(nums))
        j = nums.index(max(nums))
        a, b = min(i, j), max(i, j)
        return min(b + 1, n - a, (a + 1) + (n - b))
        