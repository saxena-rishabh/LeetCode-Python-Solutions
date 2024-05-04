class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        
        highest = 0
        element = -1
        for key, value in d.items():
            if value >= highest:
                highest = value
                element = key
        
        return element

        