import random
import copy
import queue


class UndirectedGraph(object):
    def __init__(self, listOfEdges):
        """
        listOfEdges shows which nodes of the graph are connected
        :type listOfEdges: [(node, node)], node can be a string or a number
        """
        self.outputEdges, self.vertices = self.makeDict(listOfEdges)
        # self.listOfEdges = listOfEdges

    def __str__(self):
        str1 = 'vertices: ' + str(self.vertices) + '\nedges: ' + str(self.outputEdges)
        return str1

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self.outputEdges.__iter__()

    def keys(self):
        return self.outputEdges.keys()

    def __getitem__(self, item):
        return self.outputEdges.__getitem__(item)

    def __len__(self):
        return self.vertices.__len__()

    def makeDict(self, listOfEdges):
        """
        creates a dictionary representation of the graph
        :param listOfEdges:
        :return: fromVert: {node: [node]}
        vertices: set of nodes
        """
        fromVert = {}
        vertices = set([])
        for pair in listOfEdges:
            if pair[0] not in fromVert.keys():
                fromVert[pair[0]] = [pair[1]]
            else:
                fromVert[pair[0]].append(pair[1])
            if pair[1] not in fromVert.keys():
                fromVert[pair[1]] = [pair[0]]
            else:
                fromVert[pair[1]].append(pair[0])

            vertices.add(pair[0])
            vertices.add(pair[1])

        return fromVert, vertices

    def mergeRandomPoints(self):
        v1 = list(self.outputEdges.keys())[random.randint(0, len(self) - 1)]
        v2 = self[v1][random.randint(0, len(self[v1]) - 1)]
        self.outputEdges[v1].extend(self.outputEdges[v2])
        print(v1, v2)
        for x in self.outputEdges[v2]:
            l = self.outputEdges[x]
            for i in range(0, len(l)):
                if l[i] == v2:
                    l[i] = v1

        while v1 in self.outputEdges[v1]:
            self.outputEdges[v1].remove(v1)

        del self.outputEdges[v2]
        self.vertices.remove(v2)

    def randomContraction(self):
        while len(self.vertices) > 2:
            self.mergeRandomPoints()

        return len(self.outputEdges[list(self.vertices)[0]])

    def repeatRandContr(self, n):
        answers = []
        for i in range(n):
            g = copy.deepcopy(self)
            answers.append(g.randomContraction())
        return min(answers)


class GraphForSearch(object):
    def __init__(self, listOfEdges, directed=False):
        """
        self.edges: dict {vertex: [vertex]}
        self.vertices dict {vertex: [bool if explored]}
        :param listOfEdges: list [(vertex, vertex)]
               directed: bool if graph is directed or not
        """
        self.edges, self.vertices = self.makeDict(listOfEdges, directed)
        self.vertList = list(self.vertices.keys())
        self.directed = directed
        self.listOfEdges = listOfEdges

    def __str__(self):
        str1 = 'vertices: ' + str(self.vertices) + '\nedges: ' + str(self.edges)
        return str1

    def __repr__(self):
        return self.__str__()

    def __iter__(self):
        return self.edges.__iter__()

    def keys(self):
        return self.edges.keys()

    def __getitem__(self, item):
        return self.edges.__getitem__(item)

    def __len__(self):
        return len(self.vertices.items())

    def makeDict(self, listOfEdges, directed):
        fromVert = {}
        vertices = {}
        for pair in listOfEdges:
            if pair[0] not in fromVert.keys():
                fromVert[pair[0]] = [pair[1]]
            else:
                fromVert[pair[0]].append(pair[1])
            if not directed:
                if pair[1] not in fromVert.keys():
                    fromVert[pair[1]] = [pair[0]]
                else:
                    fromVert[pair[1]].append(pair[0])
            else:
                if pair[1] not in fromVert.keys():
                    fromVert[pair[1]] = []

            vertices[pair[0]] = False
            vertices[pair[1]] = False

        return fromVert, vertices

    def makeBackDict(self):
        fromVert = {}
        if not self.directed:
            raise ValueError('Graph must be directed')
        for pair in self.listOfEdges:
            if pair[1] not in fromVert.keys():
                fromVert[pair[1]] = [pair[0]]
            else:
                fromVert[pair[1]].append(pair[0])
            if pair[0] not in fromVert.keys():
                fromVert[pair[0]] = []

        return fromVert

    def bfs(self, s):
        """
        breadth first search
        :param s: start node
        :return: list of nodes in the order traversed [node]
        """
        q = queue.Queue()
        q.put(s)
        self.vertices[s] = True
        result = []
        while not q.empty():
            v = q.get()
            result.append(v)
            for node in set(self.edges[v]):
                if not self.vertices[node]:
                    q.put(node)
                    self.vertices[node] = True

        return result

    def shortestPath(self, s, f):
        g = copy.deepcopy(self)
        q = queue.Queue()
        q.put(s)
        distances = dict(zip(list(g.vertices.keys()), ['inf'] * len(g)))
        distances[s] = 0
        g.vertices[s] = True
        while not q.empty():
            v = q.get()
            for nbr in set(g.edges[v]):
                if not g.vertices[nbr]:
                    distances[nbr] = distances[v] + 1
                    q.put(nbr)
                    g.vertices[nbr] = True

        return distances[f]

    def getConnectComp(self):
        components = []
        for node in self.vertList:
            if not self.vertices[node]:
                components.append(self.bfs(node))

        return components

    def dfs(self, s):
        q = []
        q.append(s)
        self.vertices[s] = True
        result = []
        while not q == []:
            v = q.pop()
            result.append(v)
            for node in set(self.edges[v]):
                if not self.vertices[node]:
                    q.append(node)
                    self.vertices[node] = True

        return result

    def reverseDfs(self, s):
        self.backEdges = self.makeBackDict()
        q = []
        q.append(s)
        self.vertices[s] = True
        result = []
        while not q == []:
            v = q.pop()
            result.append(v)
            for node in set(self.backEdges[v]):
                if not self.vertices[node]:
                    q.append(node)
                    self.vertices[node] = True

        return result

    def topSort1(self):
        result = []
        self.backEdges = self.makeBackDict()
        while not self.vertList == []:
            for key in self.vertList:
                value = self.edges[key]
                if value == []:
                    result.insert(0, key)

                    for node in self.backEdges[key]:
                        for nbr in self.edges[node]:
                            if nbr == key:
                                self.edges[node].remove(nbr)
                    del self.edges[key]
                    del self.backEdges[key]
                    self.vertList.remove(key)

        return result

    def topSortDFS(self):
        def dfs(g, node):
            nonlocal  currLbl
            g.vertices[node] = True
            for nbr in g.edges[node]:
                if not g.vertices[nbr]:
                    dfs(g, nbr)
            output[currLbl] = node
            currLbl -= 1

        output = {}
        currLbl = len(self)
        for node in self.edges.keys():
            if not self.vertices[node]:
                dfs(self, node)
        return output

    def kosaraju(self):
        def localDfs(g, node):
            nonlocal s
            nonlocal t
            g.vertices[node] = True
            leaders.append((node, s))
            for nbr in g.backEdges[node]:  # make it back
                if not g.vertices[nbr]:
                    localDfs(g, nbr)
            t += 1
            print(node, t)
            times.append((node, t))

        t = 0
        s = 0
        times = []
        leaders = []
        vertices = self.vertList.copy()
        vertices.sort(reverse=True)
        # first pass (on reverse graph)
        g = copy.deepcopy(self)
        g.backEdges = g.makeBackDict()  # uncomment
        for vrt in vertices:
            if not g.vertices[vrt]:
                s = vrt
                localDfs(g, vrt)
        times.sort(key=lambda x: x[1], reverse=True)
        rs = []
        for pair in times:
            if not self.vertices[pair[0]]:
                rs.append(self.dfs(pair[0]))

        print('leaders', leaders)
        print('times', times)
        return rs


listOfEdges = [(1, 2), (1, 3), (2, 3), (2, 4), (3, 4), (4, 3), (4, 2), (1, 5), (5, 6), (6, 3), (3, 5)]
loe2 = [(1, 2), (1, 3), (3, 2), (2, 4), (3, 4), (3, 5), (4, 6), (5, 4), (5, 6)]
loe3 = [(1, 3), (1, 5), (3, 5), (5, 7), (5, 9), (2, 4), (6, 8), (6, 10)]
cc = [(7, 1), (4, 7), (1, 4), (9, 7), (6, 9), (9, 3), (3, 6), (8, 6), (2, 8), (5, 2), (8, 5)]
ccr = [(1, 7), (7, 4), (4, 1), (7, 9), (9, 6), (3, 9), (6, 3), (6, 8), (8, 2), (2, 5), (5, 8)]

g1 = GraphForSearch(listOfEdges)
g2 = GraphForSearch(listOfEdges, True)
g3 = GraphForSearch(loe2)
g4 = GraphForSearch(loe2, True)
g5 = GraphForSearch(loe3, False)
g6 = GraphForSearch(cc, True)
