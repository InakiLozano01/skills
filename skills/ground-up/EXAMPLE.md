# Examples: before and after

The domains are invented. The examples are in Spanish; the same moves apply in English.

- [Example 1: a decision request (`decide`, domain reader)](#example-1-a-decision-request-decide-domain-reader)
- [Example 2: a progress report in Slack thread format (`track`, engineering reader)](#example-2-a-progress-report-in-slack-thread-format-track-engineering-reader)
- [Example 3: a compact status reply for "how much is left?" (`track`, domain/product reader)](#example-3-a-compact-status-reply-for-how-much-is-left-track-domainproduct-reader)

---

## Example 1: a decision request (`decide`, domain reader)

### Before

An agent wrote this for the user to forward to Clara. It assumes the reader already knows the project.

> **Estado del dedupe**
>
> MATCH-12 queda bloqueado por IMP03. El importer de HC une fichas por nombre + especie y en sandbox vimos merges cruzados entre tutores. Opciones: A) exigir microchip para auto-merge; B) mantener heurística + teléfono y flaggear el resto. Necesitamos definición de Clara para avanzar con el PR #41.

The outsider cannot tell what VetRed's import does, what a "ficha" or a "merge cruzado" is, whether the problem happened to real customers, or what each option costs. The task codes act as subjects of sentences, and the question to Clara is never asked.

### After

> Clara, necesitamos que decidas cuándo el importer puede unir por su cuenta dos historias clínicas que parecen de la misma mascota.
>
> VetRed es una red de cuatro clínicas veterinarias. Cada mascota tiene una historia clínica: el registro de sus consultas, vacunas y tratamientos. Cuando una clínica se suma a la red, sus historias clínicas se copian al sistema central con un proceso de importación, que el equipo llama "importer".
>
> Para no crear la misma mascota dos veces, el importer une dos historias clínicas cuando coinciden el nombre de la mascota y la especie. Ese criterio falla cuando dos dueños distintos tienen, por ejemplo, un perro llamado Luna. En ese caso, las vacunas de una Luna pueden aparecer en la historia clínica de la otra.
>
> Reproducimos el problema con datos inventados en un entorno de prueba. No comprobamos que haya ocurrido con datos reales. Todavía no sabemos cuántas mascotas de la red comparten nombre y especie; ese conteo está en curso.
>
> Como responsable de la operación de las clínicas, la decisión es tuya. Hay dos opciones:
>
> - **Unir solo si coincide el microchip**, el número de identificación que muchas mascotas llevan bajo la piel. No habría uniones equivocadas. Las mascotas sin microchip quedarían duplicadas, y el personal de recepción tendría que unirlas a mano.
> - **Unir si coinciden el nombre, la especie y el teléfono del dueño**, y enviar a revisión los casos restantes. Habría menos duplicados, pero un dueño con dos mascotas del mismo nombre y especie seguiría expuesto a una unión equivocada.
>
> Las dos opciones no se revierten igual. Un duplicado se corrige después, uniendo las dos historias clínicas. Una unión equivocada es difícil de deshacer, porque alguien tiene que separar a mano qué consulta y qué vacuna es de cada mascota.
>
> Recomendamos la primera opción. Una historia clínica mezclada puede llevar a un tratamiento equivocado, y un duplicado solo genera trabajo administrativo. La regla quedaría así: si dos historias clínicas tienen el mismo microchip, el importer las une; si no, quedan separadas.
>
> Necesitamos tu respuesta antes del 10 de noviembre, cuando empieza la importación de la quinta clínica. La corrección ya está hecha y solo espera tu decisión.
>
> **Pregunta:** ¿el importer debe unir historias clínicas solo cuando coincide el microchip, aunque eso deje mascotas duplicadas que recepción tendrá que unir a mano?

### What changed

- The message opens with a **BLUF (Bottom Line Up Front)** line that names the topic and what Clara must do, addressing her as "tú" throughout.
- The domain basics are **grounded** next: what VetRed is, what a historia clínica is, and what the importer does. `"importer"` stays verbatim with an **appositive gloss** because the team uses that name.
- The problem is shown through a **concrete mechanism** and scenario (**Specification by Example**: two dogs named Luna) in place of `"merges cruzados"`.
- **Certainty** is explicit: reproduced with synthetic data, not verified in a real case, and the count is in progress.
- Each option shows what changes and who carries the cost. The text states which mistake is a **one-way door** (hard to reverse) and which is a **two-way door** (cheap to fix). The recommendation gives its reason and states the rule as it would enter the spec.
- Clara works in the **domain** bounded context, so the text speaks her **ubiquitous language** (pets, owners, vaccines, reception) and keeps the importer's code inside a **deep module**.
- `MATCH-12`, `IMP03`, and `PR #41` are omitted because Clara does not use them to decide. The text keeps the one operational fact that changes her timing: the fix is ready and waits on her answer.
- It ends with one short question Clara can answer with yes or no.

---

## Example 2: a progress report in Slack thread format (`track`, engineering reader)

### Before

An agent wrote this status update for Marco, a technical lead, as a wall of abstract prose.

> Marco, te paso el avance de la etapa 2 de DocVault. En docvault-engine ya abrimos PRs para versionado, idempotencia de jobs y el clasificador inicial con extracción. También hay un adaptador de grafo probado con mocks. En docvault-infra abrimos un PR con almacenamiento versionado, cola y entorno local. Además tenemos una rama local con cambios de recuperación y retiro de fuentes. Falta integrar las partes y probar todo junto; en main los endpoints siguen deshabilitados.

The reader cannot scan it on Slack, cannot see the global task vs. what stage 2 tackles, does not know what failure each piece prevents, has no PR links to inspect, and has to paste paragraphs that lose their structure.

### After

**Mensaje 1 (apertura del hilo en Slack):**

```text
:thread: Migración de DocVault - Avance de la etapa 2 (procesamiento de documentos)

RESUMEN EJECUTIVO

• Ya hay piezas implementadas y probadas localmente para registrar, procesar y conservar evidencia de los documentos sin duplicar trabajo ante reintentos.

• Los dos repositorios nuevos ya se conectaron en una primera prueba local a través de una cola de mensajes. La integración completa sigue en curso.

• Las funciones nuevas todavía no están disponibles para usuarios: falta integrar las ramas, probar el recorrido completo de un documento y activarlo en el entorno de destino.

cc @Marco (revisión de la cadena de PRs y validación contra la hoja de ruta)
```

**Mensaje 2 (respuesta dentro del hilo):**

```text
CONTEXTO

• DocVault guarda documentos legales para que los equipos puedan consultar qué cláusulas y vencimientos contienen.

• La tarea global es migrar esa capacidad a servicios separados. La etapa 2 aborda el recorrido intermedio: recibir un documento, procesarlo, vincular cada dato extraído con el archivo del que salió y dejarlo listo para búsquedas.

• docvault-engine contiene la lógica de documentos, versiones y extracción. docvault-infra prepara el almacenamiento, las colas de trabajo y el entorno para ejecutar ambos servicios juntos.

QUÉ AVANZÓ

• Procesamiento recuperable: docvault-engine registra un trabajo por cada documento y versión. Las pruebas locales comprueban que una entrega repetida reutiliza el mismo trabajo y no puede asignarse a otro cliente, es decir, a otro espacio aislado de documentos.
https://github.com/example-org/docvault-engine/pull/18

• Versiones y evidencia: si la versión 1 de un contrato está activa y llega una versión 2, la versión 1 sigue disponible para consultas mientras se procesa la nueva. La versión 2 solo la reemplaza cuando termina de verificarse. Ese comportamiento pasó pruebas locales; falta conectarlo al procesador completo.
https://github.com/example-org/docvault-engine/pull/22

• Entrega de trabajos por cola: docvault-engine guarda primero el evento en su base de datos y luego un proceso lo envía a la cola que organiza los trabajos pendientes, con pruebas de fallos y reintentos. Otro cambio comprueba que el mensaje recibido corresponda al documento y cliente correctos. Ambas piezas siguen inactivas hasta cerrar la recuperación.
https://github.com/example-org/docvault-engine/pull/25
https://github.com/example-org/docvault-engine/pull/29

• Clasificación y extracción: hay una implementación inicial que vincula cada cláusula extraída con la versión del archivo que la produjo. Para documentos largos, si las partes del documento discrepan sobre su tipo, el clasificador pide revisión en lugar de elegir uno. Probado con proveedores simulados; aún no conectado al procesamiento real.

• Infraestructura y primera conexión: el PR de integración de docvault-infra prepara el almacenamiento con historial de versiones, la cola y un entorno local. En ese entorno ya se comprobó la comunicación entre la cola y una copia local de docvault-engine.
https://github.com/example-org/docvault-infra/pull/14

CÓMO CONVERGE Y QUÉ SIGUE

• Una rama local de docvault-engine reúne los cambios de recuperación, retiro de fuentes dadas de baja y verificación de citas. Su integración y sus pruebas siguen en curso.

• El siguiente paso es encadenar y revisar los PRs abiertos, integrar las versiones de docvault-engine y docvault-infra, y demostrar en local que un documento recorre todo el flujo de punta a punta.

• En la rama principal (main) de docvault-engine, las consultas de búsqueda y cláusulas todavía responden como no disponibles.

PEDIDOS, DUDAS Y DEPENDENCIAS

• Revisión de PRs (@Marco): confirmar el orden de revisión de la cadena de versiones y cola (#18, #22, #25 y #29) antes de unir la rama de integración.

• Dependencia abierta: queda pendiente contrastar este estado con la hoja de ruta en Notion, a la que no hubo acceso en esta sesión.
```

### What changed

- The update splits into two copy-ready Slack blocks: a `:thread:` opener with a **BLUF** (`RESUMEN EJECUTIVO`) in plain words and a tag for Marco, and a thread reply with the structured detail using `•` bullets and blank lines that survive copy-paste.
- `CONTEXTO` grounds what DocVault does from zero, states the **global task** (service migration) and the slice this update covers (stage 2: the document processing path), and attaches **appositive glosses** to both repositories (`docvault-engine` and `docvault-infra`).
- `QUÉ AVANZÓ` groups work by capability rather than listing loose PRs. Each bullet builds **ground up** inside, passes the **portability test** by showing the **concrete mechanism** solved (version 1 staying live while version 2 processes; long documents with conflicting sections requesting review), states its **certainty** and where it was verified (local tests, simulated providers), and gives Marco the PR URLs as evidence.
- `CÓMO CONVERGE Y QUÉ SIGUE` shows how the local integration branch and the two repos come together, names the next step, and states plainly what `main` still returns today.
- `PEDIDOS, DUDAS Y DEPENDENCIAS` surfaces the review ask for Marco and **documents the null** on the Notion roadmap.

---

## Example 3: a compact status reply for "how much is left?" (`track`, domain/product reader)

### Before

A coworker asked on Slack: *"Necesitamos cerrar el documento de feedback de los operadores de CargoCheck hoy. ¿Cuánto falta?"*. An agent wrote operational notes to the user first, and then gave a 5-paragraph prose block full of unglossed shorthand and internal git mechanics:

> Ya despaché cuatro subagentes para extraer commits de la PR #310 en worktrees separados.
>
> Puedes responder:
>
> ```
> Ya fusionamos varias correcciones del feedback: el visor evita mezclar citas, se pueden reintentar páginas sin imagen y se vinculó la segunda firma con la corrida.
>
> Queda una parte importante. Ya hay trabajo implementado en una PR grande, pero esa PR mezcla muchos cambios y tiene conflictos con lo que ya fusionamos. La estamos dividiendo en entregas más pequeñas para revisarlas e integrarlas.
>
> Las primeras entregas cubren domicilio fiscal, balances ambiguos, páginas sin clasificar y revocaciones. En paralelo se trabajan los pendientes falsos, caras de DNI separadas y firmantes declarados.
>
> Después quedan la revisión de hallazgos, partes de la ficha y la medición sobre la muestra autorizada. Algunas reglas necesitan confirmación de Operaciones.
>
> Aún no tengo una estimación fiable de cierre: necesito los resultados de las primeras revisiones para separar lo que podemos integrar.
> ```

The reply is a wall of prose with no bullets, hides the proportion of the feedback document that is actually done vs. pending, exposes internal git merge-conflict details, drops unglossed shorthand ("segunda firma con la corrida", "pendientes falsos", "ficha", "muestra autorizada"), and ends with a defensive refusal to estimate without saying what can close today.

### After

**Mensaje listo para copiar a Slack (va primero):**

```text
De los 18 puntos del documento de feedback de los operadores, 8 ya están integrados en la rama principal (main), 7 ya tienen código escrito que estamos revisando por partes, y 3 esperan definición de Operaciones o pruebas finales. Todavía no están verificados en producción con casos reales.

YA RESUELTO EN MAIN (8 PUNTOS, PENDIENTE DE VALIDAR EN PRODUCCIÓN)

• Visor y citas: cada cita e imagen muestra únicamente páginas del archivo que se está revisando, sin mezclar páginas de otros documentos del mismo envío.

• Reintento de páginas en blanco: cuando una página llega sin imagen legible, el operador puede volver a procesarla sin recargar todo el envío.

• Trazabilidad de doble aprobación: cuando un envío exige dos aprobaciones ("segunda firma"), la segunda queda asociada a la misma ejecución de revisión ("corrida") que evaluó los documentos.

EN REVISIÓN E INTEGRACIÓN (7 PUNTOS)

• Cuatro correcciones ya están escritas y hoy las estamos separando en entregas chicas para revisar e integrar:
  - mostrar el domicilio fiscal detectado como candidato a revisar junto con el documento de donde salió;
  - marcar los balances contables donde el importe o la moneda se leen con duda;
  - avisar qué páginas de un archivo largo quedaron sin clasificar, manteniendo su número de página original;
  - enviar a revisión manual cualquier poder legal cuando no se pueda confirmar si sigue vigente o fue revocado.

• Tres mejoras siguen en desarrollo en paralelo:
  - reducir alertas falsas causadas por archivos mal clasificados;
  - unir las dos caras de un documento de identidad cuando llegan en páginas sueltas;
  - evitar que una lectura incompleta bloquee a un firmante que ya figura declarado en el formulario.

QUÉ FALTA O REQUIERE DEFINICIÓN (3 PUNTOS)

• Pantalla de resumen ("ficha") y edición de alertas: falta completar la vista con representantes y apoderados respaldados por sus documentos, y conservar las correcciones manuales del operador si se vuelve a correr el análisis.

• Definiciones pendientes de Operaciones: falta que el equipo de Operaciones confirme cómo calcular el vencimiento de los poderes y qué combinación de firmas exigir en cada caso (revisado en main y PRs abiertos; sin regla cerrada aún en el documento de Operaciones).

• Evaluación final: una vez integrados los cambios, falta volver a correr la prueba sobre el conjunto de envíos reales autorizados para medir precisión y tiempos.

CUÁNDO PODEMOS CERRARLO

• Hoy sí podemos dejar cerrado el documento de seguimiento actualizando el estado de los 18 puntos y dejando marcadas las preguntas para Operaciones.

• Para dar una fecha de cierre de todas las correcciones en el sistema, necesito que hoy terminen las revisiones de las primeras cuatro entregas y que Operaciones confirme las reglas pendientes.
```

---

*Nota para ti: las cuatro extracciones de la PR #310 siguen corriendo en ramas separadas basadas en `main` (`a1b2c3d`). La comparación anterior mide contra `main`; desde el repositorio no se ve qué versión está desplegada hoy en producción.*

### What changed

- The update is delivered after building a complete **traceability matrix** of the feedback document against `main`, and the copy-ready Slack block comes **first**, before the internal note to the user.
- The **BLUF** headline partitions all 18 items of the feedback document across state buckets (8 in `main`, 7 in review/integration, 3 waiting on work or definitions from Operaciones) and states that production verification is still pending.
- The 5-paragraph prose wall becomes scannable `•` bullets grouped by state (`YA RESUELTO EN MAIN`, `EN REVISIÓN E INTEGRACIÓN`, `QUÉ FALTA O REQUIERE DEFINICIÓN`, `CUÁNDO PODEMOS CERRARLO`).
- Every shorthand label is unpacked into a complete clause with **concrete mechanism** and behaviour or given an **appositive gloss** on first use (`"segunda firma"`, `"corrida"`, `"ficha"`), internal git conflict mechanics stay inside a **deep-module** phrase (`"ya están escritas y hoy las estamos separando en entregas chicas para revisar e integrar"`), and the pending rule **documents the null** (`"revisado en main y PRs abiertos; sin regla cerrada aún en el documento de Operaciones"`).
- The closing answers `"¿cuánto falta / hoy?"` constructively: it separates what **can** close today (updating the 18 items in the tracking document and surfacing the questions for Operaciones) from the concrete conditions that unlock the product ETA.
