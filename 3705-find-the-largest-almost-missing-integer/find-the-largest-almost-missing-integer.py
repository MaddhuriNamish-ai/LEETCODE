class Solution:
    def largestInteger(self, nums, k):
        n = len(nums)
        subarrays = [set(nums[i:i+k]) for i in range(n - k + 1)]
        
        best = -1
        for x in set(nums):
            count = sum(1 for s in subarrays if x in s)
            if count == 1:
                best = max(best, x)
        return best