
# https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=detect-cycle-in-an-undirected-graph

#User function Template for python3

##########################################################DFS ###############################################

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, adj):
        # code here
        
        v=len(adj)
        ls=[]
        
        visited=[False for _ in range(v)]
        
        self.dfs(0,ls,adj,visited)
        
        return ls
        
    def dfs(self,node,ls,adj,visited):
        visited[node]=True
        ls.append(node)
        
        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.dfs(neighbour,ls,adj,visited)


##########################################################BFS ###############################################

from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        visited=[False]*V
        
        for i in range(V):
            if not visited[i]:
                if self.bfs(i,adj,visited,-1):
                    return True
                    
        return False
        
    def bfs(self,node,adj,visited,parent):
        
        visited[node]=True
        q=[]
        q.append((node,parent))
        
        while q:
            currentN,currentNParent=q.pop(0)
            for neighbour in adj[currentN]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    q.append((neighbour,currentN))
                elif neighbour!=currentNParent:
                    return True
                
        return False

