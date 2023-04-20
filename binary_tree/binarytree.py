from __future__ import annotations
from typing import Any, Callable
from binarynode import BinaryNode
import graphviz


class BinaryTree:
    root: BinaryNode

    def __init__(self, value: Any) -> None:
        self.root = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_in_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_pre_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]) -> None:
        self.root.traverse_post_order(visit)

    def show(self) -> None:
        graph = graphviz.Digraph()
        self._add_node(graph, self.root)
        graph.render("tree.gv", view=True)

    def _add_node(self, graph: graphviz.Digraph, node: BinaryNode) -> None:
        if node is not None:
            graph.node(str(node.value))
            if node.left_child is not None:
                self._add_node(graph, node.left_child)
                graph.edge(str(node.value), str(node.left_child.value))
            if node.right_child is not None:
                self._add_node(graph, node.right_child)
                graph.edge(str(node.value), str(node.right_child.value))
