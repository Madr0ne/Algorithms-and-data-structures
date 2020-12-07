class LinkedQueue:
    class _Node:
        __slots__ = '_data', '_next'

        def __init__(self, data, n=None):
            self._data = data
            self._next = n

    def __init__(self):
        self._front = None
        self._rear = None
        self._length = 0

    def __len__(self):
        return self._length

    def is_empty(self):
        return self._length == 0

    def peek(self):
        if self.is_empty():
            raise Exception('queue is empty')
        return self._front._data

    def enqueue(self, data):
        new_node = self._Node(data)
        if self.is_empty():
            self._front = new_node
        else:
            self._rear._next = new_node
        self._rear = new_node
        self._length += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('queue is empty')
        n = self._front._data
        self._front = self._front._next
        self._length -= 1
        if self.is_empty():
            self._rear = None
        return n
