from __future__ import annotations
from graphviz import Digraph
from dataclasses import dataclass
import typing as t


@dataclass
class BTNode:
    label: str
    rchild: t.Optional[t.Any] = None
    lchild: t.Optional[t.Any] = None


def visualize_bt(root: t.Any, converter: t.Callable[[t.Any], BTNode]) -> None:
    """
    Visualize the given Binary Tree
    params:
    - root: Any type representing a Binary Tree node
    - converter: A function to convert any node type to Node
    """
    g = Digraph('G', filename='bst_test.gv')

    todos = [converter(root)]
    while len(todos):
        node = todos.pop(0)
        # visit node
        if node.lchild is not None:
            lchild = converter(node.lchild)
            g.edge(node.label, lchild.label, 'L')
            todos.append(lchild)
        if node.rchild is not None:
            rchild = converter(node.rchild)
            g.edge(node.label, rchild.label, 'R')
            todos.append(rchild)
    g.view()
