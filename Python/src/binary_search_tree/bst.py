from __future__ import annotations

from dataclasses import dataclass
import typing as t

@dataclass
class BSTNode:
    key: int
    count: int = 1
    lchild: t.Optional[BSTNode] = None
    rchild: t.Optional[BSTNode] = None
    parent: t.Optional[BSTNode] = None
