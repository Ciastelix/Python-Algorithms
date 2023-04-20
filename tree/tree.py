from tree_node import TreeNode
from typing import Callable
import graphviz


class Tree:
    root: TreeNode

    def __init__(self, root: TreeNode):
        self.root = root

    def add(self, child: TreeNode) -> None:
        self.root.add_child(child)

    def for_each_deep_first(self, visit: Callable[[TreeNode], None]) -> None:
        self.root.for_each_deep_first(visit)

    def for_each_level_order(self, visit: Callable[[TreeNode], None]) -> None:
        self.root.for_each_level_order(visit)

    # show tree using graphviz
    def show(self) -> None:
        graph = graphviz.Digraph()
        self._add_node(graph, self.root)
        graph.render("tree.gv", view=True)

    def _add_node(self, graph: graphviz.Digraph, node: TreeNode) -> None:
        graph.node(str(node))
        for child in node.children:
            graph.edge(str(node), str(child))
            self._add_node(graph, child)


if __name__ == "__main__":
    tree = Tree(TreeNode("F"))
    tree.root.add_child(TreeNode("B"))
    tree.root.add_child(TreeNode("G"))
    tree.root.search("B").add_child(TreeNode("A"))
    tree.root.search("B").add_child(TreeNode("D"))
    tree.root.search("D").add_child(TreeNode("C"))
    tree.root.search("D").add_child(TreeNode("E"))
    tree.root.search("G").add_child(TreeNode("I"))
    tree.root.search("I").add_child(TreeNode("H"))
    tree.for_each_level_order(print)
