---
description: Avvia una sessione di studio su una track (python, django, typescript-react, capstone)
argument-hint: <track>
---

Avvia una sessione sulla track **$ARGUMENTS** seguendo il "Flusso di una sessione" in CLAUDE.md.

1. Controlla la data di oggi.
2. Leggi `tracks/$ARGUMENTS/progress.md`, `profile/errors.md` e l'ultimo file in `weekly/` (se esiste).
3. Se la track non ha ancora un `risultati.md` di ingresso, proponi di partire con `/test-ingresso $ARGUMENTS`.
4. Altrimenti decidi il tipo di sessione con la regola del "Formato Exercism" in CLAUDE.md (se la track lo usa): esercizio del sistema se c'è un ripasso in scadenza o se in questa settimana se ne sono fatti meno di 2, altrimenti il prossimo di `tracks/$ARGUMENTS/exercism/lista.md` (leggi anche `log.md` lì accanto).
5. Dimmi in massimo 3 righe: tipo di sessione, esercizio, cosa devo fare per primo.
6. Aspetta la mia conferma. Esercizio del sistema: invoca `exercise-designer`. Exercism: importalo con `tools/exercism_new.sh <slug>` e riassumimi la consegna in poche righe.
