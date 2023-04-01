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

def preorder_traversal(tree: Node):
    """
    Visit the root node first, then recursively do a preorder traversal of the left subtree, followed by a recursive preorder traversal of the right subtree.
    """
    if tree:
        print(tree.value)
        preorder_traversal(tree.left)
        preorder_traversal(tree.right)

def postorder_traversal(tree: Node):
    """
    We recursively do a postorder traversal of the left subtree and the right subtree followed by a visit to the root node.
    """
    if tree:
        postorder_traversal(tree.left)
        postorder_traversal(tree.right)
        print(tree.value)

def inorder_traversal(tree: Node):
    """
    We recursively do an inorder traversal on the left subtree, visit the root node, and finally do a recursive inorder traversal of the right subtree.
    """
    if tree:
        inorder_traversal(tree.left)
        print(tree.value)
        inorder_traversal(tree.right)


if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    n3.set_left(n4)
    n3.set_right(n5)

    n1.set_left(n2)
    n1.set_right(n3)

    n1.print_children()

    n2.print_children()

    print("#"*50)
    preorder_traversal(n1)

    print("#"*50)
    postorder_traversal(n1)

    print("#"*50)
    inorder_traversal(n1)