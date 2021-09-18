from sys import argv

class Graph:
    """
    The Graph class represents an undirected, unweighted Graph of vertices as an adjacency list of sets.

    Each index of the adjacency list thus represents a vertex and the element at that index is thus a set
    of the vertices adjacent to the vertex v at index i. The V vertices are named from 0 through V-1.
    
    """


    def __init__(self, V: int):
        if V < 0:
            raise ValueError("Cannot instantiate a graph with a negative number of vertices!")
        self._V = V  
        self._E = 0  
        self._adj = [set() for _ in range(V)]  


    def _validate_vertex(self, v: int) -> None:
        if v < 0 or v >= self._V:
            raise ValueError("vertex {} is not between 0 and {}".format(v, self._V))

    def add_edge(self, v: int, w: int) -> None:
        """
        Adds an undirected edge between vertex v and w to the graph.

        :param v: one vertex in the edge
        :param w: the other vertex in the edge
        :raises ValueError: unless both 0 <= v < V and 0 <= w < V
        """
        self._adj[v].add(w) 
        self._adj[w].add(v) 
        self._E += 1

    def get_n_vertices(self) -> int:
        return self._V

    def get_n_edges(self) -> int:
        return self._E

    def adj(self, v: int) -> set():
        """
        Returns the vertices adjacent to vertex v.

        :param v: the vertex
        :returns: the vertices adjacent to vertex v, as an iterable
        :raises ValueError: unless  0 <= v < V
        """
        self._validate_vertex(v)
        return self._adj[v]

    def degree(self, v):
        """
        Returns the degree of vertex v.

        :param v: the vertex
        :returns: the degree of vertex v
        :raises ValueError:  unless 0 <= v < V
        """
        self._validate_vertex(v)
        return self._adj[v].size()

    def __repr__(self):
        """
        Returns a string representation of this graph.

        :returns: the number of vertices V, followed by the number of edges E,
                  followed by the V adjacency lists
        """
        s = ["{} vertices, {} edges\n".format(self._V, self._E)]
        for v in range(self._V):
            s.append("%d : " % (v))
            for w in self._adj[v]:
                s.append("%d " % (w))
            s.append("\n")

        return "".join(s)


def main():
    if 'ut' in argv:
        G = Graph(5)
        edges = [(0,1),(0,2),(2,1),(1,3),(3,0),(3,4)]
        for edge in edges:
            v,w = edge
            G.add_edge(v,w)

        print(G.__repr__)


if __name__ == '__main__':
    main()