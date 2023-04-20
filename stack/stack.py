import sys
from typing import Any

sys.path.insert(1, "../linked_list")

from linkedlist import LinkedList


class Stack:
    _storage: LinkedList

    def __init__(self) -> None:
        self._storage = LinkedList()

    def push(self, element: Any) -> None:
        self._storage.append(element)

    def pop(self) -> Any:
        return self._storage.remove_last()

    def __str__(self) -> str:
        ret = self._storage.__str__().split(" -> ")
        ret = [str(i) for i in ret]
        return "\n".join(ret[::-1])

    def __len__(self) -> int:
        return len(self._storage)
