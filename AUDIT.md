# Informe de Auditoría — B-Tree

**Asignatura:** Estructuras de Datos Avanzadas (IC10D – EDA)  
**Estudiante:** [Francisco Meza Copaira]  
**RUT:** [20885256-6]  
**Fecha:** [19-11-2026]  
**Taller:** 4 — Auditoría de un B-Tree

---

## 1. Matriz de costos

Completa la matriz con el modelo de costo que corresponda. Si una operación
no aplica a un modelo, escribe `N/A` y justifica.

| Operación | Costo RAM (peor) | Costo RAM (amortizado) | Costo E/S | Condición (N, B, M) | Evidencia |
| :--- | :---: | :---: | :---: | :--- | :--- |
| `search(key)` | `O(...)` | `O(...)` | `O(...)` | | |
| `insert(key)` | `O(...)` | `O(...)` | `O(...)` | | |
| `delete(key)` | `O(...)` | `O(...)` | `O(...)` | | |
| `height()` | `O(...)` | `O(...)` | `O(...)` | | |
| `occupancy()` | `O(...)` | `O(...)` | `O(...)` | | |
| `validate()` | `O(...)` | `O(...)` | `O(...)` | | |

> **No se pide una demostración formal.** No uses funciones potenciales ni
> recurrencias. Usa trazas, conteos y condiciones explícitas.

---

## 2. Justificación por traza

Elige al menos **dos operaciones** y síguelas con un ejemplo pequeño.
Indica el estado antes, los pasos y el estado después.

### Operación 1: `[nombre]`

- **Entrada / estado inicial:**
- **Traza paso a paso:**
- **Conteo relevante** (comparaciones, nodos visitados, splits, etc.):
- **Conclusión de costo:**

### Operación 2: `[nombre]`

- **Entrada / estado inicial:**
- **Traza paso a paso:**
- **Conteo relevante:**
- **Conclusión de costo:**

---

## 3. Hallazgos de diseño e implementación

Registra los hallazgos que puedas sostener con evidencia. El **mínimo es
tres**; si encuentras más, agrega filas. No confundas un **error de
correctitud** con una **decisión controvertida**: si el código funciona,
pero la decisión es discutible, clasifícala como diseño.

| ID | Ubicación | Decisión observada | Por qué es discutible | Impacto | Propuesta | Prioridad |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| H-01 | `src/tree-97` |Se elimina un nodo pero no se verifica si es un nodo hoja, o si tiene hermanos y al final para reordenar, se hace un rebuild a todo el arbol sin el nodo que se esta eliminando| Es discutible ya que primero no verifica si es un hoja o un hermano, si es un nodo hoja simplemente es eliminar este nodo y el costo computacional seria minimo, si es un hermano se tiene que reordenar el arbol y aun asi el costo computacional seria mucho mas bajo que rehacer el arbol completo| Es mucho mas costoso computacionalmente | Verificar que nodo estamos eliminando, si es un hoja, si tiene hijos, si tiene hermano, una vez que se haya eliminado la clave, reordenar el arbol, no rehacerlo. | ALTA |
| H-02 | `src/...:línea` | | | | | |
| H-03 | `src/...:línea` | | | | | |

> Si encuentras más de tres, duplica una fila. No se penaliza no llegar a
> las decisiones más finas; se evalúa la calidad de las que sí sostienes.

### 3.1 Clasificación

Para cada hallazgo, indica si es:

- **Decisión de diseño:** el código es correcto, pero hay una alternativa
  con mejor costo, claridad o fidelidad al modelo.
- **Deuda de implementación:** el código funciona, pero la forma de
  implementarlo introduce un costo oculto.
- **Error de correctitud:** el código no cumple su contrato. En ese caso,
  adjunta una traza o un test que lo demuestre.

---

## 4. Evidencia de ejecución

Puedes usar los tests, el demo o trazas propias. No pegues salidas
completas: cita lo relevante.

```text
Comando:
Resultado:
Interpretación:
```

---

## 5. Registro de la defensa oral

| Momento | Pregunta o solicitud del docente | Respuesta / modificación | Resultado |
| :--- | :--- | :--- | :--- |
| 1 | | | |
| 2 | | | |
| 3 | | | |

---

## 6. Conclusión

En no más de un párrafo: ¿qué decisión cambiarías primero y por qué? ¿Qué
decisión defenderías tal como está?
