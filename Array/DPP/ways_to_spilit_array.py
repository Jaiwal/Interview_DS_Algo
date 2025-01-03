from typing import List

#solution 1 : good to see pattern wise solving however its n2 appraoch
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        prefix=[0]*(n)
        suffix=[0]*(n)
        
        prefix[0]=nums[0]
        for i in range(1,n-1):
            prefix[i]=prefix[i-1]+nums[i]

        suffix[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suffix[i]=suffix[i+1]+nums[i]

        spilt=0

        for i in range(n-1):
            if prefix[i]>=suffix[i+1]:
                spilt+=1

        return spilt


#solution 2 : just keep total sum 

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n=len(nums)
        summ=sum(nums)
        left_sum=0
        right_sum=0
        pivot=0

        for i in range(n-1):
            left_sum+=nums[i]
            right_sum=summ-left_sum
            if left_sum>=right_sum:
                pivot+=1
        
        return pivot
        



        