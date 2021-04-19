import unittest
import typing as t
import random
from binary_search_tree.bst import BSTNode, make_simple_bst, find_min, delete_min, delete_key, insert_node, depth, \
    average_depth, converter
from binary_search_tree.visualizer import visualize_bt


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
        self.assertEqual(root.count, 6)

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
        self.assertEqual(root.count, 5)

    def test_delete_key(self) -> None:
        keys = [8, 9, 5, 7, 4, 6]
        root = make_simple_bst(keys=keys)
        root = delete_key(root, 5, algorithm='hibbard')
        expected_root = make_simple_bst([8, 6, 9, 4, 7])
        self.assertTrue(root.equals(expected_root))
        self.assertEqual(root.count, 5)

    def test_make_random_bst_instructions(self) -> None:
        instructions = make_random_bst_instructions(10, 5)
        self.assertEqual(len(instructions), 15)

    def test_algorithms_comparison(self) -> None:
        instructions = make_random_bst_instructions(1024, 512)
        root_1 = execute_instructions(instructions, 'hibbard')
        root_2 = execute_instructions(instructions, 'arbitrary-principle')
        print('hibbard', depth(root_1), average_depth(root_1))
        print('arbitrary-principle', depth(root_2), average_depth(root_2))
        self.assertTrue(depth(root_2) <= depth(root_1))
        self.assertTrue(average_depth(root_2) <= average_depth(root_1))

    def test_visualizer(self) -> None:
        instructions = make_random_bst_instructions(30, 10)
        root = execute_instructions(instructions, 'hibbard')
        visualize_bt(root, converter)


# HELPER FUNCTIONS
ADD = 'add'
DEL = 'del'


def make_random_bst_instructions(adds: int, dels: int) -> t.List[t.Tuple[str, int]]:
    '''
    Make a instructions list of "adds" insertion and "dels" deletion randomly
    return the list of operations, for example [('add', 3), ('add', 4), ('del', 3)]
    '''
    insertion_keys = list(range(adds))
    random.shuffle(insertion_keys)
    current_keys = []
    deletion_count = 0
    instructions = []

    while len(insertion_keys) or deletion_count < dels:
        # 0: insertion, 1: deletion
        action = [ADD, DEL][random.randint(1, adds + dels) > adds]
        if action == ADD:
            if not len(insertion_keys):
                continue
            key = insertion_keys.pop()
            instructions.append((ADD, key))
            current_keys.append(key)
        else:
            if len(current_keys) <= 1 or deletion_count == dels:
                continue
            key_index = random.choice(range(len(current_keys)))
            key = current_keys.pop(key_index)
            instructions.append((DEL, key))
            deletion_count += 1
    return instructions


def execute_instructions(instructions: t.List[t.Tuple[str, int]], algorithm: str) -> BSTNode:
    root = None
    for action, key in instructions:
        if action == ADD:
            root = insert_node(BSTNode(key=key, value=key), root)
        elif action == DEL:
            root = delete_key(root, key, algorithm)
        else:
            raise NotImplementedError()
    return root
