from .bst import BSTNode
import typing as t


def hibbard_deletion(node: BSTNode, key: int):
    # root = hibbard_deletion( root , key)
    pass


def node_delete(node: t.Optional[BSTNode], key: int):
    '''
    Delete the node with the key in subtree
    '''
    if node is None:
        return None
    if key < node.key:
        node_delete(node.lchild, key)
    elif key > node.key:
        node_delete(node.rchild, key)
    else:
        rhand_delete_node(node)


def rhand_delete_node(node: BSTNode) -> None:
    '''
    Delete the given node in right-handed style
    '''
    if node.rchild is None:
        if node.parent is not None:
            if node.parent.lchild == node:
                node.parent.lchild = node.lchild
            else:
                node.parent.rchild = node.lchild
        if node.lchild is not None:
            node.lchild.parent = node.parent
        return


def lhand_delete_node(node: BSTNode) -> None:
    pass
    '''
    Delete the given node in left-handed style
    '''
    # if node.lchild is None:
    #     if node.parent is not None:
    #         if node.parent.rchild == node:
    #             node.parent.rchild = node.rchild
    #         else:
    #             node.parent.lchild = node.rchild
    #     if node.rchild is not None:
    #         node.rchild.parent = node.parent
    #     return


def find_min(node: BSTNode) -> BSTNode:
    '''
    return the node with minimal key in the subtree
    '''
    if node.lchild is None:
        return node

    raise NotImplementedError()


def insert(self, node: BSTNode):
    if self.node:
        if node < self.node:
            if self.left is None:
                self.left = BSTNode(node)
            else:
                self.left.insert(node)
        elif node > self.node:
            if self.right is None:
                self.right = BSTNode(node)
            else:
                self.right.insert(node)
    else:
        self.node =
