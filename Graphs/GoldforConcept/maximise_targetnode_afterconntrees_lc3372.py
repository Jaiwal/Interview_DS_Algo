from typing import List
from collections import deque, defaultdict

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        For each node in tree1, returns the number of reachable nodes within distance k 
        plus the maximum number of reachable nodes from any node in tree2 within distance k-1.
        """
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Compute reachable counts
        res1 = self.findCount(edges1, k)
        res2 = self.findCount(edges2, k - 1)

        maxTargetNodeFromTree2 = max(res2)

        # Add max count from tree2 to each result in tree1
        for i in range(n):
            res1[i] += maxTargetNodeFromTree2

        return res1

    def findCount(self, edges: List[List[int]], d: int) -> List[int]:
        """
        For a given tree (edges), computes how many nodes are reachable from each node
        within a maximum distance d using BFS.
        """
        nodes = len(edges) + 1
        adj = defaultdict(list)

        # Build adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = [0] * nodes
        for i in range(nodes):
            res[i] = self.dfs(i, adj, d, -1)

        return res

    def dfs(self, curr, adj, d, currNodeParent) -> int:
        """
        dFS traversal to count reachable nodes within a max distance `d` from `curr`.
        """
        if d<0:
            return 0

        count=1 #this node is taken 

        for neigh in adj[curr]:
            if neigh!=currNodeParent:
                count+=self.dfs(neigh,adj,d-1,curr)

        return count
    

#bfs using dequeue passes but with queue gives TLE

from typing import List
from collections import deque, defaultdict

class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        """
        For each node in tree1, returns the number of reachable nodes within distance k 
        plus the maximum number of reachable nodes from any node in tree2 within distance k-1.
        """
        n = len(edges1) + 1
        m = len(edges2) + 1

        # Compute reachable counts
        res1 = self.findCount(edges1, k)
        res2 = self.findCount(edges2, k - 1)

        maxTargetNodeFromTree2 = max(res2)

        # Add max count from tree2 to each result in tree1
        for i in range(n):
            res1[i] += maxTargetNodeFromTree2

        return res1

    def findCount(self, edges: List[List[int]], d: int) -> List[int]:
        """
        For a given tree (edges), computes how many nodes are reachable from each node
        within a maximum distance d using BFS.
        """
        nodes = len(edges) + 1
        adj = defaultdict(list)

        # Build adjacency list
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res = [0] * nodes
        for i in range(nodes):
            res[i] = self.bfs(i, adj, d, nodes)

        return res

    def bfs(self, curr: int, adj: dict, d: int, N: int) -> int:
        """
        BFS traversal to count reachable nodes within a max distance `d` from `curr`.
        """
        queue = deque([(curr, 0)])  # (node, distance)
        visited = [False] * N
        visited[curr] = True
        count = 0

        while queue:
            node, dist = queue.popleft()

            if dist > d:
                continue

            count += 1

            for neigh in adj[node]:
                if not visited[neigh]:
                    visited[neigh] = True
                    queue.append((neigh, dist + 1))

        return count
    
#with queue

from typing import List
from queue import Queue
from collections import defaultdict
class Solution:
    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:
        #nodes in tree 1, edges-1
        n=len(edges1)+1
        m=len(edges2)+1

        res1=[0]*n #store target nodes count from each node withtin tree1 max k dist
        res2=[0]*m #store target ndoe count from each node within tree2 max k-1 dist
        
        res1=self.findCount(edges1,k)
        res2=self.findCount(edges2,k-1)

        maxTargetNodeFromTree2=max(res2)

        for i in range(n):
            res1[i]+=maxTargetNodeFromTree2
        
        return res1

    def findCount(self,edges,d):
        nodes=len(edges)+1

        #create adj list first
        adj=defaultdict(list)

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)

        res=[0]*nodes

        for i in range(nodes):
            res[i]=self.bfs(i,adj,d,nodes)

        return res

    def bfs(self,curr,adj,d,N):
        """
        Perform BFS starting from the current node `curr`, and count how many nodes
        are reachable within distance `d`.
        """

        queue=Queue()
        queue.put((curr,0))
        visited=[False]*N
        visited[curr]=True
        count=0 #count of target nodes within range d

        while not queue.empty():
            node,dist=queue.get()

            if dist>d:
                continue
            count+=1 #include this node as valid target node

            for neig in adj[node]:
                if not visited[neig]:
                    visited[neig]=True
                    queue.put((neig,dist+1))

        return count

        
