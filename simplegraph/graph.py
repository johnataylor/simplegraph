
class GraphValue:
    def __init__(self, value, is_ref=False):
        self.value = value
        self.is_ref = is_ref

    def __hash__(self):
        return hash((self.value, self.is_ref))

    def __eq__(self, other):
        return (self.value, self.is_ref) == (other.value, other.is_ref)

    def __str__(self):
        return str(self.value) if not self.is_ref else '<' + str(self.value) + '>'

class Triple:
    def __init__(self, s, p, o):
        self.s = s
        self.p = p
        self.o = o

class Graph:
    def __init__(self):
        self._spo = {}
        self._pos = {}
        self._osp = {}
        self.count = 0

    def __len__(self):
        return self.count

    def merge(self, graph):
        for t in graph.triples():
            self.add(t.s, t.p, t.o)

    def add(self, s, p, o):
        Graph.__add_to_index(self._spo, s, p, o)
        Graph.__add_to_index(self._pos, p, o, s)
        if Graph.__add_to_index(self._osp, o, s, p):
            self.count += 1

    def remove(self, s, p, o):
        pass

    @staticmethod
    def __add_to_index(index, x, y, z):
        if x not in index:
            index[x] = {y:{z}}
            return True            
        if y not in index[x]:
            index[x][y] = {z}
            return True
        s = index[x][y]
        before = len(s)
        s.add(z)
        after = len(s)
        return after > before

    def triples(self):
        for s in self._spo:
            for p in self._spo[s]:
                for o in self._spo[s][p]:
                    yield Triple(s, p, o)

    def get_by_subject(self, s):
        if s in self._spo:
            for p in self._spo[s]:
                for o in self._spo[s][p]:
                    yield Triple(s, p, o)
        
    def get_by_subject_predicate(self, s, p):
        if s in self._spo and p in self._spo[s]:
            for o in self._spo[s][p]:
                yield Triple(s, p, o)

    def get_by_predicate(self, p):
        if p in self._pos:
            for o in self._pos[p]:
                for s in self._pos[p][o]:
                    yield Triple(s, p, o)

    def get_by_predicate_object(self, p, o):
        if p in self._pos and o in self._pos[p]:
            for s in self._pos[p][o]:
                yield Triple(s, p, o)

    def get_by_object(self, o):
        if o in self._osp:
            for s in self._osp[o]:
                for p in self._osp[o][s]:
                    yield Triple(s, p, o)

    def get_by_object_subject(self, o, s):
        if o in self._osp and s in self._osp[o]:
            for p in self._osp[o][s]:
                yield Triple(s, p, o)

    def contains(self, t):
        if t.s in self._spo:
            tpo = self._spo[t.s]
            if t.p in tpo:
                to = tpo[t.p]
                return t.o in to
        return False

    def contains_graph(self, g):
        for t in g.triples():
            if not self.contains(t):
                return False
        return True

    def equals(self, g):
        if len(self) != len(g):
            return False
        return self.contains_graph(g)

def print_triple(t):
    print('<' + str(t.s) + '> <' + str(t.p) + '> ' + str(t.o))

def print_graph(graph):
    for t in graph.triples():
        print_triple(t)
