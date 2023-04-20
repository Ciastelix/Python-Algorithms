from typing import Any

class Node:
    value: Any
    next: "Node"
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)
