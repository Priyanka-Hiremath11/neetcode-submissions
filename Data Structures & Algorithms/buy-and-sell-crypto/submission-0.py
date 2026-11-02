class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        res=0
        while l!=len(prices):
            for i in range(l+1,len(prices)):
                if prices[i]>prices[l]:
                    profit=prices[i]-prices[l]
                    res=max(res,profit)
            l+=1
        return res