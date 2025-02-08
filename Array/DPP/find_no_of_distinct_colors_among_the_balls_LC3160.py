#solution1: using array 
from typing import List
from collections import defaultdict
class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ballList=[-1 for _ in range(limit+1)]

        #-1 represents ball is not colored

        mp=defaultdict(int)
        res=[0 for _ in range(len(queries))]

        for index,query in enumerate(queries):
            ball=query[0]
            color=query[1]

            if ballList[ball]!=-1:
                #find out previous color first
                prevCol=ballList[ball]
                #decrease the color count in map
                mp[prevCol]-=1

                if mp[prevCol]==0:
                    del mp[prevCol]
            

            #if not colored
            ballList[ball]=color
            mp[color]+=1

            res[index]=len(mp)

        return res

            
        
#solution2: using map

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n=len(queries)
        result=[0]*n

        colormp=defaultdict(int) #color->count
        ballmp={}  #ball->color

        for i in range(n):
            ball,color=queries[i]
            
            #if ball already colored
            if ball in ballmp:
                prevcolor=ballmp[ball]
                colormp[prevcolor]-=1

                #remove color from
                if colormp[prevcolor]==0:
                    del colormp[prevcolor]

            ballmp[ball]=color
            colormp[color]+=1

            result[i]=len(colormp)

        return result
        