#solution1: brutforce for checking all possible paths using BT
from typing import List
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        visited=[[False for _ in range(cols)]for _ in range(rows)]
        
        #explore all paths, send starting cordinates, send cost taken for current cell
        return self.dfs(0,0,grid,visited,0)

    def dfs(self,i,j,grid,visited,cost):
        if i==len(grid)-1 and j==len(grid[0])-1:
            return cost

        #mark the cell as visited first
        visited[i][j]=True

        #explore
        minCost=float('inf')

        # # R, L, D, U
        
        # for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        #     i_=i+dr
        #     j_=j+dc
    
        #     if 0<=i_<len(grid) and 0<=j_<len(grid[0]) and not visited[i_][j_]:
        #         newCost=cost+ ((grid[i][j]-1!=dr)?1:0)
        #         #if dr is 

        directions=[(0,1),(0,-1),(1,0),(-1,0)]
        for dir_i in range(3):
            i_=i+directions[dir_i][0]
            j_=j+directions[dir_i][1]

            if 0<=i_<len(grid) and 0<=j_<len(grid[0]) and not visited[i_][j_]:
                nextCost=cost+ (1 if grid[i][j] - 1 != dir_i else 0)

                minCost=min(minCost,self.dfs(i_,j_,grid,visited,nextCost))

        
        visited[i][j]=False
        return minCost
    
#solution2:using djikstra's

import heapq
class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        pq=[]
        res=[[float('inf') for _ in range(cols)]for _ in range(rows)]
        
        #put the source in pq
        heapq.heappush(pq,(0,0,0))

        #cost to reach source is 0 ofc
        res[0][0]=0

        while pq:
            curr= heapq.heappop(pq)
            currCost=curr[0]
            i=curr[1]
            j=curr[2]

            directions=[(0,1),(0,-1),(1,0),(-1,0)]

            for dir_i in range(4):
                i_=i+directions[dir_i][0]
                j_=j+directions[dir_i][1]

                if 0<=i_<len(grid) and 0<=j_<len(grid[0]):
                    gridDirection=grid[i][j]
                    dirCost=1 if grid[i][j]-1!=dir_i else 0
                    newCost=currCost+dirCost
                    if newCost<res[i_][j_]:
                        res[i_][j_]=newCost
                        heapq.heappush(pq,(newCost,i_,j_))


        return res[rows-1][cols-1]



 



