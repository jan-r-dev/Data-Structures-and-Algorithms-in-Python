from __future__ import annotations
from typing import Any


class Node:
    data: Any
    next: Node | None

    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None

    def set_next(self, next: Node | None) -> None:
        self.next = next


class SinglyLinkedList:
    head: Node | None

    def __init__(self, head: Node | None = None):
        self.head = head

    def push(self, new_data: Any) -> None:
        """
        Insert new node as the head of the list.
        """
        new_node = Node(new_data)

        new_node.set_next(self.head)
        self.head = new_node

    def insert_after(self, prev_node: Node, new_data: Any) -> None:
        """
        Insert new node after specified node.
        """
        new_node = Node(new_data)

        new_node.set_next(prev_node.next)
        prev_node.set_next(new_node)

    def append(self, new_data: Any) -> None:
        """
        Insert new node at the end of the list.
        """
        new_node = Node(new_data)

        if self.head == None:
            self.head = new_node
            return
        else:
            assert self.head is not None

        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def print_list(self) -> None:
        print("Reading list values:\n")

        cur_node = self.head
        while cur_node:
            print(f"Node data: {cur_node.data}")
            if cur_node.next is None:
                break

            cur_node = cur_node.next

        print("\nEnd of list reached.")


if __name__ == "__main__":
    a = Node(1)
    b = Node(2)
    c = Node(3)

    a.set_next(b)
    b.set_next(c)

    signly_linked_list = SinglyLinkedList(a)
    signly_linked_list.print_list()

    print("#"*50)

    signly_linked_list.append(4)
    signly_linked_list.insert_after(b, 2.5)
    signly_linked_list.push(0)
    signly_linked_list.print_list()
