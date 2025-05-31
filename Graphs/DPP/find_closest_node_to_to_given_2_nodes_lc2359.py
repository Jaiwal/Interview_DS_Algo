#dfs:

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)

        dist_1=[float('inf')]*n
        dist_2=[float('inf')]*n

        visited_1=[False]*n
        visited_2=[False]*n

        dist_1[node1]=0
        dist_2[node2]=0

        self.dfs(edges,node1,dist_1,visited_1)
        self.dfs(edges,node2,dist_2,visited_2)

        minDistanceNode=-1
        minDistanceSoFar=float('inf')

        for i in range(n):
            maxD=max(dist_1[i],dist_2[i])

            if minDistanceSoFar>maxD:
                minDistanceSoFar=maxD
                minDistanceNode=i

        return minDistanceNode

    def dfs(self,edges,node,dist,visited):
        visited[node]=True

        neighbour=edges[node]

        if neighbour!=-1 and not visited[neighbour]:
            visited[neighbour]=True
            dist[neighbour]=1+dist[node]
            self.dfs(edges,neighbour,dist,visited)





#bfs

from queue import Queue
class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n=len(edges)

        dist_1=[float('inf')]*n
        dist_2=[float('inf')]*n

        self.bfs(edges,node1,dist_1,)
        self.bfs(edges,node2,dist_2)

        minDistanceNode=-1
        minDistanceSoFar=float('inf')

        for i in range(n):
            maxD=max(dist_1[i],dist_2[i])

            if minDistanceSoFar>maxD:
                minDistanceSoFar=maxD
                minDistanceNode=i

        return minDistanceNode

    def bfs(self,edges,node,dist):
        q=Queue()

        q.put(node)
        dist[node]=0
        visited=[False]*len(edges)
        visited[node]=True

        while not q.empty():
            node=q.get()

            neighbour=edges[node]

            if neighbour!=-1 and not visited[neighbour]:
                visited[neighbour]=True
                dist[neighbour]=1+dist[node]
                q.put(neighbour)
     