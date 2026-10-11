---
description: Consegna un esercizio per la valutazione (chiacchierata finale e reviewer)
argument-hint: <track> <NNN>
---

Consegno l'esercizio indicato da: **$ARGUMENTS** (track e numero).

1. Trova la cartella `tracks/<track>/exercises/<NNN>-*/`.
2. Controlla che la sezione "Prima di iniziare" di `appunti.md` sia compilata. Se è vuota, fermati e dimmelo: non si valuta senza nota di design.
3. Lancia i test sul codice e mostrami l'esito.
4. Fammi la chiacchierata finale (3-4 domande mirate, vedi "Formato leggero" in CLAUDE.md) e scrivi `verbale.md` nella cartella.
5. Invoca `reviewer` sulla cartella, passandogli `verbale.md` e la sezione "Formato leggero" di CLAUDE.md. Il `mentor` si invoca solo se questo è l'ultimo esercizio del modulo.
6. Riportami in modo diretto:
   - esito e punteggi
   - i 2-3 punti più importanti del reviewer
   - eventuali errori registrati in `errors.md`
7. Proponi il passo successivo (prossimo esercizio, variante da rifare o pausa).
8. Scrivi o aggiorna il log di oggi in `sessions/` e suggerisci un commit.
