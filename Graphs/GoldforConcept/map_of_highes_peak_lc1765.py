#solution1: multi source BFS so cool
from typing import List
from queue import Queue
class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows=len(isWater)
        cols=len(isWater[0])

        height=[[-1 for _ in range(cols)]for _ in range(rows)]

        q=Queue()

        for i in range(rows):
            for j in range(cols):
                if isWater[i][j]==1:
                    height[i][j]=0
                    q.put((i,j))
        
        while not q.empty():
            q_size=q.qsize()

            for _ in range(q_size):
                i,j=q.get()

                for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
                    i_=i+dr
                    j_=j+dc

                    if 0<=i_<len(isWater) and 0<=j_<len(isWater[0]) and height[i_][j_]==-1:
                        height[i_][j_]=height[i][j]+1
                        q.put((i_,j_))

        return height


        