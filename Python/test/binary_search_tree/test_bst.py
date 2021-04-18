import unittest
from binary_search_tree.bst import BSTNode, make_simple_bst, find_min, delete_min, delete_key


class TestBST(unittest.TestCase):
    def test_insertion(self) -> None:
        keys = [8, 9, 5, 7, 4, 6]
        root = make_simple_bst(keys=keys)
        self.assertEqual(root.key, 8)
        self.assertEqual(root.lchild.key, 5)
        self.assertEqual(root.rchild.key, 9)
        self.assertEqual(root.lchild.lchild.key, 4)
        self.assertEqual(root.lchild.rchild.key, 7)
        self.assertEqual(root.lchild.rchild.lchild.key, 6)

    def test_find_min(self) -> None:
        keys = [8, 9, 5, 7, 4, 6]
        root = make_simple_bst(keys=keys)
        self.assertEqual(find_min(root).key, 4)

    def test_delete_min(self) -> None:
        keys = [8, 9, 5, 7, 4, 6]
        root = make_simple_bst(keys=keys)
        root = delete_min(root)
        self.assertEqual(root.key, 8)
        self.assertEqual(root.lchild.lchild, None)

    def test_delete_key(self) -> None:
        keys = [8, 9, 5, 7, 4, 6]
        root = make_simple_bst(keys=keys)
        root = delete_key(root, 5, algorithm='hibbard')
        expected_root = make_simple_bst([8, 6, 9, 4, 7])
        self.assertTrue(root.equals(expected_root))
