class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pprod=[1]*len(nums)
        sprod=[1]*len(nums)

        pprod[0]=nums[0]
        for i in range(1,len(nums)):
            pprod[i]=pprod[i-1]*nums[i]
        sprod[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            sprod[i]=sprod[i+1]*nums[i]
        dp=[1]*len(nums)
        
        dp[0]=sprod[1]
        dp[-1]=pprod[-2] 
        for i in range(1,len(nums)-1):
            dp[i]=pprod[i-1]*sprod[i+1]
        return dp

        

        