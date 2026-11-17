"""Smoke test de la plantilla.

No prueba una estructura concreta: solo verifica que el paquete fuente
se importa correctamente y que el entorno de pruebas está operativo.
Las pruebas de comportamiento de cada taller se agregan en esta carpeta.
"""

import src.main


def test_import_paquete():
    assert src.main is not None
