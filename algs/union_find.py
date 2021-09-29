from sys import argv

class UF:
    """
    weighted quick union
    """
    def __init__(self, n: int):
        self.id = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        self._count = n

    def union(self, p: int, q: int) -> None:
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.size[i] < self.size[j]:
            self.id[i] = j
            self.size[j] += self.size[i]
        else:
            self.id[j] = i
            self.size[i] += self.size[j]
        self._count -= 1

    def find(self, p: int) -> int:
        while p != self.id[p]:
            p = self.id[p]
        return p

    def connected(self, p: int, q: int) -> bool:
        self.find(p) == self.find(q)

    def count(self) -> int:
        return self._count


def main():
    if 'ut' in argv:
        with open('data/mediumUF.txt') as f:
            lines = [list(map(int,line.split())) for line in f.readlines()]
            n = lines[0][0]
            
        uf = UF(n)
        for pair in lines[1:]:
            p,q = pair
            if not uf.connected(p,q):
                uf.union(p,q)
                print(p,q)
        print(uf.count(), 'components')

if __name__ == '__main__':
    main()