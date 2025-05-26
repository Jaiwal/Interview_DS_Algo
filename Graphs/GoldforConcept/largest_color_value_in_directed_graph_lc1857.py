from collections import deque,defaultdict
from typing import List
class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        adj=defaultdict(list)
        n=len(colors)
        indegree=[0]*n

        for u,v in edges:
            adj[u].append(v)
            indegree[v]+=1

        queue=deque()

        t=[[0]*26 for _ in range(n)]

        for i in range(n):
            if indegree[i]==0:
                queue.append(i)
                t[i][ord(colors[i])-ord('a')]=1
                #abhi hi set krdo un nodes ka jo kisi pe depend nhi

        ans=0
        countNodes=0

        while queue:
            u=queue.popleft()
            countNodes+=1

            ans=max(ans,t[u][ord(colors[u])-ord('a')])

            for v in adj[u]:
                for i in range(26):
                    add=1 if (ord(colors[v])-ord('a'))==i else 0
                    t[v][i]=max(t[v][i],t[u][i]+add)
                
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)

        
        if countNodes<n:
            return -1

        return ans