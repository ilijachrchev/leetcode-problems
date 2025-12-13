class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        sublast = 1

        for i in range(n - 1):
            temp = last
            last = last + sublast
            sublast = temp
        return last