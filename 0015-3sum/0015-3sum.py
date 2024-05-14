class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        dic={}
        lst=[]
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            low=i+1
            high=len(nums)-1
            while low<high:
                sm=nums[i]+nums[low]+nums[high]
                if sm==0:
                    val=[nums[i],nums[low],nums[high]]
                    if str(val) in dic:
                        dic[str(val)]+=1
                    else:
                        dic[str(val)]=1
                        lst.append(val)
                    low+=1
                    high-=1
                elif sm>0:
                    high-=1
                else:
                    low+=1
        return lst
        