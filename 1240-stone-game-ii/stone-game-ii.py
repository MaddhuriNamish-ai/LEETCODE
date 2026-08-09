from functools import lru_cache
from typing import List
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        @lru_cache(maxsize=None)
        def dp(i, M):
            if i >= n:
                return 0
            if i + 2 * M >= n:
                return suffix[i]
            best = 0
            for X in range(1, 2 * M + 1):
                best = max(best, suffix[i] - dp(i + X, max(M, X)))
            return best

        result = dp(0, 1)
        dp.cache_clear()
        return result
        