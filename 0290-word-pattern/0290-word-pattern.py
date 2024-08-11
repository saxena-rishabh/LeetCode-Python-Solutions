class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        s = s.split()
        mapped_in_s = set()
        for i in range(len(pattern)):
            if pattern[i] not in dic:
                if s[i] not in mapped_in_s:
                    dic[pattern[i]] = (pattern[i], s[i])
                    mapped_in_s.add(s[i])
                else:
                    return False
            else:
                if dic[pattern[i]][1] != s[i]:
                    return False
            
        return True