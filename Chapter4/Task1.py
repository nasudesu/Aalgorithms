class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return f'<Node: {self.data}>'


class Stack:
    def __init__(self):
        self._top = None
        self._size = 0

    def __len__(self):
        return self._size

    def peek(self):
        """
        Returns the value of the top node without altering the stack
        """
        return self._top.data if self._top else None

    def push(self, data):
        """
        Add an element to the stack
        Parameters:
        - 'data': Data/value being added
        Returns: None
        """
        self._top = Node(data, self._top)
        self._size += 1

    def pop(self):
        """
        Remove the top node from the stack and return its content
        Parameters: None
        Returns: The content of the node or None if stack is empty
        """
        if self._size == 0:
            return None
        else:
            top = self._top.data
            self._top = self._top.next
            self._size -= 1
            return top

    def __repr__(self):
        # YOUR CODE HERE. Remove the next line if necessary
        pur = ""
        if self._size > 1 or self._size == 0:
            pur += "s"
        str = ""
        currentNode = self._top
        for i in range(self._size):
            str += f"{currentNode.data}, "
            currentNode = currentNode.next
        str = str.rstrip(", ")
        return f"<Stack ({self._size} element{pur}): [{str}]>"



mystack = Stack()
for c in 'ABC':
    mystack.push(c)
val = mystack.pop()
val = mystack.pop()
val = mystack.pop()
print(val, mystack)
print("A <Stack (0 elements): []>")
