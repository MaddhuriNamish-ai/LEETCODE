class Solution:
    def checkDivisibility(self, n: int) -> bool:
        s = 0
        p = 1
        x = n
        while x:
            d = x % 10
            s += d
            p *= d
            x //= 10
        return n % (s + p) == 0
        