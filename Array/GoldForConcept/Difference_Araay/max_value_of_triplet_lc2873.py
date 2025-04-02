#brute force is to use 3 loops which is way too much

#app 2

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        leftMax=[0]*n
        rightMax=[0]*n

        for j in range(1,n):
            leftMax[j]=max(leftMax[j-1],nums[j-1])

        for j in  range(n-2,-1,-1):
            rightMax[j]=max(rightMax[j+1],nums[j+1])

        res=0

        for j in range(1,n):
            res=max(res,(leftMax[j]-nums[j])*rightMax[j])

        return res
        


####this is such a gold approach without using extra space

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        maxDiff=0
        maxi=0

        for k in range(n):
            res=max(res,maxDiff*nums[k])
            maxDiff=max(maxDiff,maxi-nums[k])
            maxi=max(maxi,nums[k])

        return res
 