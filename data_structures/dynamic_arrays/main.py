from ctypes import py_object, Array
from typing import Any


class DynamicArray():
    capacity: int
    element_count: int

    def __init__(self) -> None:
        self.capacity = 1
        self.element_count = 0
        self.array = self._make_array(self.capacity)

    def __len__(self) -> int:
        return self.element_count

    def __getitem__(self, i: int) -> Any:
        if i < 0 or i >= self.element_count:
            return IndexError(f"Index {i} is out of bounds. Length of array: {len(self)}")

        return self.array[i]

    def _resize(self, new_capacity: int):
        new_array = self._make_array(new_capacity)

        for i in range(self.element_count):
            new_array[i] = self.array[i]

        self.array = new_array
        self.capacity = new_capacity

    def _make_array(self, capacity: int):
        return (capacity * py_object)()

    def append(self, item: Any) -> None:
        if self.element_count == self.capacity:
            self._resize(self.capacity * 2)

        self.array[self.element_count] = item
        self.element_count += 1


if __name__ == "__main__":
    array = DynamicArray()

    array.append(2)

    print(array[0])

    array.append(3)
    array.append(4)
    array.append(5)

    print(array[3])
