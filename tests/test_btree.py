"""Pruebas de correctitud del B-Tree del Taller 4.

Estas pruebas verifican que el código funciona bajo sus propias
convenciones. No evalúan las decisiones de diseño que se auditan en clase.
"""

import random

import pytest

from src.btree import BTree


def test_orden_debe_ser_par_y_mayor_igual_a_cuatro():
    with pytest.raises(ValueError):
        BTree(order=3)
    with pytest.raises(ValueError):
        BTree(order=5)

    tree = BTree(order=4)
    assert tree.order == 4
    assert tree.max_keys == 3
    assert tree.min_keys == 1


def test_insercion_y_busqueda_secuencial():
    for order in (4, 6):
        tree = BTree(order=order)
        for key in range(200):
            tree.insert(key)

        assert tree.validate()
        assert len(tree) == 200
        assert all(tree.search(key) for key in range(200))
        assert not tree.search(200)
        assert tree.height() >= 1


def test_split_de_la_raiz():
    tree = BTree(order=4)

    for key in range(20):
        tree.insert(key)

    assert tree.validate()
    assert not tree.root.leaf
    assert len(tree.root.keys) >= 1
    assert len(tree.root.children) == len(tree.root.keys) + 1
    assert tree.keys() == list(range(20))


def test_insercion_aleatoria_y_validacion():
    rng = random.Random(2026)
    keys = list(range(500))
    rng.shuffle(keys)

    tree = BTree(order=4)
    for key in keys:
        tree.insert(key)
        assert tree.validate()

    assert len(tree) == len(keys)
    assert all(tree.search(key) for key in keys)
    assert not tree.search(-1)
    assert not tree.search(500)


def test_claves_duplicadas_y_borrado_total():
    tree = BTree(order=4)

    for _ in range(3):
        tree.insert(5)

    assert tree.validate()
    assert len(tree) == 3
    assert tree.search(5)
    assert tree.keys() == [5, 5, 5]

    assert tree.delete(5) is True
    assert tree.validate()
    assert len(tree) == 0
    assert not tree.search(5)
    assert tree.keys() == []


def test_borrado_reconstruye_y_conserva_el_resto():
    tree = BTree(order=4)

    for key in range(100):
        tree.insert(key)

    assert tree.delete(50) is True
    assert tree.validate()
    assert not tree.search(50)
    assert len(tree) == 99
    assert all(tree.search(key) for key in range(100) if key != 50)
    assert tree.metrics.rebuilds == 1

    assert tree.delete(50) is False
    assert tree.metrics.rebuilds == 1


def test_altura_y_ocupacion():
    empty = BTree(order=4)
    assert empty.height() == 0
    assert empty.occupancy() == 0.0
    assert empty.validate()

    tree = BTree(order=4)
    for key in range(1000):
        tree.insert(key)

    assert tree.height() >= 1
    assert 0.0 < tree.occupancy() <= 1.0
    assert tree.validate()


def test_estadisticas_basicas():
    tree = BTree(order=4)
    for key in (10, 20, 30, 40, 50):
        tree.insert(key)

    stats = tree.stats()
    assert stats["order"] == 4
    assert stats["keys"] == 5
    assert stats["splits"] >= 1
    assert stats["node_reads"] >= 0
    assert stats["rebuilds"] == 0


def test_to_dict_respeta_la_estructura():
    tree = BTree(order=4)
    for key in range(10):
        tree.insert(key)

    data = tree.to_dict()
    assert data["leaf"] is False
    assert len(data["children"]) == len(data["keys"]) + 1
    assert tree.validate()
