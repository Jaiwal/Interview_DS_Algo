#solution1: recursive gives TLE
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #You can either start from the step with index 0, or the step with index 1.
        return min(self.minCost(0,cost),self.minCost(1,cost))

    def minCost(self,index,cost):
        if index>len(cost)-1:
            return 0

        take_one_step_from_here=cost[index]+self.minCost(index+1,cost)
        take_two_step_from_here=cost[index]+self.minCost(index+2,cost)

        return min(take_one_step_from_here,take_two_step_from_here)


        
#solutio2: memo
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #You can either start from the step with index 0, or the step with index 1.
        memo=[-1 for _ in range(len(cost)+1)]
        return min(self.minCost(0,cost,memo),self.minCost(1,cost,memo))

    def minCost(self,index,cost,memo):
        if index>len(cost)-1:
            return 0
        
        if memo[index]!=-1:
            return memo[index]
        take_one_step_from_here=cost[index]+self.minCost(index+1,cost,memo)
        take_two_step_from_here=cost[index]+self.minCost(index+2,cost,memo)

        memo[index]=min(take_one_step_from_here,take_two_step_from_here)
        return memo[index]


        
#solution3: bottom up
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.minCost(0,cost),self.minCost(1,cost))

    def minCost(self,index,cost):
        n=len(cost)
        dp=[0 for _ in range(n)]

        dp[0]=cost[0]
        dp[1]=cost[1]

        if n>=2:
            for i in range(2,n):
                dp[i]=cost[i]+min(dp[i-1],dp[i-2])

        return min(dp[n-1],dp[n-2])


#solution4: modify orgn cost array

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.minCost(0,cost),self.minCost(1,cost))

    def minCost(self,index,cost):
        n=len(cost)
        if n==2:
            return min(cost[0],cost[1])
        
        #not recommended but modifying original cost array here
        if n>=2:
            for i in range(2,n):
                cost[i]=cost[i]+min(cost[i-1],cost[i-2])

        return min(cost[n-1],cost[n-2])


'''
result is min (start at 0 index, start at 1 index)
at every index, you include current pese and now can take one step and two step so return min of both

dp:
think about what will it take to reach at ith, ith cost and min of either one step and 2 step before'''