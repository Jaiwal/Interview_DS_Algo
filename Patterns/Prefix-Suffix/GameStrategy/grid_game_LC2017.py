from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        firstRowRemainingSum=sum(grid[0])
        secondRowTakanSum=0

        #R1 will focus on minimizing for R2, he no care about itself
        minimizedRobot2Sum=float('inf')

        #min sum R2 can have depends on strategy R1 can take which is at col it goes down
        #No of such strategy= no of cols

        for robot1colStrategy in range(len(grid[0])):

            #R1 goes down from robot1colStrategy
            #Now what R2 has left as an option

            #current col in first row point is gone for R2
            firstRowRemainingSum-=grid[0][robot1colStrategy]

            #R2 gotta take best of whats available, didnt add anything in second row since this is first col 
            bestofrobot2=max(firstRowRemainingSum,secondRowTakanSum)

            #R1 just want R2 should get minimum 
            minimizedRobot2Sum=min(minimizedRobot2Sum,bestofrobot2)

            secondRowTakanSum+=grid[1][robot1colStrategy]

        return minimizedRobot2Sum






        