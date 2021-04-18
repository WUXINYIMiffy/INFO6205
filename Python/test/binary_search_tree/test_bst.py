import unittest
from binary_search_tree.bst import BSTNode, search_key, insert_node, make_bst


class TestBST(unittest.TestCase):
    def test_insertion(self) -> None:
        keys = [8, 9, 5, 7, 4, 6]
        root = make_bst(keys=keys, values=keys)
        self.assertEqual(root.key, 8)
        self.assertEqual(root.lchild.key, 5)
        self.assertEqual(root.rchild.key, 9)
        self.assertEqual(root.lchild.lchild.key, 4)
        self.assertEqual(root.lchild.rchild.key, 7)
        self.assertEqual(root.lchild.rchild.lchild.key, 6)
