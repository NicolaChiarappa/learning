# Note del designer — 002 (per il reviewer, Nick non le apre)

Gli output stanno solo in `chiave.md` (stessa cartella).

## Cosa allena
- E001: per ogni riga la domanda "sposta un'etichetta o modifica un oggetto?" invece di "mutabile o immutabile". Gli snippet 1 e 4 hanno la stessa riga (`+=`) con esiti opposti a seconda dell'oggetto, quindi la regola sul tipo da sola non decide; nello snippet 5 la stessa riga con indice (`snapshot[k] += ...`) fa le due cose.
- E005: `+=` su lista (snippet 1, 4, 5) contro tupla e stringa (1, 4, 5).
- E003: contenitori che conservano riferimenti (snippet 2; anche 5).
- E002: riassegnare contro mutare un parametro; coppia dentro/fuori funzione sulla stessa riga `log = []` (snippet 3); `+=` su parametro con argomento mutabile e immutabile (snippet 4).
- E004: copia superficiale, mutare un oggetto interno contro riassegnare una chiave (snippet 5).
- P02: abitudine "Atteso prima di eseguire" (campo e test). P04: stima derivata. P03: pytest incollato.

## Scelte di struttura
- 5 snippet, non 6: in 001 le previsioni sono costate circa 8 minuti a snippet; con spiegazione per riga e scarti strutturati 6 non starebbero in 60 minuti. Stima dichiarata 60 (consegna a 80 con nota di blocco).
- Snippet 1 e 4 non sono "facili sugli immutabili": gli immutabili compaiono come controparte di un'azione sulla lista.
- Il trasferimento (`transfer.py`) è costruito per fallire con la regola "dentro una funzione non si vede mai" e con la regola "riassegnare una chiave è come riassegnare un nome".
- Il test di completezza non esegue gli snippet e non confronta previsione e output: non deve fare da oracolo. Controlla: codice non alterato, righe nel formato, alternativa diversa dalla previsione se sicurezza <= 3, atteso con "perché" per ogni blocco di esperimento, stima derivata coerente con i campi.
- `pytest.ini` raccoglie solo `test_delivery.py`. I test del reviewer si lanciano con `pytest -q test_hidden.py` (file esplicito, funziona).

## Casi e trappole da guardare nella consegna
- Snippet 1: `ids_alias` e `label_alias` come "l'immutabile non cambia" (corretto ma motivazione per tipo, non per riga: chiedere cosa fa `+=` su una tupla). Previsione `TypeError` su `ids += (3,)`. Previsione che `names_alias` non cambi (E005 persistente).
- Snippet 2: `bundle[0] is bundle[1]` falso (E003); ultime due righe sbagliate per chi pensa che `menu["lunch"] = [99]` cambi `base_prices`. Output con `[[...],[...]]` senza spazi o con apici sbagliati.
- Snippet 3: terza riga `['x']` (E002); `result is session` True; confusione del `log` globale con il parametro. Ritorno della spiegazione "scope" (già vista in 001): se compare di nuovo, la riga non spostata dal chiamante è la prova.
- Snippet 4: `TypeError` previsto; `grown_tuple == as_tuple` True per chi pensa che la tupla venga modificata; terza riga False per chi pensa che il parametro sia sempre una copia.
- Snippet 5: `original["name"]` che diventa `'ada!'`; `original["scores"]` che diventa `[9]`; `tags` non condiviso (regola "copy copia solo il primo livello" applicata solo a metà).
- Trasferimento: previsione `{'tags': ['a']}` o `False` (E001/E002 non rientrati). La regola scritta senza domanda o senza distinzione tra nome nudo e indice a sinistra.
- Scarti: "Atteso" senza "perché" o senza un'ipotesi che discrimini; spiegazioni che reggono per costruzione (esperimento che non può dare un esito diverso dalla spiegazione); esperimenti con nomi per tipo o in italiano; blocchi REPL senza riga "Atteso" (test lo controlla solo in forma di conteggio).
- Calibrazione: confrontare "Chiusura delle previsioni" (dubbi, stima) con il numero reale di giusti; sicurezza per snippet contro esito, come in 001.

## Soluzione buona e soluzione eccellente
- Buona: 4-5 snippet giusti con output esatto, righe nella forma richiesta, scarti con esperimento e atteso scritti prima, stima coerente.
- Eccellente: nelle righe `+=` dice cosa fa l'operatore in base all'oggetto e propone un esperimento che lo prova (`id` prima e dopo); distingue "indice a sinistra" da "nome nudo" nella regola; la riga nuova è prevista giusta con la regola scritta prima, e la regola include il caso "dipende dall'oggetto" senza ricadere in "mutabile/immutabile"; i dubbi in `design.md` vengono sciolti da esperimenti poi citati negli scarti; `design.md` aggiornato a metà lavoro.
