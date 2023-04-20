from __future__ import annotations
from typing import Any, List, Callable, Union


class TreeNode:
    value: Any
    children: List[TreeNode]

    def __init__(self, value: Any) -> None:
        self.value = value
        self.children = []

    def is_leaf(self) -> bool:
        return len(self.children) == 0

    def add_child(self, child: TreeNode) -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[[TreeNode], None]) -> None:
        visit(self)
        for child in self.children:
            child.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[[TreeNode], None]) -> None:
        def visit_level(level_nodes):
            if not level_nodes:
                return

            next_level_nodes = []
            for node in level_nodes:
                visit(node)
                next_level_nodes.extend(node.children)

            visit_level(next_level_nodes)

        visit_level([self])

    def search(self, value: Any) -> Union[TreeNode, None]:
        if self.value == value:
            return self
        for child in self.children:
            result = child.search(value)
            if result is not None:
                return result
        return None

    def __str__(self) -> str:
        return str(self.value)
