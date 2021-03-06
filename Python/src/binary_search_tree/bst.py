from __future__ import annotations

import typing as t
from random import randint
from dataclasses import dataclass
from binary_search_tree.visualizer import BTNode


@dataclass
class BSTNode:
    '''
    A class representing a node in BST

    (key is unique in the tree)
    '''
    key: int
    value: int
    count: int = 1
    lchild: BSTNode = None
    rchild: BSTNode = None

    def equals(self, other_node: OptionalBSTNode) -> bool:
        if self.key != other_node.key:
            return False
        if self.value != other_node.value:
            return False
        if self.count != other_node.count:
            return False
        if self.lchild is not None:
            if not self.lchild.equals(other_node.lchild):
                return False
        elif other_node.lchild is not None:
            return False
        if self.rchild is not None:
            if not self.rchild.equals(other_node.rchild):
                return False
        elif other_node.rchild is not None:
            return False

        return True

    def update_count(self) -> None:
        self.count = count(self.lchild) + count(self.rchild) + 1


def converter(bst_node: BSTNode) -> BTNode:
    return BTNode(label=str(bst_node.key), lchild=bst_node.lchild, rchild=bst_node.rchild)


OptionalBSTNode = t.Optional[BSTNode]


def depth(root: OptionalBSTNode) -> int:
    if root is None:
        return 0
    return max(depth(root.lchild), depth(root.rchild)) + 1


def average_depth(root: OptionalBSTNode) -> int:
    if root is None:
        return 0

    sum_depth = 0
    todos = [(root, 1)]
    while todos:
        node, height = todos.pop(0)
        sum_depth += height
        if node.lchild is not None:
            todos.append((node.lchild, height + 1))
        if node.rchild is not None:
            todos.append((node.rchild, height + 1))
    return sum_depth / root.count


def count(root: OptionalBSTNode) -> int:
    if root is None:
        return 0
    else:
        return root.count


def search_key(root: OptionalBSTNode, key: int) -> OptionalBSTNode:
    '''
    search the BST with given key
    return the found node
    '''
    if root is None:
        return None

    if key == root.key:
        return root
    elif key < root.key:
        return search_key(root.lchild, key)
    else:
        return search_key(root.rchild, key)


def insert_node(node: BSTNode, root: OptionalBSTNode) -> BSTNode:
    '''
    insert a node to a BSTNode root
    '''
    if root is None:
        return node

    if node.key == root.key:
        root.value = node.value
    elif node.key < root.key:
        root.lchild = insert_node(node, root.lchild)
        root.update_count()
    else:
        root.rchild = insert_node(node, root.rchild)
        root.update_count()
    return root


def make_simple_bst(keys: t.List[int]) -> OptionalBSTNode:
    return make_bst(keys=keys, values=keys)


def make_bst(keys: t.List[int], values: t.List[int]) -> OptionalBSTNode:
    assert len(keys) == len(values)
    root = None
    for k, v in zip(keys, values):
        root = insert_node(BSTNode(key=k, value=v), root)
    return root


def delete_key(root: OptionalBSTNode, key: int, algorithm: str) -> OptionalBSTNode:
    '''
    delete a node from the BST root
    returns the new root
    '''
    if root is None:
        return None

    if key < root.key:
        root.lchild = delete_key(root.lchild, key, algorithm)
        root.update_count()
        return root
    if key > root.key:
        root.rchild = delete_key(root.rchild, key, algorithm)
        root.update_count()
        return root

    if algorithm.lower() == 'hibbard':
        if root.rchild is None:
            return root.lchild
        min_node = find_min(root.rchild)
        root.key = min_node.key
        root.value = min_node.value
        root.rchild = delete_min(root.rchild)
        root.update_count()
    elif algorithm.lower() == 'arbitrary-principle':
        # 0: left hand style; 1: right hand style
        if randint(0, 1) == 0:
            if root.lchild is None:
                return root.rchild
            max_node = find_max(root.lchild)
            root.key = max_node.key
            root.value = max_node.value
            root.lchild = delete_max(root.lchild)
            root.update_count()
        else:
            if root.rchild is None:
                return root.lchild
            min_node = find_min(root.rchild)
            root.key = min_node.key
            root.value = min_node.value
            root.rchild = delete_min(root.rchild)
            root.update_count()
    else:
        raise NotImplementedError('unsupported algorithm')
    return root


def find_min(root: BSTNode) -> BSTNode:
    '''
    return the node with the minimum key
    '''
    if root.lchild is None:
        return root
    return find_min(root.lchild)


def find_max(root: BSTNode) -> BSTNode:
    '''
    return the node with the maximum key
    '''
    if root.rchild is None:
        return root
    return find_max(root.rchild)


def delete_min(root: BSTNode) -> OptionalBSTNode:
    '''
    delete the node with minimum key in BST root
    return the new root
    '''
    if root.lchild is None:
        return root.rchild

    root.lchild = delete_min(root.lchild)
    root.update_count()
    return root


def delete_max(root: BSTNode) -> OptionalBSTNode:
    '''
    delete the node with maximum key in BST root
    return the new root
    '''
    if root.rchild is None:
        return root.lchild

    root.rchild = delete_max(root.rchild)
    root.update_count()
    return root
