class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic = {}
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = (s[i], t[i])
            else:
                if dic[s[i]][1] != t[i]:
                    return False
            
        return True
