class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        f1={}
        f2={}
        if len(s)!=len(t):
            return False
        for l in s:
            f1[l]=f1.get(l,0)+1
        for l in t:
            f2[l]=f2.get(l,0)+1
        return f1==f2
        