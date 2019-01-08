import gr
import unittest
import ddt


class Test_Init(unittest.TestCase):
    def setUp(self):
        self.list_of_edges_uni = [(0, 1, 0.5), (0, 2, 1), (1, 2, 1)]
        self.vertices_uni = {0, 1, 2}
        self.list_of_edges_bi = [
            (0, 1, 1), (2, 3, 1)
        ]
        self.vertices_bi = {0, 1, 2, 3, 4}

        self.udg_uni = gr.Graph(self.vertices_uni, self.list_of_edges_uni, directed=False)
        self.dg_uni = gr.Graph(self.vertices_uni, self.list_of_edges_uni, directed=True)

        self.udg_bi = gr.Graph(self.vertices_bi, self.list_of_edges_bi, directed=False)
        self.dg_bi = gr.Graph(self.vertices_bi, self.list_of_edges_bi, directed=True)

    def test_udg_vertices(self):
        self.assertEqual(self.udg_uni.vertices, {0, 1, 2})

    def test_dg_vertices(self):
        self.assertEqual(self.dg_uni.vertices, {0, 1, 2})

    def test_udg_vertices_bi(self):
        self.assertEqual(self.udg_bi.vertices, self.vertices_bi)

    def test_dg_vertices_bi(self):
        self.assertEqual(self.dg_bi.vertices, self.vertices_bi)

    def test_udg_dict(self):
        d = {
            0: {(1, 0.5), (2, 1)},
            1: {(0, 0.5), (2, 1)},
            2: {(0, 1), (1, 1)}
        }
        self.assertEqual(self.udg_uni.edges, d)

    def test_dg_dict(self):
        d = {
            0: {(1, 0.5), (2, 1)},
            1: {(2, 1), },
            2: set([])
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
 

if __name__ == '__main__':
    unittest.main()
    

