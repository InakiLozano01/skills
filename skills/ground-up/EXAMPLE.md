# Example: a decision request, before and after

The domain is invented. The example is in Spanish; the same moves apply in English.

## Before

An agent wrote this for the user to forward to Clara. It assumes the reader already knows the project.

> **Estado del dedupe**
>
> MATCH-12 queda bloqueado por IMP03. El importer de HC une fichas por nombre + especie y en sandbox vimos merges cruzados entre tutores. Opciones: A) exigir microchip para auto-merge; B) mantener heurística + teléfono y flaggear el resto. Necesitamos definición de Clara para avanzar con el PR #41.

The outsider cannot tell what VetRed's import does, what a "ficha" or a "merge cruzado" is, whether the problem happened to real customers, or what each option costs. The task codes act as subjects of sentences, and the question to Clara is never asked.

## After

> VetRed es una red de cuatro clínicas veterinarias. Cada mascota tiene una historia clínica: el registro de sus consultas, vacunas y tratamientos. Cuando una clínica se suma a la red, sus historias clínicas se copian al sistema central con un proceso de importación, que el equipo llama "importer".
>
> Para no crear la misma mascota dos veces, el importer une dos historias clínicas cuando coinciden el nombre de la mascota y la especie. Ese criterio falla cuando dos dueños distintos tienen, por ejemplo, un perro llamado Luna. En ese caso, las vacunas de una Luna pueden aparecer en la historia clínica de la otra.
>
> Reproducimos el problema con datos inventados en un entorno de prueba. No comprobamos que haya ocurrido con datos reales. Todavía no sabemos cuántas mascotas de la red comparten nombre y especie; ese conteo está en curso.
>
> Clara, como responsable de la operación de las clínicas, tiene que decidir cuándo el importer puede unir dos historias clínicas por su cuenta. Hay dos opciones:
>
> - **Unir solo si coincide el microchip**, el número de identificación que muchas mascotas llevan bajo la piel. No habría uniones equivocadas. Las mascotas sin microchip quedarían duplicadas, y el personal de recepción tendría que unirlas a mano.
> - **Unir si coinciden el nombre, la especie y el teléfono del dueño**, y enviar a revisión los casos restantes. Habría menos duplicados, pero un dueño con dos mascotas del mismo nombre y especie seguiría expuesto a una unión equivocada.
>
> Las dos opciones no se revierten igual. Un duplicado se corrige después, uniendo las dos historias clínicas. Una unión equivocada es difícil de deshacer, porque alguien tiene que separar a mano qué consulta y qué vacuna es de cada mascota.
>
> Recomendamos la primera opción. Una historia clínica mezclada puede llevar a un tratamiento equivocado, y un duplicado solo genera trabajo administrativo. La regla quedaría así: si dos historias clínicas tienen el mismo microchip, el importer las une; si no, quedan separadas.
>
> La respuesta hace falta antes del 10 de noviembre, cuando empieza la importación de la quinta clínica. La corrección está lista para revisión (PR #41) y espera esta decisión.
>
> **Pregunta para Clara:** ¿el importer debe unir historias clínicas solo cuando coincide el microchip, aunque eso deje mascotas duplicadas que recepción tendrá que unir a mano?

## What changed

- The domain comes first: what VetRed is, what a historia clínica is, and what the importer does. "importer" stays, with a gloss, because the team uses that name.
- The problem is told as a concrete case, two dogs named Luna, in place of "merges cruzados".
- Certainty is explicit: reproduced with invented data, not seen in a real case, and the count is in progress.
- Each option says what changes and who carries the cost. The text says which mistake is hard to reverse (a one-way door) and which is cheap to fix (a two-way door). The recommendation gives its reason and states the rule as it would enter the spec.
- Clara owns the clinics' operation, so the text speaks her language: pets, owners, vaccines, reception. The importer's code stays out of sight.
- MATCH-12 and IMP03 are gone, because Clara does not need them to decide. PR #41 stays after a plain description, because someone will look for it.
- The message is short, so it has no headings. It ends with one question Clara can answer with yes or no.
