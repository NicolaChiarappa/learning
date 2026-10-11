# 003 — La griglia condivisa
Modulo: M01 | Difficoltà: 3 | Tempo: 45-60 minuti | Tipo: nuovo (riprende E001, E004, E005, E006)

Trovare un difetto in codice non tuo, spiegarlo, correggerlo e dimostrare la correzione. Niente snippet da prevedere.

## Teoria essenziale
Un'assegnazione non copia: crea o sposta un'etichetta, e l'oggetto resta uno solo. Una lista ha **posizioni** (`x[0]`, `x[1]`, ...), e ciascuna guarda un oggetto, come un nome. Quando una lista ne contiene altre, la domanda per ogni riga è: sposta una posizione o modifica un oggetto? E dopo, chi altro guarda quell'oggetto?

```python
tags_a = ["red"]
catalog = [tags_a, ["blue"]]
catalog[1] = ["green"]       # index on the left of "=": acts on a position of catalog
print(tags_a, catalog)       # ['red'] [['red'], ['green']]
```

`x[i] += y` e `x[i] = x[i] + y` sono la stessa riga? Non darlo per scontato: verificalo con un esperimento. Documentazione: Language Reference, "Augmented assignment statements".

`print("ab")` scrive `ab`, ma dentro un contenitore le stringhe mostrano gli apici: `print(["ab"])` scrive `['ab']`. pytest mostra sempre questa forma. Un test fallito si legge così: `E  assert <valore restituito> == <valore atteso>`, e sotto `At index N diff: ...` dice il primo punto in cui differiscono.

Dopo la correzione, non prima: Python Programming FAQ, "How do I create a multidimensional list?".

## Il problema
`seating.py` è la mappa dei posti di una piccola sala: una sala è una lista di file, una fila è una lista di posti (`"free"`, `"taken"`, `"closed"`). Nella demo con una fila funziona. In produzione dicono che "la mappa si comporta in modo strano dopo alcune operazioni" e che "il conteggio dei posti liberi non quadra". Non c'è altro.

Regole della versione corretta:
- **R1** `build_hall(rows, seats_per_row)` restituisce `rows` file, ciascuna con `seats_per_row` posti, tutti `"free"`.
- **R2** Le file sono indipendenti: cambiare un posto o la lunghezza di una fila non cambia mai nessun'altra fila, subito dopo `build_hall` e dopo qualunque sequenza di operazioni.
- **R3** `book_seat(hall, row, seat)` mette quel posto a `"taken"` e non cambia nient'altro.
- **R4** `add_seat(hall, row)` aggiunge un posto `"free"` in fondo a quella fila e a nessun'altra.
- **R5** `close_row(hall, row)` mette tutti i posti di quella fila a `"closed"`; la fila resta della stessa lunghezza, le altre non cambiano.
- **R6** `free_per_row(hall)` restituisce una lista di **int**, uno per fila, con il numero di posti `"free"`.
- **R7** Le dimensioni zero sono valide: `build_hall(0, n)` è `[]`; `build_hall(n, 0)` sono `n` file vuote, indipendenti.
- **R8** (facoltativa, solo se hai tempo) Una dimensione negativa solleva `ValueError` con un messaggio che contiene il nome dell'argomento sbagliato.
- **R9** `book_seat`, `add_seat`, `close_row` modificano la sala ricevuta e restituiscono `None`; ogni chiamata a `build_hall` restituisce una sala senza niente in comune con le altre.

I test base **non** coprono tutte le regole: coprono i casi normali e un caso limite ovvio. Quali restano scoperte lo dici tu in `appunti.md`.

## Cosa fare
1. Leggi `seating.py`, `test_seating.py` e le regole. Non eseguire niente.
2. Scrivi "Prima di iniziare" in `appunti.md`.
3. Lancia i test base ed esegui gli esperimenti che ti servono (niente pythontutor). Prima di ogni esecuzione scrivi in "Durante" cosa ti aspetti, e quale risultato diverso ti smentirebbe; poi incolla l'output dal terminale.
4. Scrivi `test_regression.py`: un test tuo che riproduce il difetto, per la causa giusta, e **fallisce sul codice originale** (`original/seating_original.py` è una copia di riferimento: non modificarla).
5. Correggi `seating.py` cambiando il minimo. Non toccare firme, nomi di funzioni e `test_seating.py`.
6. Scrivi "Dopo" in `appunti.md`.

Nomi, codice e commenti di prova in inglese e per ruolo, non per tipo. Appunti in italiano.

## Comandi
```bash
cd /Users/nicolachiarappa/Desktop/Projects/learning/tracks/python/exercises/003-shared-grid
PY=/Users/nicolachiarappa/Desktop/Projects/learning/.venv/bin/python
$PY -m pytest -q        # test_seating.py + test_regression.py
```
All'inizio alcuni test base sono rossi: è il punto dell'esercizio. `seating.py` parte identico a `original/`: lancia `test_regression.py` prima di correggere e incolla il rosso in "Durante".

## Consegna
Quando i test passano e `appunti.md` ha le tre parti, scrivi all'orchestratore "consegno 003": ti farà 3-4 domande in chat e poi partirà la review.

Se dopo 20 minuti sei bloccato, scrivi in "Dopo" dove, cosa hai provato e che ipotesi hai: un tentativo minimo onesto vale come consegna.
