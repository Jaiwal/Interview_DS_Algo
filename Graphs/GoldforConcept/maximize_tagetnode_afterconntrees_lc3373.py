from typing import List
from collections import defaultdict

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:
        N=len(edges1)+1
        M=len(edges2)+1


        adjA=self.getAdj(edges1)
        adjB=self.getAdj(edges2)


        markA=[-1]*N
        markA[0]=0

        countsA=[0,0] #zeroMarkedcountA,onemarkedcountA
        self.dfs(0,adjA,-1,markA,countsA)


        markB=[-1]*M
        markB[0]=0

        countsB=[0,0] #zeroMarkedcountA,onemarkedcountA
        self.dfs(0,adjB,-1,markB,countsB)

        maxfromTree2=max(countsB)

        res=[]

        for i in range(N):
            count=countsA[markA[i]]
            res.append(count+maxfromTree2)

        return res
        
        
    def getAdj(self,edges):
        adj=defaultdict(list)
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        return adj

    def dfs(self,curr,adj,parent,mark,counts):
        if mark[curr]==0:
            counts[0]+=1
        else:
            counts[1]+=1

        for neighbour in adj[curr]:
            if neighbour!=parent:
                mark[neighbour]=1-mark[curr]
                self.dfs(neighbour,adj,curr,mark,counts)
        