from sys import argv
from graph import Graph

class DepthFirstSearch:
    """
    The DepthFirstSearch class implements a method of finding the vertices 
    connected to a source vertex in an undirected graph - specifically 
    the Graph class from the algs repository.

    To use it, initialise an instance of this class with a graph instance and 
    source vertex represented by an integer as parameters. 

    Then call the connections method to return a set of the vertices to which
    the source vertex is connected.
    """
    def __init__(self, graph: Graph, source_vertex: int):
        self._marked = [False] * graph._V
        self._count = 0
        self._dfs(graph, source_vertex)

    def _dfs(self, graph: Graph, source_vertex: int) -> None:
        self._marked[source_vertex] = True
        self._count += 1
        for w in graph.adj(source_vertex):
            if not self._marked[w]:
                self._dfs(graph, w)

    def connections(self) -> set():
        return set([i for i in range(len(self._marked)) if self._marked[i]])

    def is_connected(self) -> bool:
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
        # should print {9, 10, 11, 12} in any order
        print(search.is_connected())
        # should print False



if __name__ == '__main__':
    main()