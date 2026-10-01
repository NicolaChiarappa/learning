---
description: Prepara il test d'ingresso di una track, oppure lo valuta se l'ho già svolto
argument-hint: <track>
---

Gestisci il test d'ingresso della track **$ARGUMENTS**.

1. Cerca in `tracks/$ARGUMENTS/assessment/` una cartella `*-ingresso`.
2. **Se non esiste:** invoca `assessor` con `track=$ARGUMENTS`, `fase=prepara`, `tipo=ingresso`. Poi dimmi dove si trova il test, quanto dura e in che ordine svolgerlo. Ricordami di non usare l'IA durante il test.
3. **Se esiste ma non c'è `risultati.md`:** chiedimi conferma che ho finito, poi invoca `assessor` con `fase=valuta`. Subito dopo invoca `planner` con `modalità=crea`. Riportami:
   - la sintesi dei risultati
   - le aree dove mi sono sovrastimato o sottostimato
   - i primi 2 moduli della roadmap
4. **Se esiste già `risultati.md`:** dimmelo e proponi `/verifica $ARGUMENTS` o `/sessione $ARGUMENTS`.
