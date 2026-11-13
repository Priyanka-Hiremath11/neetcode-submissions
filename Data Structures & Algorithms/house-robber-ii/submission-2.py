class Solution:
    def rob(self, nums: List[int]) -> int:
        dp1=[-1]*(len(nums)+1)
        dp2=[-1]*(len(nums)+1)
        if len(nums)==1: 
            return nums[0]
        def robi(i,start,dp):
            if i<start:
                return 0
            
            if dp[i]!=-1:
                return dp[i]
            take=nums[i]+robi(i-2,start,dp)
            nottake=robi(i-1,start,dp)
            dp[i]=max(take,nottake)
            return dp[i]
        return max(robi(len(nums)-2,0,dp1),robi(len(nums)-1,1,dp2))
    