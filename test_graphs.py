import graphs as gr
import unittest
import numpy as np


class Test_Iint(unittest.TestCase):
    def setUp(self):
        self.list_of_edges_uni = [(0, 1, 0.5), (0, 3, 1), (1, 2, 1), (2, 3, 0.1)]
        self.vertices_uni = {0, 1, 2, 3}
        self.list_of_edges_bi = [
            (0, 1, 1), (2, 3, 1)
        ]
        self.vertices_bi = {0, 1, 2, 3, 4}

        self.udg_uni = gr.Graph(self.vertices_uni, self.list_of_edges_uni, directed=False)
        self.dg_uni = gr.Graph(self.vertices_uni, self.list_of_edges_uni, directed=True)

        self.udg_bi = gr.Graph(self.vertices_bi, self.list_of_edges_bi, directed=False)
        self.dg_bi = gr.Graph(self.vertices_bi, self.list_of_edges_bi, directed=True)

    def test_udg_vertices(self):
        self.assertEqual(self.udg_uni.vertices, {0, 1, 2, 3})

    def test_dg_vertices(self):
        self.assertEqual(self.dg_uni.vertices, {0, 1, 2, 3})

    def test_udg_vertices_bi(self):
        self.assertEqual(self.udg_bi.vertices, self.vertices_bi)

    def test_dg_vertices_bi(self):
        self.assertEqual(self.dg_bi.vertices, self.vertices_bi)

    def test_udg_dict_uni(self):
        d = {
            0: {(1, 0.5), (3, 1)},
            1: {(0, 0.5), (2, 1)},
            2: {(1, 1), (3, 0.1)},
            3: {(0, 1), (2, 0.1)}
        }
        self.assertEqual(self.udg_uni.edges, d)

    def test_dg_dict_uni(self):
        d = {
            0: {(1, 0.5), (3, 1)},
            1: {(2, 1), },
            2: {(3, 0.1), },
            3: set([])
        }
        self.assertEqual(self.dg_uni.edges, d)

    def test_udg_dict_bi(self):
        d = {
            0: {(1, 1), },
            1: {(0, 1), },
            2: {(3, 1), },
            3: {(2, 1), },
            4: set([])
        }
        self.assertEqual(self.udg_bi.edges, d)

    def test_dg_dict_bi(self):
        d = {
            0: {(1, 1), },
            1: set([]),
            2: {(3, 1), },
            3: set([]),
            4: set([])
        }
        self.assertEqual(self.dg_bi.edges, d)


class Test_Dijkstra(unittest.TestCase):
    def setUp(self):
        self.list_of_edges_uni = [(0, 1, 0.5), (0, 3, 1), (1, 2, 1), (2, 3, 0.1)]
        self.vertices_uni = {0, 1, 2, 3}

        self.list_of_edges_bi = [(0, 1, 1), (2, 3, 1)]
        self.vertices_bi = {0, 1, 2, 3, 4}

        self.edges_simple = [(0, 1, 2)]
        self.verts_simple = {0, 1}

        self.uni = gr.Graph(self.vertices_uni, self.list_of_edges_uni, directed=False)
        self.bi = gr.Graph(self.vertices_bi, self.list_of_edges_bi, directed=False)
        self.simple = gr.Graph(self.verts_simple, self.edges_simple, directed=False)

    def test_simple(self):
        d = {0: 0, 1: 2}
        self.assertEqual(self.simple.dijkstra(0), d)

    def test_uni_0(self):
        d = {0: 0, 1: 0.5, 2: 1.1, 3: 1}
        self.assertEqual(self.uni.dijkstra(0), d)

    def test_uni_1(self):
        d = {0: 0.5, 1: 0, 2: 1, 3: 1.1}
        self.assertEqual(self.uni.dijkstra(1), d)

    def test_bi_0(self):
        d = {0: 0, 1: 1, 2: np.inf, 3: np.inf, 4: np.inf}
        self.assertEqual(self.bi.dijkstra(0), d)

    def test_bi_2(self):
        d = {0: np.inf, 1: np.inf, 2: 0, 3: 1, 4: np.inf}
        self.assertEqual(self.bi.dijkstra(2), d)

    def test_bi_4(self):
        d = {0: np.inf, 1: np.inf, 2: np.inf, 3: np.inf, 4: 0}
        self.assertEqual(self.bi.dijkstra(4), d)


if __name__ == '__main__':
    unittest.main()
