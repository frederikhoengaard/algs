from sys import argv


class Node:
    def __init__(self):
        self.value = None
        self.next = None
        self.previous = None


class Queue:
    """
    The Queue class represents a linked-list implementation of the 
    FIFO queue as originally described in Algorithms, Sedgewick & Wayne, 4ed
    on p. 151 with the addition of iterator and contains methods. 

    All methods including instantiation are constant time operations.
    """
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.n = 0

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n

    def enqueue(self,item) -> None:
        old_last = self.last
        self.last = Node()
        self.last.item = item
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.n += 1

    def dequeue(self) -> Node:
        if self.is_empty():
            raise ValueError("Cannot dequeue from empty queue")
        item = self.first.item
        self.first = self.first.next
        self.n -= 1
        if self.is_empty():
            self.last = None
        return item

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.next

    def __contains__(self, compare_item) -> bool:
        if not self.is_empty():
            for item in self:
                if item == compare_item:
                    return True
        return False


class Deque():
    """
    The Deque class represents a linked-list implementation of the 
    doubled-ended queue as originally described in Algorithms, Sedgewick & Wayne, 4ed
    on p. 167 with the addition of iterator and contains methods. 

    All methods including instantiation are constant time operations.
    """
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.n: int = 0

    def is_empty(self) -> bool:
        return self.n == 0

    def size(self) -> int:
        return self.n

    def push_left(self, item) -> None:
        old_first = self.first
        self.first = Node()
        self.first.item = item
        if self.is_empty():
            self.last = self.first
        else:
            self.first.next = old_first
            old_first.previous = self.first
        self.n += 1

    def push_right(self, item) -> None:
        old_last = self.last
        self.last = Node()
        self.last.item = item
        self.last.previous = old_last
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last
        self.n += 1

    def pop_left(self) -> Node:
        if self.is_empty():
            raise ValueError("Cannot dequeue from empty queue")
        old_first = self.first
        self.first = old_first.next
        self.n -= 1
        if self.is_empty():
            self.last = None
        else:
            self.first.previous = None
        return old_first.item

    def pop_right(self) -> Node:
        if self.is_empty():
            raise ValueError("Cannot dequeue from empty queue")
        old_last = self.last
        self.last = old_last.previous
        self.n -= 1
        if self.is_empty():
            self.first = None
        else:
            self.last.next = None
        return old_last.item

    def __iter__(self):
        current = self.first
        while current is not None:
            yield current.item
            current = current.next
    
    def __contains__(self, compare_item) -> bool:
        if not self.is_empty():
            for item in self:
                if item == compare_item:
                    return True
        return False


def main():
    if 'ut' in argv:
        # unit test for Queue:
        queue = Queue()
        for i in range(0,10,2):
            queue.enqueue(i)
        print('Items in queue:',queue.n)
        for _ in range(2):
            print('Dequeueing:',queue.dequeue())
        print('Items in queue',queue.n)
        print('Queue is: ', end="")
        for item in queue:
            print(item, end=" ")
        print('\nIs 7 in the queue?',7 in queue)
        print('Is 7 not in the queue?',7 not in queue)
        print('Is 8 in the queue?',8 in queue)
        print('======')

        # unit test for Deque
        deque = Deque()
        for i in range(0,10):
            if i % 2 == 0:
                print('Pushing right:',i)
                deque.push_right(i)
            else:
                print('Pushing left:',i)
                deque.push_left(i)
        print('Deque is: ', end="")
        for item in deque:
            print(item, end=" ")
        print('\nPopping leftmost item:',deque.pop_left())
        print('Deque is: ', end="")
        for item in deque:
            print(item, end=" ")
        print('\nPopping rightmost item:',deque.pop_right())
        print('Deque is: ', end="")
        for item in deque:
            print(item, end=" ")


if __name__ == '__main__':
    main()
