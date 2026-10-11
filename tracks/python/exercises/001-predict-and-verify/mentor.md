# Mentor — 001

Data: 2026-10-11. Il contenuto tecnico è in `review.md`: qui c'è solo come hai lavorato.

## Cosa ho visto nel tuo ragionamento

- **Hai scritto il modello sbagliato prima di iniziare e non lo hai più toccato.** In `design.md` il modello è "devo capire se il tipo è mutabile o immutabile". Il README, venti righe sopra, ti dava la domanda giusta ("questa riga sposta un'etichetta o modifica un oggetto?"). Ti è stato fatto notare prima delle previsioni: hai aggiunto "probabilmente id()" e sei partito. Risultato: 4 errori su 4 sugli oggetti mutabili, cioè dove la tua regola non decide niente.
- **Le tue ipotesi non producono conseguenze, e le tue spiegazioni non vengono messe alla prova.** Snippet 9: scrivi "copy copia solo la struttura, deepcopy anche i valori" e poi prevedi lo stesso output per le due copie. L'ipotesi era quella giusta: non l'hai usata. Snippet 7: spieghi lo scarto con lo scope, poi lanci un esperimento con `items += [item]` che dà `True` con lo stesso identico scope, e non ti accorgi che ha appena smentito la spiegazione. L'esperimento lo sai costruire (snippet 3 e nota Django lo dimostrano). Quello che manca è chiederti, prima di lanciarlo, cosa dovrebbe uscire se hai ragione.
- **Il momento in cui l'esercizio insegna lo hai fatto fare a un altro.** Trascrizione, voti di sicurezza, confronto tra output e previsione, controllo di completezza: tutti delegati. Due volte "credo di aver finito" con campi obbligatori vuoti, senza lanciare i test. E le previsioni erano scritte nei file degli snippet, che il README diceva di non toccare.
- **I voti riga per riga erano onesti, il giudizio d'insieme no.** Sicurezza 5 → 4 giusti su 4; sicurezza 3 → 1 su 4. Poi però "7 su 9", "non ho fatto errori di ragionamento", "l'avrei fatta corretta" sullo snippet 10. Tre volte, sempre nello stesso verso. I tuoi stessi "non so" dicevano 5: bastava contarli.
- **Dove hai lavorato meglio: la nota Django.** Passi piccoli, un'ipotesi per volta, un esperimento tuo e diverso da quello suggerito, e una chiusura scritta come si deve: "credevo ne venisse costruito uno ogni volta". Cosa pensavi, cosa hai visto. È il formato che mancava negli scarti del 7 e del 9.

## Il pattern

Primo esercizio della track: il confronto è con il test d'ingresso del 2026-10-10.

**Confermati**
- *"Finito" senza controllare la consegna.* Nel test ti fermavi ai test verdi senza rileggere le regole. Qui non hai nemmeno lanciato i test. Anche scrivere le risposte dentro i file degli snippet è la seconda volta (nel test: snippet 03, 08, 09). La consegna continua a essere letta come contesto e non come elenco da spuntare. Non sta migliorando.
- *Giudizio complessivo più favorevole dei dati.* Nel test sovrastimavi le aree che usi ogni giorno. Qui sovrastimi il totale dopo aver stimato bene i singoli pezzi. Non è un problema di percezione: i dati giusti li avevi scritti tu, non li hai sommati.
- *Lo scarto archiviato come "cosa del linguaggio".* Nel test il bug era "assurdo". Qui è "non conoscevo alcuni comportamenti". Il tono è cambiato, la mossa è la stessa: la causa sta fuori dal tuo modello, quindi il modello non si corregge. Per il 3 e il 9 è in parte vero. Per il 7 no: la stessa riga (`x = x + [...]`) l'avevi prevista giusta nello snippet 2 e hai cambiato risposta solo perché stava dentro una funzione.
- *Nomi in italiano e per tipo* anche nel REPL (`dizionario`, `lista`, `Oggetto`, `costruisci`).

**In miglioramento, con evidenza**
- *Evitare ciò che non sai.* Nel test: tre esercizi su cinque saltati, tentativo a tempo rifiutato. Qui: "non so" alla prima stesura, poi un'ipotesi su tutti e nove gli snippet obbligatori. Servono ancora due solleciti, e lo snippet 10 è rimasto con i `?`. Ma hai tentato, e sullo snippet 2 l'ipotesi era giusta.
- *Spiegare il perché.* Nel test: 10 sezioni "Spiegazione" vuote su 10. Qui: 9 compilate su 9, con i nomi veri del codice. Il limite attuale è che la spiegazione si ferma al tipo e che la sintesi finale non contiene nessuna regola.
- *Chiedere.* "Cosa cavolo è il REPL?" subito, senza girarci intorno, e gli indizi sulla nota Django chiesti di tua iniziativa. Nel test l'aiuto arrivava perché eri fermo, non perché lo chiedevi.

**Nuovo**
- *Ipotesi e spiegazioni non portate alle conseguenze* (snippet 9, scarto del 7, frase sullo snippet 10). È il pattern che ha deciso l'esito "da rifare", più del 5/9.
- *Il feedback ricevuto non diventa revisione.* Tre osservazioni precise sul `design.md`, due parole aggiunte. Una sola occorrenza: lo segno e lo riguardo al prossimo esercizio.

## Da cambiare nel processo

**Una sola abitudine: niente esecuzione senza una riga "Atteso" scritta prima.**

Vale per gli snippet, e soprattutto per ogni esperimento che fai nel REPL durante l'analisi degli scarti. Prima di premere invio scrivi in `risposte.md`:

```
Atteso: <output esatto> perché <la spiegazione che sto mettendo alla prova>
```

Poi esegui e incolli sotto quello che è uscito. Se non coincide, la spiegazione è da buttare: lo scrivi e ne formuli un'altra. Se non sai cosa scrivere in "Atteso", non hai ancora un'ipotesi: hai solo voglia di guardare.

Perché questa e non un'altra: avrebbe fermato lo scarto del 7 (con "è una questione di scope" cosa ti aspettavi dalla versione con `+=`, e perché?) e la previsione del 9 (un'ipotesi che distingue `copy` da `deepcopy` deve dare due output diversi).

Come si verifica nel 002: ogni blocco REPL incollato in `risposte.md` ha la sua riga "Atteso" sopra. Zero eccezioni. Si conta.

**Condizione, non abitudine:** `risposte.md` lo compili tu dall'inizio alla fine, confronto compreso, e dici "consegno" solo dopo aver incollato l'output dei test di completezza. Il copia-incolla che volevi evitare si evita scrivendo direttamente nel file giusto.
