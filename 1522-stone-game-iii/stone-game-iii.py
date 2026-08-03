from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + stoneValue[i]
        
        dp = [0] * (n + 1)  
        
        for i in range(n - 1, -1, -1):
            best = float('-inf')
            for k in range(1, 4):
                if i + k > n:
                    break
                taken = suffix_sum[i] - suffix_sum[i + k]
                best = max(best, taken - dp[i + k])
            dp[i] = best
        
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"