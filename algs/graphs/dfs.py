from sys import argv
from graph import Graph

class DepthFirstSearch:
    def __init__(self, graph: Graph, source_vertex):
        self._marked = [False] * graph._V
        self._count = 0
        self._dfs(graph, source_vertex)

    def _dfs(self, graph, source_vertex):
        self._marked[source_vertex] = True
        self._count += 1
        for w in graph.adj(source_vertex):
            if not self._marked[w]:
                self._dfs(graph, w)

    def connections(self):
        return set([i for i in range(len(self._marked)) if self._marked[i]])

    def is_connected(self):
        return self._count == len(self._marked)


def main():
    if 'ut' in argv:
        with open('data/tinyG.txt') as f:
            lines = [list(map(int,line.split())) for line in f.readlines()]
            V = lines[0][0]
            E = lines[1][0]
        G = Graph(V)
        for i in range(2,len(lines)):
            v,w = lines[i]
            G.add_edge(v,w)
        search = DepthFirstSearch(G,9)
        print(search.connections())
        print(search.is_connected())



if __name__ == '__main__':
    main()