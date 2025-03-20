class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        n=len(nums)

        res=1 #ek element bhi nice hai
        i=0
        j=0
        mask=0

        while j<n:
            while mask & nums[j]!=0:
                mask^=nums[i]
                i+=1
            
            res=max(res,j-i+1)
            mask|=nums[j]

            j+=1
        




        

        return res
        