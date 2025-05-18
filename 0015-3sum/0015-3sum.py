class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        d = {}
        answers = []
        for i in range(0, len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    s = f'{nums[i]}{nums[l]}{nums[r]}'
                    if s not in d:
                        d[s] = 1
                        answers.append([nums[i], nums[l], nums[r]])
                    break
                elif total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
        
        return answers



        