from __future__ import annotations
from typing import Any


class Node:
    data: Any
    next: Node | None
    prev: Node | None

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
        self.prev = None

    def set_next(self, next: Node | None) -> None:
        self.next = next

    def set_prev(self, prev: Node | None) -> None:
        self.prev = prev


class DoublyLinkedList:
    head: Node
    tail: Node

    def __init__(self, head: Node, tail: Node):
        self.head = head
        self.tail = tail

    def push(self, new_data: Any) -> None:
        """
        Insert new node as the head of the list.
        """
        new_head = Node(new_data)

        new_head.set_next(self.head)
        self.head.set_prev(new_head)

        self.head = new_head

    def insert_after(self, orig_node: Node, new_data: Any) -> None:
        """
        Insert new node after specified node.
        """
        new_node = Node(new_data)

        new_node.set_next(orig_node.next)
        new_node.set_prev(orig_node)

        if orig_node.next is not None:
            orig_node.next.set_prev(new_node)

        orig_node.set_next(new_node)

    def append(self, new_data: Any) -> None:
        """
        Insert new node at the end of the list.
        """
        new_tail = Node(new_data)

        new_tail.set_prev(self.tail)
        self.tail.set_next(new_tail)

        self.tail = new_tail

    def print_list(self, reverse: bool = False) -> None:
        print("Reading list values:\n")

        if not reverse:
            cur_node = self.head
            while cur_node:
                print(f"Node data: {cur_node.data}")
                if cur_node.next is None:
                    break

                cur_node = cur_node.next

        else:
            cur_node = self.tail
            while cur_node:
                print(f"Node data: {cur_node.data}")
                if cur_node.prev is None:
                    break

                cur_node = cur_node.prev

        print("\nEnd of list reached.")


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.set_next(b)
    b.set_prev(a)

    b.set_next(c)
    c.set_prev(b)

    doubly_linked_list = DoublyLinkedList(a, c)
    doubly_linked_list.print_list()

    print("#"*50)

    doubly_linked_list.append(4)
    doubly_linked_list.insert_after(b, 2.5)
    doubly_linked_list.push(0)


    doubly_linked_list.print_list()
    print("#"*50)
    doubly_linked_list.print_list(reverse=True)
