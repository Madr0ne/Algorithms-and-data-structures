class LinkedStack:
    class _Node:
        __slots__='_element', '_next'

        def __init__(self, data, n = None):
            self._element = data
            self._next = n

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, data):
        self._head = self._Node(data, self._head)
        self._size += 1

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        h = self._head._element
        self._head = self._head._next
        self._size -= 1
        return h
