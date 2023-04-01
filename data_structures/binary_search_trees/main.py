from __future__ import annotations


class BSTNode:

    def __init__(self, value: int | None = None):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, new_value: int):

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

        


if __name__ == "__main__":
    pass
