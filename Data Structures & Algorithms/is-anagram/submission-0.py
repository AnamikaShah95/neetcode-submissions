class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        freq={}
        for i in s:
            freq[i] = freq.get(i,0)+1
        for i in t:
            if freq.get(i,0)==0:
                return False
            freq[i] -= 1
        return True

        