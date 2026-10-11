# Errori ricorrenti

Registro degli errori *concettuali* (non i refusi). Lo aggiorna il reviewer; l'orchestratore lo legge a inizio sessione per proporre i ripassi.

Regole:
- errore nuovo → ripasso a +10 giorni
- errore ripetuto → occorrenze +1, ripasso a +7 giorni
- ripasso superato → stato "risolto" con data (la voce non si cancella)

| ID | Track | Errore (concetto) | Prima volta | Occorrenze | Ultimo esercizio | Ripasso il | Stato |
|---|---|---|---|---|---|---|---|
| E001 | python | Ragiona con la regola "mutabile o immutabile" invece che con la domanda "questa riga sposta un'etichetta o modifica un oggetto?"; dal 002: dice cosa fa la riga ma non chi guarda l'oggetto dopo | 2026-10-11 | 2 | python/002 | 2026-10-18 | aperto (in miglioramento) |
| E002 | python | Parametro di funzione trattato come la variabile del chiamante: riassegnarlo dentro la funzione creduto visibile fuori | 2026-10-11 | 1 | python/002 | — | risolto il 2026-10-11 (ripasso nello stesso giorno: riconfermare in V1) |
| E003 | python | Contenitore creduto una copia: mettere un oggetto in un dict o in una lista non lo copia, ne conserva il riferimento | 2026-10-11 | 1 | python/002 | — | risolto il 2026-10-11 (ripasso nello stesso giorno: riconfermare in V1) |
| E004 | python | Copia superficiale creduta indipendente a tutti i livelli; non distingue mutare un oggetto interno condiviso da riassegnare una chiave | 2026-10-11 | 2 | python/002 | 2026-10-18 | aperto |
| E005 | python | `+=` trattato come `= ... +`: su una lista modifica sul posto; dal 002 resta aperto solo il caso con indice a sinistra (`contenitore[chiave] += ...`) | 2026-10-11 | 1 | python/002 | 2026-10-21 | aperto (superato su nomi nudi e parametri) |
| E006 | python | Non distingue come Python mostra un valore: stringa stampata da sola (senza apici) contro stringa dentro un contenitore (con apici) | 2026-10-11 | 2 | python/002 | 2026-10-18 | aperto |

## Dettagli
<!--
### E001 — titolo breve
- Cosa succede: ...
- Perché è un errore: ...
- Esercizi in cui è comparso: python/003, python/007
-->

### E001 — Regola sul tipo al posto del modello nome → oggetto
- Cosa succede: Nick decide l'esito di una riga chiedendosi se il tipo è mutabile o immutabile. In `design.md` di python/001 il modello è descritto così, e non è stato cambiato dopo la segnalazione. Risultato: tutti gli snippet con immutabili giusti (4, 8), tutti e quattro gli errori (3, 5, 7, 9) su oggetti mutabili. Lo snippet 8 è giusto con motivazione incompleta ("int immutabile"), incoerente con quella data per il 7 ("il puntatore in ingresso viene riassegnato").
- Perché è un errore: "mutabile" dice che un oggetto può cambiare, non se la riga che si sta leggendo lo cambia. Su liste e dict la regola non decide nulla, e ogni caso nuovo viene vissuto come "comportamento del linguaggio che non conoscevo" (sintesi finale di 001) invece che come conseguenza ricavabile. È la radice di E002-E005.
- Come si riconosce che è risolto: per ogni riga rilevante Nick scrive, senza sollecito, "sposta un'etichetta" o "modifica un oggetto" e quali nomi guardano lo stesso oggetto dopo; la sintesi contiene una regola applicabile a codice mai visto.
- python/002 (2026-10-11): migliorato, non risolto. A favore: modello scritto come domanda in `design.md` e nella sintesi; 4/5 snippet giusti con sicurezza calibrata; trasferimento giusto; nella sintesi nomina da solo l'errore ("considero solo la mutabilità"). Contro: il criterio qui sopra non è soddisfatto: 26 voci di "Righe", nessuna con i nomi che guardano l'oggetto dopo, nonostante tre richieste. La regola sul tipo è ancora la prima mossa (`design.md`: "sono immutabili quindi per forza di cose il += costruisce un nuovo oggetto", scritto prima del modello). Conseguenza misurabile: snippet 5, ipotesi alternativa, `snapshot["name"] += "!"` descritta come "nuovo oggetto stringa" e poi `original["name"]` previsto `'ada!'`. Nel trasferimento la spiegazione ("riassegna la label a una nuova lista") non contiene il motivo per cui `row` vede la modifica. La regola finale non distingue nome nudo da indice a sinistra.
- Esercizi in cui è comparso: python/001, python/002

### E002 — Parametro = variabile del chiamante
- Cosa succede: in python/001 snippet 7 prevede che `items = items + [item]` dentro `with_item` modifichi `shopping` e che `other is shopping` sia `True`. La stessa riga fuori da una funzione (snippet 2) l'aveva prevista giusta. Nell'analisi dello scarto attribuisce la differenza allo scope ("variabile che vive esclusivamente nello scope della funzione"), che però è identico in `add_item`, dove la modifica si vede; il suo stesso contro-esperimento con `items += [item]` lo smentisce senza che se ne accorga.
- Perché è un errore: senza distinguere "il parametro è un nome locale attaccato allo stesso oggetto" da "il parametro è il nome del chiamante" non si può decidere se una funzione modifica i propri argomenti, che è il focus di design di M01 (esercizio 5) e la base di M05.
- python/002 (2026-10-11): ripasso superato. Snippet 3 (stessa riga `log = []` dentro e fuori da una funzione) e snippet 4 (`+=` su parametro, lista e tupla) giusti con sicurezza 5; trasferimento giusto compreso `same is row`. Lo scarto del 7 di 001, riscritto, attribuisce la differenza alla riga e non più allo scope. Limite: verifica nello stesso giorno dell'errore; nelle spiegazioni non scrive che alla chiamata parametro e argomento guardano lo stesso oggetto. Da riconfermare in V1 e in M01 esercizio 5.
- Esercizi in cui è comparso: python/001

### E003 — Il contenitore come copia
- Cosa succede: in python/001 snippet 5 prevede che `history = {"first": morning}` conservi una copia ("io credo una copia"), quindi `[1,2,3]` e `True` dopo `morning.append(4)`. Nello snippet 1 aveva previsto correttamente che `backup = scores` condivide l'oggetto: stesso meccanismo, due risposte. Lo scarto è corretto nel meccanismo, provato nel REPL senza `is`.
- Perché è un errore: è la causa diretta dei bug di aliasing in strutture annidate (M01 esercizio 2) e, in Django, dei dati condivisi tra richieste o tra istanze.
- python/002 (2026-10-11): ripasso superato. Snippet 2 giusto con sicurezza 5 e spiegazione corretta ("due riferimenti alla lista base_prices"), compreso `bundle[0] is bundle[1]`. Limite: verifica nello stesso giorno; la stessa idea ("copie dei valori") ricompare nello snippet 5 per `dict(original)`, contata sotto E004. Da riconfermare in "La griglia condivisa" e in V1.
- Esercizi in cui è comparso: python/001

### E004 — Copia superficiale contro profonda
- Cosa succede: in python/001 snippet 9 prevede `menu` invariato dopo `shallow["starters"].append("salad")` e `shallow["mains"] is menu["mains"]` falso. L'ipotesi scritta ("copy copia solo la struttura, deepcopy anche i valori") portava alla risposta giusta ma non è stata tradotta in conseguenze: stessa previsione per le due copie. Lo scarto non ha prova REPL e non spiega perché `desserts` non compare in `menu`.
- Perché è un errore: scegliere tra copia superficiale e profonda motivando è un obiettivo di M01; senza la distinzione tra mutare un oggetto condiviso e riassegnare una chiave la scelta è casuale.
- python/002 (2026-10-11): ricaduta. Snippet 5: per `snapshot = dict(original)` sceglie "nuovo dizionario con le copie dei valori" (sicurezza 3) e prevede `tags` non condiviso. In `design.md`, prima delle previsioni, aveva scritto l'ipotesi giusta ("comportamento uguale al copy, non deepcopy", `is` → true), e nello scarto del 9 di 001 lo aveva appena provato nel REPL: né l'una né l'altro sono arrivati alla previsione. Seconda metà dell'errore: `snapshot["scores"] = [9]` letta come "aggiunge in coda il 9" (riassegnare una chiave scambiato per mutare l'oggetto), mentre `menu["lunch"] = [99]` nello snippet 2 e `record["tags"] = ...` nel trasferimento sono lette bene. Scarto: esperimento che conferma solo ciò che l'output mostrava già, "Atteso" senza perché, nessuna prova sulle due righe lette male.
- Esercizi in cui è comparso: python/001, python/002

### E005 — `+=` come scorciatoia di `= ... +`
- Cosa succede: in python/001 snippet 3 prevede che `backup += [10]` crei una lista nuova. Lo scarto è analizzato bene per le liste (esperimento di contrasto con `is`). La regola ricavata non è stata provata su tuple, stringhe, int. Sullo snippet 10 dichiara a posteriori "l'avrei fatta corretta": né la regola di prima né quella di dopo danno l'output reale.
- Perché è un errore: il comportamento di `+=` dipende dall'oggetto; una regola imparata su un solo tipo diventa la prossima regola memorizzata (rischio: "`+=` modifica sempre").
- python/002 (2026-10-11): superato su nomi nudi e parametri. Snippet 1 e 4 giusti: lista modificata sul posto e vista dall'alias, tupla e stringa sostituite con l'alias fermo sul vecchio oggetto, nessun `TypeError` previsto per `list += tuple`. Non superato con indice a sinistra: snippet 5, ipotesi alternativa, `snapshot["name"] += "!"` previsto visibile in `original`; nello scarto lo riconosce ("non ho notato che il += sulle stringhe costruisce un nuovo oggetto") ma non lo prova. Occorrenze e data di ripasso lasciate invariate: l'errore non è nella previsione scelta, e la previsione scelta sui casi di 001 è giusta.
- Esercizi in cui è comparso: python/001, python/002 (solo `contenitore[chiave] += ...`)

### E006 — Come Python mostra un valore: `str` contro `repr`
- Cosa succede: python/001, snippet 7: `[milk, eggs, tea]` senza apici per una lista di stringhe. python/002, snippet 1: `"ab"` tra virgolette per `print(label_alias)`, e lo stesso testo riscritto a mano nel campo "Output ottenuto" al posto dell'output reale, senza notare la differenza. Il README di 002 dava la regola e un esempio.
- Perché è un errore: `print` di una stringa mostra il testo; una stringa dentro un contenitore viene mostrata con gli apici. Chi non ha la distinzione non legge l'output di un test fallito (`'5'` contro `5`) né un valore nel debugger. Serve da M02.
- Cosa NON è in questa voce: spazi dopo le virgole, virgolette doppie al posto delle singole, `false`/`true` minuscoli (0/9 in 001, 0/5 in 002 come output esatto). Sono disattenzione verso una regola scritta, non un concetto mancante: restano nota di processo in `progress.md` (pattern P03).
- Registrato il 2026-10-11 con 2 occorrenze perché osservato in due esercizi; ripasso a +7 giorni.
- Esercizi in cui è comparso: python/001, python/002
