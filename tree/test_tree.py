import unittest
from tree_node import TreeNode
from tree import Tree
from collections import deque
from typing import Callable


class TestTreeNode(unittest.TestCase):
    def test_is_leaf(self):
        leaf = TreeNode(value=1)
        self.assertTrue(leaf.is_leaf())

        non_leaf = TreeNode(value=2)
        non_leaf.add_child(TreeNode(value=3))
        self.assertFalse(non_leaf.is_leaf())

    def test_add_child(self):
        parent = TreeNode(value=1)
        child = TreeNode(value=2)
        parent.add_child(child)
        self.assertEqual(len(parent.children), 1)
        self.assertEqual(parent.children[0], child)

    def test_for_each_deep_first(self):
        node = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        child1.add_child(TreeNode(value=4))
        node.add_child(child1)
        node.add_child(child2)
        result = []
        visit = lambda x: result.append(x.value)
        node.for_each_deep_first(visit)
        self.assertEqual(result, [1, 2, 4, 3])

    def test_search(self):
        root = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        child1.add_child(TreeNode(value=4))
        root.add_child(child1)
        root.add_child(child2)
        tree = Tree(root)
        found = tree.root.search(4)
        self.assertIsNotNone(found)
        self.assertEqual(found.value, 4)
        not_found = tree.root.search(5)
        self.assertIsNone(not_found)

    def for_each_level_order(self, visit: Callable[[TreeNode], None]) -> None:
        q = deque([self])
        while q:
            current = q.popleft()
            visit(current)
            for child in current.children:
                q.append(child)


class TestTree(unittest.TestCase):
    def test_add(self):
        tree = Tree(TreeNode(value=1))
        child = TreeNode(value=2)
        tree.add(child)
        self.assertEqual(len(tree.root.children), 1)
        self.assertEqual(tree.root.children[0], child)

    def test_for_each_deep_first(self):
        root = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        child1.add_child(TreeNode(value=4))
        root.add_child(child1)
        root.add_child(child2)
        tree = Tree(root)
        result = []
        visit = lambda x: result.append(x.value)
        tree.for_each_deep_first(visit)
        self.assertEqual(result, [1, 2, 4, 3])

    def test_for_each_level_order(self):
        root = TreeNode(value=1)
        child1 = TreeNode(value=2)
        child2 = TreeNode(value=3)
        child1.add_child(TreeNode(value=4))
        root.add_child(child1)
        root.add_child(child2)
        tree = Tree(root)
        result = []
        visit = lambda x: result.append(x.value)
        tree.for_each_level_order(visit)
        self.assertEqual(result, [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main()
