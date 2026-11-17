"""B-Tree estándar.

Convenciones:
- ``order`` es el número máximo de hijos por nodo interno.
- ``order`` debe ser par y >= 4.
- ``height`` se cuenta en aristas: un árbol de un solo nodo tiene altura 0.
"""

from __future__ import annotations

from typing import Any, Iterator

from .metrics import BTreeMetrics
from .node import BTreeNode


class BTree:
    """B-Tree de orden par ``order``."""

    def __init__(self, order: int = 4, metrics: BTreeMetrics | None = None) -> None:
        if order < 4 or order % 2 != 0:
            raise ValueError("order debe ser par y >= 4")
        self.order = order
        self.degree = order // 2
        self.max_keys = order - 1
        self.min_keys = self.degree - 1
        self.root = BTreeNode(leaf=True)
        self.metrics = metrics if metrics is not None else BTreeMetrics()

    # ---------------------------------------------------------------- búsqueda

    def search(self, key: Any) -> bool:
        """Retorna True si ``key`` está en el árbol."""
        return self._search_node(self.root, key) is not None

    def _search_node(self, node: BTreeNode, key: Any) -> tuple[BTreeNode, int] | None:
        self.metrics.node_reads += 1
        index = node.find_index(key, self.metrics)

        if index < len(node.keys) and node.keys[index] == key:
            return (node, index)
        if node.leaf:
            return None
        return self._search_node(node.children[index], key)

    # --------------------------------------------------------------- inserción

    def insert(self, key: Any) -> None:
        """Inserta ``key``. Se permiten claves duplicadas."""
        if self.root.is_full(self.max_keys):
            new_root = BTreeNode(leaf=False)
            new_root.children.append(self.root)
            self._split_child(new_root, 0)
            self.root = new_root

        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node: BTreeNode, key: Any) -> None:
        index = node.find_index(key, self.metrics)

        if node.leaf:
            node.keys.insert(index, key)
            self.metrics.key_inserts += 1
            return

        if node.children[index].is_full(self.max_keys):
            self._split_child(node, index)
            if key > node.keys[index]:
                index += 1

        self._insert_non_full(node.children[index], key)

    def _split_child(self, parent: BTreeNode, index: int) -> None:
        """Parte el hijo lleno ``parent.children[index]``.

        La mediana sube al padre. El hijo izquierdo conserva la mitad
        izquierda y el nuevo hermano recibe la mitad derecha.
        """
        child = parent.children[index]
        median_index = self.degree - 1
        median = child.keys[median_index]

        right = BTreeNode(leaf=child.leaf)
        right.keys = child.keys[median_index + 1 :]
        child.keys = child.keys[:median_index]

        if not child.leaf:
            right.children = child.children[median_index + 1 :]
            child.children = child.children[: median_index + 1]

        parent.keys.insert(index, median)
        parent.children.insert(index + 1, right)
        self.metrics.splits += 1

    # ----------------------------------------------------------------- borrado

    def delete(self, key: Any) -> bool:
        """Elimina las apariciones de ``key``.

        Retorna True si la clave existía y False en caso contrario.
        """
        if not self.search(key):
            return False

        remaining = [current for current in self.keys() if current != key]
        self._rebuild(remaining)
        return True

    def _rebuild(self, keys: list[Any]) -> None:
        self.root = BTreeNode(leaf=True)
        self.metrics.rebuilds += 1
        for key in keys:
            self.insert(key)

    # ------------------------------------------------------------- utilidades

    def keys(self) -> list[Any]:
        """Retorna todas las claves en orden, materializadas en una lista."""
        result: list[Any] = []
        self._collect_keys(self.root, result)
        return result

    def _collect_keys(self, node: BTreeNode, result: list[Any]) -> None:
        for index, key in enumerate(node.keys):
            if not node.leaf:
                self._collect_keys(node.children[index], result)
            result.append(key)
        if not node.leaf:
            self._collect_keys(node.children[-1], result)

    def height(self) -> int:
        """Altura en aristas, siguiendo el camino más a la izquierda."""
        height = 0
        node = self.root
        while not node.leaf:
            height += 1
            node = node.children[0]
        return height

    def occupancy(self) -> float:
        """Fracción de ranuras ocupadas sobre el total de nodos."""
        nodes = list(self._iter_nodes())
        if not nodes:
            return 0.0
        slots = len(nodes) * self.max_keys
        used = sum(len(node.keys) for node in nodes)
        return used / slots if slots else 0.0

    def stats(self) -> dict[str, int | float]:
        """Resumen de estructura y métricas acumuladas."""
        nodes = list(self._iter_nodes())
        return {
            "order": self.order,
            "height_edges": self.height(),
            "nodes": len(nodes),
            "keys": sum(len(node.keys) for node in nodes),
            "occupancy": self.occupancy(),
            "comparisons": self.metrics.comparisons,
            "node_reads": self.metrics.node_reads,
            "splits": self.metrics.splits,
            "rebuilds": self.metrics.rebuilds,
        }

    def _iter_nodes(self) -> Iterator[BTreeNode]:
        stack = [self.root]
        while stack:
            node = stack.pop()
            yield node
            stack.extend(node.children)

    def to_dict(self) -> dict[str, Any]:
        """Representación recursiva útil para depuración y diagramas."""

        def convert(node: BTreeNode) -> dict[str, Any]:
            return {
                "keys": list(node.keys),
                "leaf": node.leaf,
                "children": [convert(child) for child in node.children],
            }

        return convert(self.root)

    # ------------------------------------------------------------- validación

    def validate(self) -> bool:
        """Verifica los invariantes estructurales del B-Tree."""
        if not self.root.keys:
            return self.root.leaf and not self.root.children

        leaf_depths: set[int] = set()

        def visit(node: BTreeNode, depth: int, is_root: bool) -> bool:
            if len(node.keys) > self.max_keys:
                return False
            if not is_root and len(node.keys) < self.min_keys:
                return False
            if any(node.keys[i] > node.keys[i + 1] for i in range(len(node.keys) - 1)):
                return False

            if node.leaf:
                if node.children:
                    return False
                leaf_depths.add(depth)
                return True

            if len(node.children) != len(node.keys) + 1:
                return False
            return all(visit(child, depth + 1, False) for child in node.children)

        if not visit(self.root, 0, True):
            return False
        if len(leaf_depths) != 1:
            return False

        ordered = self.keys()
        return all(ordered[i] <= ordered[i + 1] for i in range(len(ordered) - 1))

    def __len__(self) -> int:
        return sum(len(node.keys) for node in self._iter_nodes())
