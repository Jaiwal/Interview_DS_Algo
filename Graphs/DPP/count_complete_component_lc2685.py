#bfs solution

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list) 

        result=0

        for v,u in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited=[False for _ in range(n)]
        
        for i in range(n):
            if not visited[i]:
                edge_vertex=[0,0] #need this for every component
                self.bfs(i,adj,visited,edge_vertex)
                if edge_vertex[0]==edge_vertex[1]*(edge_vertex[1]-1):
                    result+=1

        return result

    def bfs(self,node,adj,visited,edge_vertex):
        q=[]
        q.append(node)
        visited[node]=True
        
        while q:
            node=q.pop()
            edge_vertex[0]+=len(adj[node])
            edge_vertex[1]+=1

            for neighbour in adj[node]:
                if not visited[neighbour]:
                    q.append(neighbour)
                    visited[neighbour]=True


#dfs solution
# 

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj=defaultdict(list) 

        result=0

        for v,u in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited=[False for _ in range(n)]
        
        for i in range(n):
            if not visited[i]:
                edge_vertex=[0,0] #need this for every component
                self.dfs(i,adj,visited,edge_vertex)
                if edge_vertex[0]==edge_vertex[1]*(edge_vertex[1]-1):
                    result+=1

        return result

    def dfs(self,node,adj,visited,edge_vertex):
        visited[node]=True
        edge_vertex[1]+=1
        edge_vertex[0]+=len(adj[node])

        for neighbour in adj[node]:
            if not visited[neighbour]:
                self.dfs(neighbour,adj,visited,edge_vertex)

      
