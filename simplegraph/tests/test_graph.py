
import unittest
from simplegraph import Graph, GraphValue, InferenceRules, print_graph, spin

from .data import graph_a0, graph_a1

class TestGraph(unittest.TestCase):
    def test_len(self):
        g = Graph()
        g.add('s', 'p', GraphValue('o1'))
        g.add('s', 'p', GraphValue('o2'))
        self.assertEqual(len(g), 2)

    def test_idempotency(self):
        g = Graph()
        g.add('s', 'p', GraphValue('o1'))
        g.add('s', 'p', GraphValue('o1'))
        self.assertEqual(len(g), 1)

    def test_get_by_subject(self):
        g = Graph()
        t = graph_a0()
        g.merge(t)
        g.merge(graph_a1())
        r = Graph()
        for s, p, o in g.get_by_subject('a0'):
            r.add(s, p, o)
        self.assertTrue(t.equals(r))

    # def test_inference(self):
    #     g = Graph()
    #     g.add('s0', 'p0', GraphValue('o0', True))
    #     g.add('s0', 'p1', GraphValue('o0', True))
    #     g.add('s0', 'p2', GraphValue('o0', True))
    #     g.add('s0', '@type', GraphValue('T1', True))
    #     s = Graph()
    #     s.add('p0', 'range', GraphValue('T0', True))
    #     s.add('p0', 'domain', GraphValue('T1', True))
    #     s.add('T1', 'subClassOf', GraphValue('T2', True))
    #     rules = InferenceRules.create_from_schema(s)
    #     spin(g, rules)
    #     print()
    #     print_graph(g)

if __name__ == '__main__':
    unittest.main()
