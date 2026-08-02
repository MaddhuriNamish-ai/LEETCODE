from functools import lru_cache
from typing import List

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(maxsize=None)
        def dp(i: int, j: int) -> int:
            
        
            if i > j:
                return 0
            return max(
                piles[i] - dp(i + 1, j),
                piles[j] - dp(i, j - 1)
            )

        result = dp(0, n - 1) > 0
        dp.cache_clear()
        return result
        