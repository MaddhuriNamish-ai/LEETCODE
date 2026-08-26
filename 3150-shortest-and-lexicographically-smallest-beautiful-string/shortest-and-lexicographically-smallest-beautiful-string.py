class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        best = ""
        best_len = float('inf')
        
        left = 0
        ones = 0
        for right in range(n):
            if s[right] == '1':
                ones += 1
            while ones > k or (ones == k and s[left] == '0'):
                if s[left] == '1':
                    ones -= 1
                left += 1
            
            if ones == k:
                cur_len = right - left + 1
                candidate = s[left:right+1]
                if cur_len < best_len or (cur_len == best_len and candidate < best):
                    best_len = cur_len
                    best = candidate
        
        return best
        