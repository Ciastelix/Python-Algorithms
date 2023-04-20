from typing import Any
from node import Node
from dataclasses import dataclass


@dataclass
class LinkedList:
    head: Node = None

    def push(self, value: Any) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node

    def append(self, value: Any) -> None:
        node = Node(value)
        if not self.head:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def node(self, at: int) -> Node:
        current = self.head
        if at >= len(self):
            raise IndexError("Index out of range")
        for _ in range(at):
            current = current.next
        return current

    def insert(self, value: Any, at: int) -> None:
        self.node(at - 1).next = Node(value, self.node(at))

    def pop(self) -> Any:
        temp = self.head
        self.head = self.head.next
        return temp.value

    def remove_last(self) -> Any:
        current = self.head
        while current.next.next:
            current = current.next
        temp = current.next
        current.next = None
        return temp.value

    def remove(self, after: Node) -> Any:
        current = self.head
        temp = None
        while current:
            if current.value == after.value:
                temp = current.next
                current.next = current.next.next
            current = current.next
        if temp:
            return temp.value
        return None

    def __len__(self) -> int:
        current = self.head
        length = 0
        while current:
            length += 1
            current = current.next
        return length

    def __str__(self) -> str:
        nodes = list()
        current = self.head
        while current:
            nodes.append(str(current.value))
            current = current.next
        return " -> ".join(nodes)
