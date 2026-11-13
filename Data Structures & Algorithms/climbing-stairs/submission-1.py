class Solution:
    def climbStairs(self, n: int,) -> int:
        dp=[-1]*(n+1)
        def climb(i,dp):
            if i<0:
                return 0
            if i==0:
                return 1
            if dp[i]!=-1:
                return dp[i]
            dp[i]= climb(i-1,dp)+climb(i-2,dp)
            return dp[i]
        return climb(n-1,dp)+climb(n-2,dp)
        