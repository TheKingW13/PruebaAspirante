from numpy import *
import math
class exm:
    n = 0
    adj=[]
    visited=[],[]
    dist=[],[]
    k = 0
    INF = 10000000
    bitMask=[]
    cost=[],[]

    adj[n]

    for  i in n:
    	adj[i]

    visited = [n][(1<<k)]
    dist = int[n][(1<<k)]
    cost = int[n][n]

    for i in range(0,dist.length):
    	for j in range(0,dist[i].length):
    		dist[i][j] = INF

    def  addEdge(u, v, c,adj):
        adj[u].add(v)
        adj[v].add(u)
        cost[u][v] = c
        cost[v][u] = c

    def bfs(source,mask,dist):
         dist[source][mask] = 0
         LinkedList=[]
         set.add({source,mask});
         while(set.size()>0):
             current=[]
             currentSource = current[0]
             currentMask = current[1]
             adj=[currentSource].iterator()
             bitMask=[]
             while(adj.hasNext()):
                next = adj.next()
                newMask = currentMask| bitMask[next]
                newDist = dist[currentSource][currentMask] + cost[currentSource][next]
                    if newDist < dist[next][newMask]:
                    	dist[next][newMask] = newDist
                    	set.add({next,newMask})

    output = int.MAX_VALUE
    for i in range (1,k):
        for j in range(1,j):
            if i|j == (1<<k)-1:
                output = math.min(output,math.max(dist[n-1][i],dist[n-1][j]))
        print(output)


	bitMask[n]
		for i in range(0,n):
           int numberOfFish = sc.nextInt()
           for in j range(0,numberOfFish):
               int fishType = sc.nextInt()
               bitMask[i] = bitMask[i] | 1<<(fishType-1)

    Graph g = new Graph(n,k,bitMask)
    for in i range (0,m):
         int u = sc.nextInt()
         int v = sc.nextInt()
         int cost = sc.nextInt()
         g.addEdge(u-1,v-1,cost)

    g.bfs(0,bitMask[0])