"""Métricas de operación del B-Tree.

Cuentan operaciones en RAM.
"""

from dataclasses import dataclass


@dataclass
class BTreeMetrics:
    """Contadores acumulados de la última vida del árbol."""

    comparisons: int = 0
    node_reads: int = 0
    key_inserts: int = 0
    splits: int = 0
    rebuilds: int = 0

    def reset(self) -> None:
        """Reinicia todos los contadores."""
        self.comparisons = 0
        self.node_reads = 0
        self.key_inserts = 0
        self.splits = 0
        self.rebuilds = 0
