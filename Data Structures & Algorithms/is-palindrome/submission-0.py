class Solution:
    def isPalindrome(self, s: str) -> bool:
        t=""
        for i in s:
            if i.isalnum():
                t+=i
        l,r=0,len(t)-1
        while l<r:

            if t[l].lower()!=t[r].lower():
                return False
            
            l+=1
            r-=1

        return True