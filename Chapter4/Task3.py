class StackBasedQueue():
    def __init__(self):
        self._size = 0
        self._InboundStack = []
        self._OutboundStack = []
    # YOUR CODE HERE

    def __repr__(self):
        plural = '' if self._size == 1 else 's'
        values = [c for c in self._InboundStack[::-1]]
        values.extend([c for c in self._OutboundStack])
        return f'<StackBasedQueue ({self._size} element{plural}): [{", ".join(values)}]>'

    def enqueue(self, data):
        self._InboundStack.append(data)
        self._size += 1
    # YOUR CODE HERE

    def dequeue(self):
        if self._size == 0:
            return None
        if not self._OutboundStack:
            for _ in range(self._size):
                value = self._InboundStack.pop()
                self._OutboundStack.append(value)

        value = self._OutboundStack.pop()
        self._size -= 1
        return value
    # YOUR CODE HERE


