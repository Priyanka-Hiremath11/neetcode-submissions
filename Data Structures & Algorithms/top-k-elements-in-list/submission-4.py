class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        b=[[] for i in range(len(nums)+1)]
        res=[]
        for num in nums:
            freq[num]=freq.get(num,0)+1
        for n,c in freq.items():
            b[c].append(n)
        for i in range(len(b)-1,-1,-1):
            for ele in b[i]:
                res.append(ele)
                if len(res)==k:
                    return res

        
        
            
        