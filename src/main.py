"""Demostración de la implementación del B-Tree.

Ejecutar desde la raíz del repositorio:

    python -m src.main
"""

from src.btree import BTree


def main() -> None:
    tree = BTree(order=4)

    for key in (10, 20, 5, 6, 12, 30, 7, 17):
        tree.insert(key)

    print("Claves en orden:", tree.keys())
    print("Altura (aristas):", tree.height())
    print(f"Ocupación: {tree.occupancy():.3f}")
    print("Buscar 6:", tree.search(6))
    print("Buscar 99:", tree.search(99))
    print("Válido:", tree.validate())
    print("Estadísticas:", tree.stats())
    print("Representación:", tree.to_dict())


if __name__ == "__main__":
    main()
