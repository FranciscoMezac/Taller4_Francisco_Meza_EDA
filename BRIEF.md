# BRIEF — Taller 4: Auditoría de un B-Tree

## 1. Qué vas a hacer

Recibes un B-Tree **ya implementado y funcionando**. Tu tarea no es
programarlo de nuevo: es **auditarlo**.

El código pasa sus pruebas. Eso no significa que esté bien diseñado. Tu
trabajo es identificar decisiones de diseño e implementación que sean
discutibles, explicar su impacto y proponer alternativas con su costo.

La pregunta que guía todo el taller es:

> Si este B-Tree tuviera que operar sobre un índice real de millones de
> claves, ¿qué decisiones defenderías y cuáles cambiarías?

---

## 2. Qué se te entrega

- `src/btree/node.py`: el nodo.
- `src/btree/tree.py`: el árbol, con búsqueda, inserción, borrado,
  métricas y validación.
- `src/btree/metrics.py`: contadores de operaciones.
- `src/main.py`: una demostración ejecutable.
- `tests/`: pruebas del comportamiento actual.

No se te pide modificar la implementación. Se te pide entenderla, diagramarla
y auditarla.

---

## 3. Qué debes observar

No hay una lista de respuestas. Estas son las dimensiones que se espera que
audites:

- **Modelo de costo:** ¿qué se cuenta y qué no? ¿Comparaciones, nodos,
  transferencias, bytes?
- **Capacidad y memoria:** ¿cómo se dimensiona un nodo? ¿Qué pasa con el
  tamaño de las claves y de los punteros?
- **Búsqueda dentro del nodo:** ¿cómo se recorre un nodo y cuánto cuesta?
- **Inserción y split:** ¿cuándo se parte un nodo? ¿Qué pasa con las claves
  duplicadas? ¿Qué se mueve y cuánto cuesta?
- **Borrado:** ¿qué hace el código cuando elimina una clave? ¿Es la operación
  que esperarías de un B-Tree?
- **Ocupación:** ¿qué fracción del nodo se usa? ¿Depende del orden de
  inserción?
- **Estructura del nodo:** ¿qué atributos son redundantes? ¿Hay localidad?
- **Contrato de claves:** ¿qué tipos de clave acepta? ¿Qué pasa si no son
  comparables?
- **Validación:** ¿qué invariantes comprueba? ¿A qué costo?
- **Altura:** ¿cómo se calcula? ¿Qué supone?

Para cada dimensión, busca la línea de código, explica el efecto y propone
una alternativa. No basta con decir “esto es ineficiente”: hay que decir
**por qué**, **cuánto** y **en qué condición**.

---

## 4. Entregables

### 4.1 `AUDIT.md`

Debe contener:

1. **Matriz de costos** de las operaciones principales, con modelo de costo
   explícito (RAM, E/S, o ambos) y condición (N, B, M).
2. **Justificación por traza** de al menos dos operaciones: no se pide una
   demostración formal ni recurrencias; se pide seguir el código con un
   ejemplo pequeño y contar.
3. **Hallazgos de diseño e implementación**, con:
   - ubicación en el código;
   - qué decisión se tomó;
   - por qué es discutible;
   - impacto;
   - propuesta de mejora y su costo.
4. **Evidencia**: líneas, trazas, salidas de tests o métricas.

### 4.2 Diagramas en `design/`

- Un diagrama de **clases** que refleje la estructura real del código.
- Un diagrama de **secuencia** del flujo principal.

No se evalúa que el dibujo sea “bonito”, sino que sea **fiel al código**.
Si el código tiene tres clases, el diagrama no puede tener dos. Si el
borrado reconstruye el árbol, el diagrama no puede mostrar un borrado
estándar con préstamo y fusión.

### 4.3 Defensa oral

El docente te pedirá explicar una parte del código y hacer una modificación
en vivo. La defensa no es un examen de memoria: es la comprobación de que
entiendes lo que auditaste.

### 4.4 Mínimo para aprobar

No se espera que encuentres todas las decisiones posibles. El mínimo es:

- un diagrama de clases con las tres clases y sus relaciones;
- un diagrama de secuencia de `insert`;
- **tres hallazgos** con ubicación, explicación, impacto y propuesta;
- una defensa oral básica.

Los hallazgos pueden ser de diseño o de deuda de implementación. No es
obligatorio encontrar un error de correctitud. Si encuentras más de tres,
mejor; pero tres bien argumentados son suficientes para el piso.

### 4.5 Autochequeo antes de entregar

Antes de cerrar el trabajo, verifica:

- **☐** Mi diagrama de clases muestra las tres clases y sus relaciones.
- **☐** Mi diagrama de secuencia muestra el flujo de `insert`.
- **☐** Mi `AUDIT.md` tiene al menos tres hallazgos.
- **☐** Cada hallazgo indica línea, impacto y propuesta.
- **☐** Mi matriz declara el modelo de costo y las condiciones `N`, `B`, `M`.
- **☐** Incluí al menos dos trazas, no solo fórmulas.
- **☐** Puedo explicar mis hallazgos sin leer.
- **☐** Puedo modificar una parte del código en vivo.

No necesitas encontrar todas las decisiones posibles. Con tres hallazgos
sólidos y los diagramas, cumples el mínimo.

---

## 5. Reglas

- Trabajo individual.
- En la sesión presencial, sin IA.
- No reescribas el código durante la auditoría: documenta.
- Puedes ejecutar el código y los tests tantas veces como quieras.
- Si encuentras un defecto de correctitud, documéntalo con una traza o un
  test; no lo arregles sin autorización.

---

## 6. Tiempo

El taller se desarrolla en **dos sesiones**. No hay un reparto rígido por
bloque: tú decides cuánto tiempo dedicas a leer, ejecutar, diagramar,
auditar y preparar la defensa.

La recomendación es simple: no dejes la auditoría para el final. El código
se entiende mejor ejecutándolo y trazando operaciones concretas.

---

## 7. Evaluación

Se evalúan cuatro dimensiones:

- fidelidad de los diagramas al código;
- modelado del flujo dinámico;
- calidad del análisis de costos y de los hallazgos;
- dominio en la defensa oral.

No se evalúa la cantidad de hallazgos ni la calidad estética del código.
Se evalúa **tu capacidad de leer, explicar y cuestionar** decisiones
técnicas. Los tres hallazgos del mínimo son el piso; los hallazgos
adicionales y más finos son señales de excelencia, no requisitos.

---

## 8. Preguntas de arranque

Antes de escribir `AUDIT.md`, intenta responder:

1. ¿Qué operación domina el costo del taller y por qué?
2. ¿Dónde se pierde la analogía “nodo = bloque”?
3. ¿Qué decisión de diseño cambia más la altura o la ocupación?
4. ¿Qué pasa si insertas claves duplicadas?
5. ¿Qué pasa si borras una clave?
6. ¿Qué parte del código no podrías defender en producción y por qué?
