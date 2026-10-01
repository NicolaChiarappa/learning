---
description: Mini-verifica periodica di una track (ogni 2 settimane), con aggiornamento della roadmap
argument-hint: <track>
---

Gestisci la mini-verifica della track **$ARGUMENTS**.

1. Cerca in `tracks/$ARGUMENTS/assessment/` l'ultima cartella `*-verifica`.
2. **Se non ce n'è una aperta (senza `risultati.md`):** invoca `assessor` con `fase=prepara`, `tipo=verifica`. Dimmi dove si trova e quanto dura.
3. **Se ce n'è una aperta:** chiedimi conferma che ho finito, poi invoca `assessor` con `fase=valuta` e subito dopo `planner` con `modalità=aggiorna`.
4. Riportami cosa è cambiato rispetto al test precedente e come cambia la roadmap.
