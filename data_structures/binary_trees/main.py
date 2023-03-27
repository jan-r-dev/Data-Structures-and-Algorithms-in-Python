from __future__ import annotations
from typing import Any


class Node:
    def __init__(self, value: Any, left: None | Node = None, right: None | Node = None) -> None:
        self.left = left
        self.right = right
        self.value = value

    def set_left(self, new_left: Node) -> None:
        self.left = new_left

    def set_right(self, new_right: Node) -> None:
        self.right = new_right

    def print_children(self) -> None:
        print("Printing values of children nodes:")
        print(f"Left:\t{self.left.value if self.left is not None else 'No node'}")
        print(f"Right:\t{self.right.value if self.right is not None else 'No node'}")


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    n1.set_left(n2)
    n1.set_right(n3)

    n1.print_children()

    n2.print_children()
