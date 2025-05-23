class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            max_water = max(max_water, area)
            if height[l] > height[r]:
                r -= 1
            elif height[l] < height[r]:
                l += 1
            else:
                l += 1
                r -= 1

        return max_water