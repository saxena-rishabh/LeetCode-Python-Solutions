class Solution:
    def compare(self, i, strs):
        prev = strs[0][i]
        for element in strs[1:]:
            current = element[i]
            if current != prev:
                return False
        
        return True
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # finding length of smallest string
        smallest = float('inf')
        for element in strs:
            if len(element) <= smallest:
                smallest = len(element)
        output = ''
        for i in range(smallest):
            if self.compare(i, strs):
                output += strs[0][i]
            else:
                break
        return output


    




        