import numpy as np
import heapq

class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}
        self.predecessors = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]

    def setPredecessor(self,vertex):
        self.predecessors[vertex.getId()] = vertex

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    ###ALGORITHMS###

    def fordBellman(self,a):
        '''
        a -- prices between cities
        a -- nxn np.array
        '''
        n = a.shape[0]
        #k -- num of flights within a trip
        k = 1
        x = [a[0][i] for i in range(n)]
        #y = x.copy()
        while k <= n:
            for s in range(n):
                #y[s] = x[s]
                for i in range(n):
                    if x[s] > x[i] + a[i][s]:
                        x[s] = x[i] + a[i][s]
            #x = y.copy()
            k+=1
        return x

    def floyd(self,a):
        '''
        a -- prices between cities
        a -- nxn np.array
        '''
        n = a.shape[0]
        A = np.zeros((n,n))
        k = 0
        A[:,:] = a.copy()
        while k < n:
            for j in range(n):
                for i in range(n):
                    if A[i, j] > a[i, k] + a[k, j]:
                        A[i, j] = a[i, k] + a[k, j]
            k += 1
        return A

    def bfs(self,start):
        queue = []
        visited = dict(zip(list(self.vertList.keys()),[False]*len(self.vertList.items())))
        currentVert = self.vertList[start]
        queue.append(currentVert.getId())
        result = []
        visited[start] = True
        while not queue == []:
            vertInd = queue.pop(0)
            currentVert = self.vertList[vertInd]
            #visited[vertInd] = True
            result.append(currentVert.getId())
            for nbr in currentVert.getConnections():
                nbr.setPredecessor(currentVert)
                if not visited[nbr.getId()]:
                    queue.append(nbr.getId())
                    visited[nbr.getId()] = True
        return result

    def dfs(self,start):
        stack = []
        visited = dict(zip(list(self.vertList.keys()), [False] * len(self.vertList.items())))
        currentVert = self.vertList[start]
        stack.append(currentVert.getId())
        result = []
        visited[start] = True
        while not stack == []:
            vertInd = stack.pop()
            currentVert = self.vertList[vertInd]
            # visited[vertInd] = True
            result.append(currentVert.getId())
            for nbr in currentVert.getConnections():
                nbr.setPredecessor(currentVert)
                if not visited[nbr.getId()]:
                    stack.append(nbr.getId())
                    visited[nbr.getId()] = True
        return result


    def topSort(self):
        def visit(node,visited,unmarked,L):
            if visited[node] == 'temp':
                raise ValueError('Not a DAG')
            elif visited[node] == 'not':
                visited[node] = 'temp'
                unmarked.remove(node)
                for nbr in self.vertList[node].getConnections():
                    visit(nbr.getId(),visited,unmarked,L)
                visited[node] = 'perm'
                L.insert(0,node)


        L = []
        unmarked = set(list(self.vertList.keys()))
        visited = dict(zip(list(self.vertList.keys()), ['not'] * len(self.vertList.items())))
        print(unmarked)
        while not len(unmarked) == 0:
            node = unmarked.pop()
            unmarked.add(node)
            visit(node,visited,unmarked,L)
        return L

    def tarjan(self):#BUG
        def strongConnect(node,components):
            nonlocal index
            node.index = index
            node.lowlink = index
            index += 1
            stack.append(node)
            node.onStack = True

            for nbr in node.getConnections():
                try:
                    nbr.index == 0
                except AttributeError:
                    strongConnect(nbr,components)
                    node.lowlink = min(node.lowlink, nbr.lowlink)
                else:
                    if nbr.index < node.index:
                        node.lowlink = min(node.lowlink, nbr.index)

            if node.lowlink == node.index:
                s = set([node.getId()])
                w = stack.pop()
                stack.append(w)
                while not w == node:
                    w = stack.pop()
                    w.onStack = False
                    s.add(w.getId())
                components.append(s)



        index = 0
        stack = []
        components = []
        for (nodeId, node) in self.vertList.items():
            try:
                node.index == 0
            except AttributeError:
                strongConnect(node,components)
        return components

    def dijkstra(self,start):
        return None




    
def makeDAG():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(4,3,7)
    g.addEdge(5,3,3)
    g.addEdge(0,4,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    return g

def makeDCG():
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addEdge(0,1,5)
    g.addEdge(1,0,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(4,3,7)
    g.addEdge(5,3,3)
    g.addEdge(0,4,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    return g


g = makeDCG()