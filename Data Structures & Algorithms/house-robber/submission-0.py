class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*(len(nums)+1)
        def rob(i,dp):
            if i<0:
                return 0
            if i==0:
                return nums[i]
            if dp[i]!=-1:
                return dp[i]
            take=nums[i]+rob(i-2,dp)
            nottake=rob(i-1,dp)
            dp[i]=max(take,nottake)
            return dp[i]
        return rob(len(nums)-1,dp)


        