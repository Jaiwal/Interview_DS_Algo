#https://www.geeksforgeeks.org/problems/bfs-traversal-of-graph/1 

#BFS

#User function Template for python3
from typing import List
class Solution:
    # Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, adj: List[List[int]]) -> List[int]:
        v=len(adj)
        
        visited=[False for _ in range(v)]
        
        q=[]
        
        visited[0]=True
        q.append(0)
        
        ls=[]
        
        while q:
            curr=q.pop(0)
            ls.append(curr)
            
            for neighbour in adj[curr]:
                if not visited[neighbour]:
                    visited[neighbour]=True
                    q.append(neighbour)
                    
        return ls


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())  # Number of test cases
    for i in range(T):
        V = int(input())  # Number of vertices
        E = int(input())  # Number of edges
        adj = [[] for i in range(V)]  # Adjacency list
        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Undirected graph

        ob = Solution()
        ans = ob.bfsOfGraph(adj)
        print(" ".join(map(str, ans)))  # Print the BFS traversal result

# } Driver Code Ends



#DFS

#User function Template for python3

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


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    while T > 0:
        V, E = map(int, input().split())
        # Create adjacency list with V vertices
        adj = [[] for i in range(V)
               ]  # List of lists (vector of vectors equivalent)

        # Reading edges
        for i in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)

        # Create an object of Solution class
        ob = Solution()
        ans = ob.dfsOfGraph(adj)

        # Printing the result
        for i in range(len(ans)):
            print(ans[i], end=" ")
        print()
        T -= 1
        print("~")
# } Driver Code Ends