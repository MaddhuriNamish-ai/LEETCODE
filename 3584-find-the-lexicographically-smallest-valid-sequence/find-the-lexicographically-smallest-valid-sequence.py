from typing import List

class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        
        
        
        
        suf0 = [0] * (n + 1)
        j = m
        for i in range(n - 1, -1, -1):
            suf0[i] = suf0[i + 1]
            if j > 0 and word1[i] == word2[j - 1]:
                j -= 1
                suf0[i] = suf0[i+1] + 1
            
        
        
        suf0 = [0] * (n + 1)
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                suf0[i] = suf0[i + 1] + 1
                j -= 1
            else:
                suf0[i] = suf0[i + 1]
        
       
        
        result = []
        i = 0
        j = 0
        used_change = False
        
        while j < m:
            if i >= n:
                return []
            if word1[i] == word2[j]:
                result.append(i)
                i += 1
                j += 1
            else:
                if not used_change:
                    
                    if suf0[i + 1] >= m - j - 1:
                        used_change = True
                        result.append(i)
                        i += 1
                        j += 1
                    else:
                        i += 1
                else:
                    i += 1
        
        return result