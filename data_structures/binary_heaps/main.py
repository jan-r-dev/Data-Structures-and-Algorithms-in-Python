from __future__ import annotations


class BinaryHeap:
    """
    Min heap implementation. In a min heap, the key of P is less than or equal to the key of C.[2] The node at the "top" of the heap (with no parents) is called the root node.
    """

    def __init__(self, values: list[int] | None = None) -> None:
        self.heap_list: list[int] = [0]

        if values:
            self.size = len(values)
            self.heap_list = self.heap_list + values

            half_point = len(values) // 2
            while half_point > 0:
                self.perc_down(half_point)
                half_point -= 1

    def perc_up(self, index: int) -> None:
        """
        Percolate up the list and switch elements as long as the key of the parent node is lower. Ensures that the heap property is satisfied by moving the new node up if needed - in min heap, that the root node is the smallest item in the tree.
        """
        while index // 2 > 0:

            # Swap if parent larger
            if self.heap_list[index] < self.heap_list[index // 2]:
                self.heap_list[index], self.heap_list[index // 2] = self.heap_list[index // 2], self.heap_list[index]

            index = index // 2

    def perc_down(self, new_root_index: int) -> None:
        """
        Percolate down the list and switch elements as long as the key of the parent node is higher. Ensures that the heap property is satisfied by moving the root node down if needed.
        """
        while new_root_index * 2 <= self.size:
            min_child_index = self.min_child(new_root_index)

            # Swap if child smaller.
            if self.heap_list[new_root_index] > self.heap_list[min_child_index]:
                self.heap_list[new_root_index], self.heap_list[min_child_index] = self.heap_list[min_child_index], self.heap_list[new_root_index]

            new_root_index = min_child_index

    def min_child(self, index: int) -> int:
        # If right node does not exist OR if left node is smaller than right node, return left node.
        if index * 2 + 1 > self.size or self.heap_list[index * 2] < self.heap_list[index * 2 + 1]:
            return index * 2
        # Else return right node
        else:
            return index * 2 + 1

    def insert(self, new_item: int):
        self.heap_list.append(new_item)
        self.size += 1

        self.perc_up(self.size)

    def del_min(self) -> int:
        return_value = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.size]

        self.heap_list.pop()
        self.size -= 1
        self.perc_down(1)

        return return_value


if __name__ == "__main__":
    values = [9, 6, 5, 2, 3]

    binary_heap = BinaryHeap(values)

    print(binary_heap.heap_list)
