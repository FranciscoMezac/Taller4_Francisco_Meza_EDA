"""Nodo de un B-Tree.

Un nodo guarda claves ordenadas y, si no es hoja, hijos.
"""

from __future__ import annotations

from typing import Any

from .metrics import BTreeMetrics


class BTreeNode:
    """Nodo de un B-Tree de orden B.

    Invariantes:
    - Las claves están ordenadas de menor a mayor.
    - Un nodo hoja no tiene hijos.
    - Un nodo interno tiene exactamente ``len(keys) + 1`` hijos.
    """

    def __init__(self, leaf: bool = True) -> None:
        self.keys: list[Any] = []
        self.children: list[BTreeNode] = []
        self.leaf: bool = leaf

    def is_full(self, max_keys: int) -> bool:
        """Indica si el nodo alcanzó la capacidad máxima de claves."""
        return len(self.keys) >= max_keys

    def find_index(self, key: Any, metrics: BTreeMetrics | None = None) -> int:
        """Retorna la posición donde debería estar ``key``."""
        index = 0
        while index < len(self.keys):
            if metrics is not None:
                metrics.comparisons += 1
            if key <= self.keys[index]:
                break
            index += 1
        return index

    def __repr__(self) -> str:
        kind = "hoja" if self.leaf else "interno"
        return f"BTreeNode({kind}, keys={self.keys!r})"
