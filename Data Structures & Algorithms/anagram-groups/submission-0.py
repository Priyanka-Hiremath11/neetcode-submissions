class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for w in strs:
            key = ''.join(sorted(w))
            if key not in d:
                d[key]=[]
            d[key].append(w)
        return list(d.values())
