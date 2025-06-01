from queue import Queue
from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)

        steps=0

        q=Queue()
        visited=[[False for _ in range(n)]for _ in range(n)]

        visited[n-1][0]=True #starting from here
        q.put(1)

        while not q.empty():
            N=q.qsize()

            for _ in range(N):
                x=q.get()

                if x==n*n:
                    return steps

                for k in range(1,7):
                    val=x+k

                    if val>n*n:
                        break #out of boundary ni jana

                    cord=self.getCordinate(val,n)
                    row=cord[0]
                    col=cord[1]

                    if  visited[row][col]:
                        continue
                    else:
                        visited[row][col]=True

                    if board[row][col]==-1:
                        q.put(val)
                    else:
                        q.put(board[row][col])

                
            steps+=1
            

        return -1

                

    
    def getCordinate(self,num,n):

        RT=(num-1)//n
        RB=(n-1)-RT

        col=(num-1)%n
        if (n%2==0 and RB%2==0) or (n%2==1 and RB%2==1):
            col=(n-1)-col

        return [RB,col]
        