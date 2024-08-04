class Solution:
    def productExceptSelf(self, nums):
        prefix = [1]
        prev = nums[0]
        for i in nums[1:]:
            prefix.append(prev)
            prev = prev * i
        postfix = [1]
        after = nums[-1]
        for i in reversed(nums[:-1]):
            postfix.append(after)
            after = after * i
        
       
        postfix = postfix[::-1]
        final = []
        for i in range(len(nums)):
            final.append(prefix[i]*postfix[i])
        return final