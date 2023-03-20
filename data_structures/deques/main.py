from typing import Any


class Deque():
    """
    Can add/remove from both front and rear.
    """

    items: list[Any]

    def __init__(self) -> None:
        self.items = []

    def addFront(self, item: Any):
        self.items.insert(0, item)

    def removeFront(self) -> Any:
        return self.items.pop(0)

    def addRear(self, item: Any):
        self.items.append(item)

    def removeRear(self) -> Any:
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    deque = Deque()

    print(f"Empty: {deque.is_empty()}")

    deque.addFront(1)
    deque.addFront(2)

    deque.addRear(10)
    deque.addRear(20)

    print(deque.items)

    deque.removeFront()
    deque.removeRear()

    print(deque.items)

    print(f"Empty: {deque.is_empty()}")
