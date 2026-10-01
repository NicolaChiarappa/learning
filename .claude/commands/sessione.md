---
description: Avvia una sessione di studio su una track (python, django, typescript-react, capstone)
argument-hint: <track>
---

Avvia una sessione sulla track **$ARGUMENTS** seguendo il "Flusso di una sessione" in CLAUDE.md.

1. Controlla la data di oggi.
2. Leggi `tracks/$ARGUMENTS/progress.md`, `profile/errors.md` e l'ultimo file in `weekly/` (se esiste).
3. Se la track non ha ancora un `risultati.md` di ingresso, proponi di partire con `/test-ingresso $ARGUMENTS`.
4. Altrimenti dimmi in massimo 5 righe: dove sono arrivato, se ci sono ripassi in scadenza (hanno la priorità) e cosa proponi di fare ora.
5. Aspetta la mia conferma, poi invoca `exercise-designer`.
