---
description: Consegna un esercizio per la valutazione (reviewer e mentor)
argument-hint: <track> <NNN>
---

Consegno l'esercizio indicato da: **$ARGUMENTS** (track e numero).

1. Trova la cartella `tracks/<track>/exercises/<NNN>-*/`.
2. Controlla che `design.md` sia compilato. Se è vuoto, fermati e dimmelo: non si valuta senza nota di design.
3. Invoca `reviewer` sulla cartella.
4. Invoca `mentor` in modalità esercizio sulla stessa cartella.
5. Riportami in modo diretto:
   - esito e punteggi
   - il punto più importante del reviewer
   - il pattern e l'abitudine indicati dal mentor
   - eventuali errori registrati in `errors.md`
6. Proponi il passo successivo (prossimo esercizio, variante da rifare o pausa).
7. Scrivi o aggiorna il log di oggi in `sessions/` e suggerisci un commit.
