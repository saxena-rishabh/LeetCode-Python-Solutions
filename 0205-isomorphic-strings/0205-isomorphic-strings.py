class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}

        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in dic:
                if dic[s[i]] != t[i]:
                    return False
            else:
                dic[s[i]] = t[i] 
        return True
        