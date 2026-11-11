# Action request

An **action request** asks one person to do something or to send you something (`act`): give me this data, fix these points, unblock this. When the reader has to choose between options, use [DECISION-REQUEST.md](DECISION-REQUEST.md) instead. Shape the message as **SBAR** (Situation, Background, Assessment, Recommendation), the handoff order clinicians use so the listener can act after the first sentence. It adds the structure below to the rules in [SKILL.md](SKILL.md).

## Gather

List every action and every answer the material shows as pending on that person, and what each one unblocks. Mark everything else you gathered as reference: work you finished, checks that passed, context that asks nothing of this reader. Done when every item is on one of the two lists.

## Shape

Write the four parts in this order. They are an order, not four headings: in a short message the situation and the assessment share the opening paragraph, and any heading uses the reader's own words.

1. **Situation**, the BLUF: what you need from this person, how many requests, by when, and what they unblock. One or two sentences.
2. **Background**: only what this reader lacks and needs in order to act, such as what changed since they last looked. Names they own stay bare. Reference items stay out of the message: give them one line with their count or a link, and list them in the notes for the user.
3. **Assessment**: what you think is going on, how sure you are (**Certainty**), and what it costs if the request waits: the risk that stays open or the work that stays blocked. State it once, in the opening when it is the reason to act, or beside the one request it explains.
4. **Recommendation**: the numbered requests. Each one asks for a single thing this person can do or answer, and names the form of the answer (a value, a yes, a date, a list). Add the reason only when the request does not explain itself.

The requests set the size: a message with four requests is about as long as four requests need.

<example>
Status first: `"Estado de la migración: 5 de 7 hallazgos hechos (detalle abajo) [...] Además necesito de ti cuatro datos."`
Request first: `"Lena, necesito cuatro datos de tu entorno antes del jueves 7 para saber si dos hallazgos ya están expuestos en producción. De los 7 hallazgos, 5 están resueltos en main y 2 a medias (detalle en la página del reparto)."`
</example>

## Check

Done when every item below holds:

- The cold reader can say, from the opening alone, what to do, how many things, and by when.
- Every request on the gathered list is numbered, asks one thing, and names the form of its answer.
- The background holds only what this reader lacks; each reference item is a count or a link in the message and sits in the notes for the user.
- The assessment says how sure you are and what waiting costs, and appears once.
- Any heading uses the reader's words; the four SBAR labels stay backstage.
