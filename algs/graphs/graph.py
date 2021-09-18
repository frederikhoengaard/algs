from sys import argv

class Graph:
    """
    The Graph class represents an undirected, unweighted Graph of vertices as an adjacency list of sets.

    Each index of the adjacency list thus represents a vertex and the element at that index is thus a set
    of the vertices adjacent to the vertex v at index i. The V vertices are named from 0 through V-1.

    Given that the implementation uses an adjancency list of sets to represent the graph, one self-loop is 
    allowed for each vertex. No parallel edges are allowed. It supports methods for adding, deleting and 
    checking whether edges exists between two vertices as well as methods for retrieving the degree and 
    adjacent vertices of a given vertex. 
    
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
        """
        self._adj[v].add(w) 
        self._adj[w].add(v) 
        self._E += 1

    def delete_edge(self, v: int, w: int) -> None:
        """
        Deletes the undirected edge between vertex v and w from the graph.
        """
        if w in self._adj[v] and v in self._adj[w]:
            self._adj[v].remove(w)
            self._adj[w].remove(v)

    def has_edge(self, v: int, w: int) -> bool: 
        """
        Checks whether an edge exists between vertices v and w.
        """
        if w in self._adj[v] and v in self._adj[w]:
            return True
        return False

    def get_n_vertices(self) -> int:
        return self._V

    def get_n_edges(self) -> int:
        return self._E

    def adj(self, v: int) -> set():
        """
        Returns the vertices adjacent to vertex v.
        """
        self._validate_vertex(v)
        return self._adj[v]

    def degree(self, v):
        """
        Returns the degree of vertex v.
        """
        self._validate_vertex(v)
        return len(self._adj[v])

    def __repr__(self):
        """
        Returns a string representation of this graph.
        """
        s = ["Undirected graph with {} vertices and {} edges as below:\n".format(self._V, self._E)]
        for v in range(self._V):
            s.append("%d : " % (v))
            for w in self._adj[v]:
                s.append("%d " % (w))
            s.append("\n")

        return "".join(s)


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
        print(G.has_edge(9,12))
        G.delete_edge(9,12)
        print(G.has_edge(9,12))
        print(G.__repr__())


if __name__ == '__main__':
    main()