class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        m_map = {}
        for i in magazine:
            if i in m_map:
                m_map[i] += 1
            else:
                m_map[i] = 1

        for i in ransomNote:
            if i not in m_map:
                return False
            elif m_map[i] < 1:
                return False
            else:
                m_map[i] -= 1
        
        return True
        
        for key, value in r_map.items():
            if value >= 1:
                return False
        
        return True
        
        