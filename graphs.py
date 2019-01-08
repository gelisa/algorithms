# Elizaveta Guseva, 2019

from collections import defaultdict
from queue import PriorityQueue
import copy
import numpy as np


class Graph(object):
    def __init__(self, set_of_vertices, list_of_edges, directed=False):
        """
        self.edges: dict {vertex: [vertex]}
        :param list_of_edges: list [(vertex, vertex)]
               directed: bool if graph is directed or not
        """
        self.edges = self.make_dict(list_of_edges, set_of_vertices, directed)
        self.vertices = set_of_vertices
        self.directed = directed
        self.list_of_edges = list_of_edges

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
        return len(self.vertices)

    @staticmethod
    def make_dict(list_of_edges, vertices, directed):
        edges = defaultdict(set)
        for pair in list_of_edges:
            edges[pair[0]].add((pair[1], pair[2]))

            if not directed:
                edges[pair[1]].add((pair[0], pair[2]))
            else:
                if pair[1] not in edges.keys():
                    edges[pair[1]] = set([])

        for vert in vertices:
            if vert not in edges.keys():
                edges[vert] = set([])

        return edges

    # algorithms

    def dijkstra(self, from_vertex):
        pq = PriorityQueue()
        unseen = copy.copy(self.vertices)
        distances = dict([(v, np.inf) for v in self.vertices])
        distances[from_vertex] = 0
        pq.put((0, from_vertex))
        while not pq.empty():
            head_dist, head = pq.get()
            for neigh in self.edges[head]:
                n_id, n_dist = neigh
                distances[n_id] = min(distances[n_id], distances[head] + n_dist)
                if n_id in unseen:
                    pq.put((n_dist, n_id))
            if head in unseen:
                unseen.remove(head)

        return distances



