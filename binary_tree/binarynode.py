from __future__ import annotations
from typing import Any, Callable
from dataclasses import dataclass


@dataclass
class BinaryNode:
    value: Any
    left_child: BinaryNode = None
    right_child: BinaryNode = None

    def is_leaf(self) -> bool:
        return bool(self.left_child) and bool(self.right_child)

    def add_left_child(self, value: Any) -> None:
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any) -> None:
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self.value)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        visit(self.value)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self.value)

    def __str__(self) -> str:
        return str(self.value)
