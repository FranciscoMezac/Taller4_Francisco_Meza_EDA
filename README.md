# Taller 4 — Auditoría de un B-Tree

**Asignatura:** Estructuras de Datos Avanzadas (IC10D – EDA)  
**Universidad Arturo Prat (UNAP)**  
**Semestre:** 2026-02  
**Docente:** Mauricio Andrés Oyarzún Silva (`moyarzunsil@unap.cl`)

---

## 🎯 Contexto

En este taller **el código ya está implementado**. No tienes que programar
el B-Tree: tienes que **auditarlo**.

El código compila y sus pruebas pasan. El foco no es buscar errores de
sintaxis ni reescribir la solución, sino identificar **decisiones de diseño
e implementación** que sean discutibles, explicar su impacto y proponer
alternativas con su costo.

Lee el enunciado completo en [`BRIEF.md`](./BRIEF.md).

---

## 📁 Estructura del repositorio

```text
├── README.md           <- Este documento
├── BRIEF.md            <- Enunciado del taller
├── AUDIT.md            <- [En Aula] Informe de auditoría
├── pyproject.toml      <- Versión de Python y configuración de pytest
├── design/             <- [En Aula] Diagramas de clases y de secuencia
├── src/
│   ├── main.py         <- Demostración ejecutable
│   └── btree/          <- Código a auditar
│       ├── node.py
│       ├── tree.py
│       └── metrics.py
└── tests/              <- Pruebas del código
```

---

## ▶️ Cómo ejecutar

Desde la raíz del repositorio:

```bash
python -m src.main
python -m pytest
```

Si no tienes `pytest`:

```bash
python -m pip install pytest
```

---

## 📦 Qué debes producir

1. **`AUDIT.md`** con la matriz de costos, la justificación por traza y los
   hallazgos de diseño.
2. **Diagramas** en `design/`: uno de clases y uno de secuencia, coherentes
   con el código real.
3. **Defensa oral** y una modificación en vivo solicitada por el docente.

---

## 🧭 Cómo trabajar

- **Antes de la sesión:** lee `src/btree/`, ejecuta el demo y las pruebas.
- **En la sesión:** diagrama, audita y defiende.
- El taller se desarrolla en **dos sesiones**. Tú administras cuánto tiempo
  dedicas a leer, diagramar, auditar y ensayar la defensa.

No hay un calendario rígido por bloque: la responsabilidad de distribuir el
tiempo es tuya.

---

## ⚖️ Reglas

- Trabajo **individual**.
- En la sesión presencial, **sin IA**.
- No reescribas el código durante la auditoría: documenta lo que encuentres.
  Si el docente pide una modificación en vivo, hazla en una copia o rama.
- Puedes usar los tests como evidencia, pero un test que pasa no reemplaza
  una auditoría.

---

<div class="page-break"></div>

## 📊 Evaluación

### Criterio de logro mínimo

Para aprobar **no necesitas encontrar todas las decisiones posibles**. El
piso del taller es:

- un diagrama de clases con las tres clases y sus relaciones;
- un diagrama de secuencia de `insert`;
- **tres hallazgos** con ubicación, explicación, impacto y propuesta;
- una defensa oral básica.

Los tres hallazgos pueden ser de diseño o de deuda de implementación; no es
obligatorio encontrar un error de correctitud. Mientras más hallazgos
sólidos, mejor la calificación, pero los tres mínimos son el piso.

| Criterio | Ponderación | Entregable auditado |
| :--- | :---: | :--- |
| **Fidelidad arquitectónica** | 25% | Correspondencia entre `src/` y los diagramas de `design/` |
| **Modelado dinámico** | 25% | Diagrama de secuencia con llamadas, decisiones y retornos |
| **Análisis de costos** | 25% | Matriz, justificación por traza y hallazgos en `AUDIT.md` |
| **Defensa oral y dominio** | 25% | Respuestas técnicas y modificación de código en vivo |

---

## 👤 Datos del estudiante

- **Nombre completo:** ______________________________________
- **RUT:** ___________________
- **Correo institucional:** __________________________________
- **Fecha del taller:** ___________________
