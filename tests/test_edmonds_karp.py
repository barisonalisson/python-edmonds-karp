import unittest
from edmonds_karp  import EdmondsKarp

class TestEdmondsKarp(unittest.TestCase):

    def test_graph_without_edges(self):
        capacity = [[0, 0], [0, 0]]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 1), 0)

    def test_graph_with_single_edge(self):
        capacity = [[0, 1], [0, 0]]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 1), 1)

    def test_graph_with_multiple_edges(self):
        capacity = [
            [0, 10, 10],
            [0, 0, 5],
            [0, 0, 0]
        ]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 2), 15)

    def test_graph_with_max_capacity(self):
        capacity = [
            [0, float('Inf')],
            [0, 0]
        ]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 1), float('Inf'))

    def test_graph_with_min_capacity(self):
        capacity = [[0, 1], [0, 0]]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 1), 1)

    def test_graph_with_negative_capacity(self):
        capacity = [[0, -1], [0, 0]]
        with self.assertRaises(ValueError):
            EdmondsKarp(capacity)

    def test_graph_with_infinite_capacity(self):
        capacity = [
            [0, float('Inf')],
            [0, 0]
        ]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 1), float('Inf'))

    def test_graph_with_zero_capacity(self):
        capacity = [[0, 0], [0, 0]]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 1), 0)

    def test_graph_with_varied_capacity(self):
        capacity = [
            [0, 5, 10],
            [0, 0, 15],
            [0, 0, 0]
        ]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 2), 15)

    def test_graph_with_equal_capacity(self):
        capacity = [
            [0, 5, 5],
            [0, 0, 5],
            [0, 0, 0]
        ]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 2), 10)

    def test_graph_with_different_capacity(self):
        capacity = [
            [0, 10, 5],
            [0, 0, 15],
            [0, 0, 0]
        ]
        ek = EdmondsKarp(capacity)
        self.assertEqual(ek.find_max_flow(0, 2), 15)

    def test_graph_with_negative_and_positive_capacity(self):
        capacity = [
            [0, -5, 10],
            [0, 0, 5],
            [0, 0, 0]
        ]
        with self.assertRaises(ValueError):
            EdmondsKarp(capacity)

if __name__ == "__main__":
    unittest.main()
