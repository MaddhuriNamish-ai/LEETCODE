class Solution:
    def longestSubsequence(self, nums: list[int]) -> int:
        total_xor = 0
        for x in nums:
            total_xor ^= x
        n = len(nums)
        if total_xor != 0:
            return n
        if any(x != 0 for x in nums):
            return n - 1
        return 0
        