from __future__ import annotations

import typing as t
from dataclasses import dataclass

@dataclass
class EmptyNode:
    '''
    A class representing an empty BST node
    '''
    is_empty: bool = True


@dataclass
class BSTNode:
    '''
    A class representing a node in BST

    (key is unique in the tree)
    '''
    key: int
    value: int
    count: int = 1
    lchild: BSTNode = EmptyNode()
    rchild: BSTNode = EmptyNode()
    is_empty: bool = False

    def nullify(self) -> None:
        self.lchild = EmptyNode
        self.rchild = EmptyNode
        self.is_empty = True

def search_key(root: BSTNode, key: int) -> BSTNode:
    '''
    search the BST with given key
    return the found node
    '''
    return _search_key_with_parent(root, key, EMPTY_NODE)[0]


def _search_key_with_parent(root: BSTNode, key: int, parent: BSTNode) -> t.Tuple[
    BSTNode, BSTNode]:
    '''
    search the BST with given key
    return the found node, and its parent node
    '''
    if root.is_empty:
        return root, parent

    if key == root.key:
        return root, parent
    elif key < root.key:
        return _search_key_with_parent(root.lchild, key, root)
    else:
        return _search_key_with_parent(root.rchild, key, root)


def insert_node(node: BSTNode, root: t.BSTNode) -> BSTNode:
    '''
    insert a node to a BSTNode root
    '''
    maybe_found_node, found_node_parent = _search_key_with_parent(root=root, key=node.key, parent=EMPTY_NODE)
    if not maybe_found_node.is_empty:
        # reset value
        maybe_found_node.value = node.value
        return root

    if found_node_parent.is_empty:
        return node

    if node.key < found_node_parent.key:
        found_node_parent.lchild = node
    elif node.key > found_node_parent.key:
        found_node_parent.rchild = node
    else:
        raise Exception('cannot happen')
    return root


def make_bst(keys: t.List[int], values: t.List[int]) -> t.Optional[BSTNode]:
    assert len(keys) == len(values)
    root = EMPTY_NODE
    for k, v in zip(keys, values):
        root = insert_node(BSTNode(key=k, value=v), root)
    return root


def delete_key(root: t.Optional[BSTNode], key: int) -> t.Optional[BSTNode]:
    '''
    delete a node from the BST root
    returns the new root
    '''
    if root is None:
        return None

    maybe_found_node, found_node_parent = _search_key_with_parent(root, key, None)
    if maybe_found_node is None:
        return root

    if maybe_found_node.rchild is None:
        if found_node_parent is None:
            return maybe_found_node.lchild

        if found_node_parent.lchild == maybe_found_node:
            found_node_parent.lchild = maybe_found_node.lchild
        else:
            found_node_parent.rchild = maybe_found_node.lchild
        return root

    _, min_rnode = delete_min(maybe_found_node.rchild)
    maybe_found_node.value = min_rnode.value


def find_min(root: BSTNode) -> BSTNode:
    if root.lchild is None:
        return root
    return find_min(root.lchild)


def delete_min(root: BSTNode, parent: t.Optional[BSTNode]) -> t.Tuple[BSTNode, BSTNode]:
    '''
    delete the node with minimum key in BST root
    return the new root, and the node with minimum key
    '''
    min_node = find_min(root)
    _, min_node_parent = _search_key_with_parent(root, min_node.key, None)

