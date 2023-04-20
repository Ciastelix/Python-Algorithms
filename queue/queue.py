import sys
from typing import Any

sys.path.insert(1, "../linked_list")
from linkedlist import LinkedList


class Queue:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def peek(self) -> Any:
        return self._storage.node(0).value

    def enqueue(self, element: Any) -> None:
        self._storage.append(element)

    def dequeue(self) -> Any:
        return self._storage.pop()

    def __str__(self) -> str:
        return self._storage.__str__().replace(" -> ", ", ")

    def __len__(self) -> int:
        return len(self._storage)


