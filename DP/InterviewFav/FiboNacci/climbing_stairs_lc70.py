#solution1: recursive, gives TLE

class Solution:
    def climbStairs(self, n: int) -> int:
        return self.waysToClimb(n)

    def waysToClimb(self,n):
        if n<=2:
            return n

        #take one step or take two step. total ways is sum of both

        return self.waysToClimb(n-1)+self.waysToClimb(n-2)

        
#solution2: memoized above

class Solution:
    def climbStairs(self, n: int) -> int:
        memo=[-1 for _ in range(n+1)]
        return self.waysToClimb(n,memo)

    def waysToClimb(self,n,memo):
        if n<=2:
            return n

        if memo[n]!=-1:
            return memo[n]

        #take one step or take two step. total ways is sum of both

        memo[n]=self.waysToClimb(n-1,memo)+self.waysToClimb(n-2,memo)
        return memo[n]

        
#solutio3: bottom-up, for any stairs you bascially need ways on 1 step below+ 2 steps below

class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0 for _ in range(n+1)]
        return self.waysToClimb(n,dp)

    def waysToClimb(self,n,dp):

        dp[1]=1
        if n>=2:
            dp[2]=2

        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]
        
        

        
#solution4: carefully looking, it is same as fibo

class Solution:
    def climbStairs(self, n: int) -> int:

        return self.waysToClimb(n)

    def waysToClimb(self,n):

        if n<=2:
            return n

        a=1
        b=2

        for i in range(3,n+1):
            c=a+b
            a=b
            b=c

        return c

        
        
        

        
        