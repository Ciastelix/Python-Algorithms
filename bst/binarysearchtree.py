from binarynode import BinaryNode
from typing import Any
import graphviz


class BinarySearchTree:
    def __init__(self):
        self.root

    def insert(self, value: Any) -> None:
        if self.root is None:
            self.root = BinaryNode(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value: Any, node: BinaryNode) -> BinaryNode:
        if value < node.value:
            if node.left_child is None:
                node.left_child = BinaryNode(value)
            else:
                self._insert(value, node.left_child)
        else:
            if node.right_child is None:
                node.right_child = BinaryNode(value)
            else:
                self._insert(value, node.right_child)

    def insert_list(self, values: list) -> None:
        for value in values:
            self.insert(value)

    def remove(self, value: Any) -> None:
        if self.root is not None:
            self.root = self._remove(value, self.root)

    def _remove(self, value: Any, node: BinaryNode) -> BinaryNode:
        if node is None:
            return node
        elif value < node.value:
            node.left_child = self._remove(value, node.left_child)
        elif value > node.value:
            node.right_child = self._remove(value, node.right_child)
        else:
            node = self._remove_node(node)

    def _remove_node(self, node: BinaryNode) -> BinaryNode:
        if node.left_child is None and node.right_child is None:
            return None
        elif node.left_child is None:
            return node.right_child
        elif node.right_child is None:
            return node.left_child
        else:
            temp_node = self._get_predecessor(node.left_child)
            node.value = temp_node.value
            node.left_child = self._remove_node(temp_node)
            return node

    def _get_predecessor(self, node: BinaryNode) -> BinaryNode:
        if node.right_child:
            return self._get_predecessor(node.right_child)
        return node

    def contains(self, value: Any) -> bool:
        if self.root is not None:
            return self._contains(value, self.root)
        return False

    def _contains(self, value: Any, node: BinaryNode) -> bool:
        if node is None:
            return False
        elif value < node.value:
            return self._contains(value, node.left_child)
        elif value > node.value:
            return self._contains(value, node.right_child)
        else:
            return True

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
