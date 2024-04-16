class Heap:
    def __init__(self):
        self._heap = []
        self._size = 0

    def _float(self):
        # Start at the end of the heap
        index = self._size - 1
        # Calculate index of parent element
        parent_index = (index - 1) // 2
        # While not at Root node and value less than its parent
        while index > 0 and self._heap[index] < self._heap[parent_index]:
            # swap value with its parent
            self._heap[index], self._heap[parent_index] = self._heap[parent_index], self._heap[index]
            # Update indices
            index = parent_index
            parent_index = (index - 1) // 2

    def insert(self, value):
        # Add the value to the heap
        self._heap.append(value)
        # Update size of the heap
        self._size += 1
        # And float the last element of the heap
        self._float()

    def _sink(self):
        """
        Sinks the root node of the heap until the heap is in order
        """
        sink_index = 0
        c1, c2 = sink_index * 2 + 1, sink_index * 2 + 2
        has_left_child = True if c1 < self._size else False
        has_right_child = True if c2 < self._size else False
        while has_left_child or has_right_child:
            if has_left_child and has_right_child:
                if self._heap[sink_index] < self._heap[c1] and self._heap[sink_index] < self._heap[c2]: break
                smaller_child_index = c1 if self._heap[c1] < self._heap[c2] else c2
                self._heap[sink_index], self._heap[smaller_child_index] = self._heap[smaller_child_index], self._heap[sink_index]
                sink_index = smaller_child_index
            elif has_left_child:
                if self._heap[sink_index] < self._heap[c1]: break
                self._heap[sink_index], self._heap[c1] = self._heap[c1], self._heap[sink_index]
                sink_index = c1
            else:
                if self._heap[sink_index] < self._heap[c2]: break
                self._heap[sink_index], self._heap[c2] = self._heap[c2], self._heap[sink_index]
                sink_index = c2
            c1, c2 = sink_index * 2 + 1, sink_index * 2 + 2
            has_left_child = True if c1 < self._size else False
            has_right_child = True if c2 < self._size else False
        #sink_index = 0
        #while 2 * sink_index + 1 < self._size:
        #    c1, c2 = 2 * sink_index + 1, 2 * sink_index + 2
        #    smaller_child_index = c1
#
        #    if c2 < self._size and self._heap[c2] < self._heap[c1]:
        #        smaller_child_index = c2
#
        #    if self._heap[sink_index] <= self._heap[smaller_child_index]:
        #        break
#
        #    self._heap[sink_index], self._heap[smaller_child_index] = self._heap[smaller_child_index], self._heap[
        #        sink_index]
        #    sink_index = smaller_child_index


h = Heap()
h._heap = [25, 10, 20, 30, 40, 50, 60]
h._size = 7
h._sink()
print(h._heap)
