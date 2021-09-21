from sys import argv


class Node:
    def __init__(self):
        self.value = None
        self.next = None


class Queue:
    """
    The Queue class represents a linked-list implementation of the 
    FIFO queue as originally described in Algorithms, Sedgewick & Wayne, 4ed
    on p. 151 with the addition of an iterator method. 

    All methods including instantiation are constant time operations.
    """
    def __init__(self):
        self.first = None
        self.last = None
        self.n = 0

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n

    def enqueue(self,item: Node) -> None:
        old_last = self.last
        self.last = Node()
        self.last.item = item
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.n += 1

    def dequeue(self) -> Node:
        item = self.first.item
        self.first = self.first.next
        if self.is_empty():
            self.last = None
        self.n -= 1
        return item

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.next


def main():
    if 'ut' in argv:
        queue = Queue()
        for i in range(0,10,2):
            queue.enqueue(i)
        print(queue.n)
        for _ in range(2):
            print(queue.dequeue())
        print(queue.n)
        for item in queue:
            print(item)

if __name__ == '__main__':
    main()
