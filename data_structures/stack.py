"""

Stack:

Linear data structure with sequential access. It is a collection of objects that supports fast last-in,
first-out (LIFO) semantics for insertion and deletion.


Operations:

empty() – Returns whether the stack is empty – Time Complexity: O(1)
top() / peek() – Returns a copy or reference to the topmost element of the stack – Time Complexity: O(1)
push(a) – Inserts the element ‘a’ at the top of the stack – Time Complexity: O(1)
pop() – Deletes the topmost element of the stack – Time Complexity: O(1)

Attributes:
size_ – Returns the size of the stack – Time Complexity: O(1)

Example application: Undo operation.

"""

from copy import deepcopy
from typing import (
    Any,
    Optional
)


class Node:

    def __init__(self, value: Any):

        self.value: Any = value
        self.next: Optional[Any] = None


class Stack:

    def __init__(self):

        self.head: Node = Node("head")
        self.size_: int = 0

    def __str__(self):

        curr: Any = self.head.next
        out: str = f""

        while curr:
            out += f"{curr.value} -> "
            curr = curr.next
        return out[:-4]

    def push(self, value: Any):

        # Step 1. Instantiate new Node in the stack
        node = Node(value)

        # Step 2. Add the previous head value to next of node
        node.next = self.head.next

        # Step 3. Add the node to next
        self.head.next = node

        # Step 4. Increment the size
        self.size_ += 1

    def pop(self) -> Any:

        # Step 1. Raise Exception if the stack is empty
        if self.size_ == 0:
            raise Exception("Cannot pop values out of empty stack !")

        # Step 2. Get the top-most value to pop
        node: Node = self.head.next

        # Step 3. Set the next value as the new top
        self.head.next = self.head.next.next

        return node.value

    def top(self):
        # Return a copy of the top-most value
        return deepcopy(self.head.next.value)

    def peek(self):
        # Return a reference to the top-most value
        return self.head.next.value


if __name__ == "__main__":

    stack = Stack()

    for i in range(10):
        stack.push(i)

    print(f"Stack: {stack}")

    for _ in range(9):
        stack.pop()

    print(f"Stack: {stack}")
