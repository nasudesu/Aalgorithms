class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        """
        Float the last element of the heap until the heap is in order
        """
        index = self._size - 1
        parent = (index - 1) // 2
        while index > 0 and self._heap[index] < self._heap[parent]:
            self._heap[index], self._heap[parent] = self._heap[parent], self._heap[index]
            index = parent
            parent = (index - 1) // 2



h = Heap()
h._heap = [3, 6, 5, 9, 7, 8, 2]
h._size = 7
print(h._heap)
h._float()
print(h._heap)
