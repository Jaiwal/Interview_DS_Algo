#solution1: briute

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n=len(nums)
        closestSum=float('inf')


        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    currentSum=nums[i]+nums[j]+nums[k]
                    if abs(target-closestSum)>abs(target-currentSum):
                        closestSum=currentSum


        return closestSum


        

#solutio2: 2 pointer since they asked sum and not index

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n=len(nums)
        closestSum=float('inf')
        nums.sort()

        for k in range(n-2):
            i=k+1
            j=n-1

            while i<j:
                summ=nums[i]+nums[j]+nums[k]

                if abs(target-closestSum)>abs(target-summ):
                    #found better
                    closestSum=summ

                if summ<target:
                    i+=1
                else:
                    j-=1
            


        return closestSum


        