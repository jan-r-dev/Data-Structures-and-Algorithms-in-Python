from typing import Any


class Stack():
    """
    LIFO principle
    """

    items: list[Any]

    def __init__(self) -> None:
        self.items = []

    def push(self, item: Any):
        self.items.append(item)

    def pop(self) -> Any:
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def peek(self) -> Any:
        return self.items[len(self.items) - 1]

    def size(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()

    print(f"Empty: {stack.is_empty()}")

    stack.push(1)
    stack.push(2)

    print(f"Length is: {stack.size()}")
    print(stack.peek())

    removed = stack.pop()

    print(stack.peek())
    print(removed)
    print(stack.is_empty())

    print(f"Empty: {stack.is_empty()}")
