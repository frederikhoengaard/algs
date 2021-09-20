from sys import argv


class Edge:
    """
    The Edge class represents an edge intended for the construction of a directed, weighted graph.

    Each instance of the class contains the endpoint vertices v and w, where v is the tail vertex and 
    w is the head vertex, and the weight of the edge. 
    """

    def __init__(self, v: int,w: int, weight: float):
        self._v = v
        self._w = w
        self._weight = weight

    def get_weight(self) -> float:
        return self._weight

    def get_endpoints(self) -> tuple:
        return (self._v,self._w)

    def opposite_endpoint(self, vertex: int) -> int:
        if vertex == self._v:
            return self._w
        elif vertex == self._w:
            return self._v
        else:
            raise ValueError('Given vertex not connected by this edge!')

    def __repr__(self) -> str:
        return "Edge from {} to {} with weight {:.5f}".format(self._v, self._w, self._weight)

def main():
    if 'ut' in argv:
        e = Edge(1,2,3.4)
        print(e.get_endpoints())
        print(e.__repr__())

if __name__ == '__main__':
    main()