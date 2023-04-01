from __future__ import annotations


class BSTNode:
    """
    Implemented according to: https://blog.boot.dev/computer-science/binary-search-tree-in-python/
    """

    def __init__(self, value: int | None = None):
        self.left: BSTNode | None = None
        self.right: BSTNode | None = None
        self.value = value

    def insert(self, new_value: int) -> None:

        # Root is empty? Assign and return.
        if self.value is None:
            self.value = new_value
            return

        # Same as the root? No action needed.
        if self.value == new_value:
            return

        # Smaller than the root value? Go left.
        if new_value < self.value:
            if self.left:
                self.left.insert(new_value)
                return
            # Create left if it doesn't exist.
            self.left = BSTNode(new_value)
            return

        # Still running? Must be greater than the root value. Go right.
        if new_value > self.value:
            if self.right:
                self.right.insert(new_value)
                return
             # Create right if it doesn't exist.
            self.right = BSTNode(new_value)
            return

    def get_min(self) -> int | None:
        current = self
        while current.left is not None:
            current = current.left

        return current.value if current.value is not None else None

    def get_max(self) -> int | None:
        current = self
        while current.right is not None:
            current = current.right

        return current.value if current.value is not None else None

    def delete(self, value):
        if self == None:
            return self

        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
            return self

        if value > self.value:
            if self.right:
                self.right = self.right.delete(value)
            return self

        if self.right == None:
            return self.left

        if self.left == None:
            return self.right

        # Node that has the next-largest key in the tree will become the successor of the deleted node.
        successor = self.right
        while successor.left:
            successor = successor.left

        self.value = successor.value
        self.right = self.right.delete(successor.value)
        return self

    def exists(self, value):
        if value == self.value:
            return True

        if value < self.value:
            if self.left == None:
                return False
            return self.left.exists(value)

        if self.right == None:
            return False
        return self.right.exists(value)

    def preorder(self, values: list[int]):
        if self.value is not None:
            values.append(self.value)
        if self.left is not None:
            self.left.preorder(values)
        if self.right is not None:
            self.right.preorder(values)
        return values

    def inorder(self, values: list[int]):
        if self.left is not None:
            self.left.inorder(values)
        if self.value is not None:
            values.append(self.value)
        if self.right is not None:
            self.right.inorder(values)
        return values

    def postorder(self, values: list[int]):
        if self.left is not None:
            self.left.postorder(values)
        if self.right is not None:
            self.right.postorder(values)
        if self.value is not None:
            values.append(self.value)
        return values


if __name__ == "__main__":
    nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]

    bst = BSTNode()
    for num in nums:
        bst.insert(num)

    print("preorder:")
    print(bst.preorder([]))
    print("#")

    print("postorder:")
    print(bst.postorder([]))
    print("#")

    print("inorder:")
    print(bst.inorder([]))
    print("#")

    nums = [2, 6, 20]
    print("deleting " + str(nums))
    for num in nums:
        bst.delete(num)
    print("#")

    print("4 exists:")
    print(bst.exists(4))
    print("2 exists:")
    print(bst.exists(2))
    print("12 exists:")
    print(bst.exists(12))
    print("18 exists:")
    print(bst.exists(18))
