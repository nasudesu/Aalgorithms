class NodeList:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f'<NodeList: {self.data}>'


class Queue:
    def __init__(self):
        self._head = self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def __repr__(self):
        current_node = self._tail  # Start from the tail
        values = ''
        while current_node:
            values += f', {current_node.data}'
            current_node = current_node.prev  # Traverse backwards
        plural = '' if self._size == 1 else 's'
        return f'<Queue ({self._size} element{plural}): [{values.lstrip(", ")}]>'

    def enqueue(self, data):
        new_node = NodeList(data=data, next=None, prev=self._tail)

        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node
        self._size += 1

    def dequeue(self):
        if self._head is None:
            return None

        val = self._head.data

        if self._head == self._tail:
            self._head = self._tail = None
        else:
            self._head = self._head.next
            self._head.prev = None
        self._size -= 1
        return val


def get_pairs(list):
    even_list = Queue()
    odd_list = Queue()
    for number in list:
        if number % 2 == 0:
            even_list.enqueue(number)
        else:
            odd_list.enqueue(number)
    pairs = []
    while len(even_list) > 0 and len(odd_list) > 0:
        pairs.append((even_list.dequeue(), odd_list.dequeue()))
    return pairs

