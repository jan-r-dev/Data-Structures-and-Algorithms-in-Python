from typing import Any


class Queue():
    """
    FIFO principle
    """

    items: list[Any]

    def __init__(self) -> None:
        self.items = []

    def enqueue(self, item: Any):
        self.items.insert(0, item)

    def dequeue(self) -> Any:
        return self.items.pop(0)

    def is_empty(self) -> bool:
        return len(self.items) == 0

    def size(self) -> int:
        return len(self.items)


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    print(queue.items)

    print(f"Length is: {queue.size()}")

    queue.dequeue()
    queue.dequeue()
    print(queue.items)

    print(f"Empty: {queue.is_empty()}")
