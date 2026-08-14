class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        count = defaultdict(int)
        left = 0
        best = 0
        for right, ch in enumerate(s):
            count[ch] += 1
            while count[ch] > 2:
                count[s[left]] -= 1
                left += 1
            best = max(best, right - left + 1)
        return best
        