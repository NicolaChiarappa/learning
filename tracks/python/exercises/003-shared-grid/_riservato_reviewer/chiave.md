# Chiave — 003 (solo reviewer)

## Il difetto
Riga: `return [free_row for _ in range(rows)]`, con `free_row = [FREE] * seats_per_row` creata una volta fuori dal ciclo. `build_hall(3, 2)`: la lista esterna ha tre posizioni, tutte sulla stessa lista interna. Liste in tutto: 2 (l'esterna e la lista condivisa). Correzione attesa in parole: una lista nuova per ogni posizione, creata dentro il giro (non fuori).

## Design sezione 1 (risposta attesa)
`hall[0]`, `hall[1]`, `hall[2]` guardano tutte la stessa lista (nome per ruolo a piacere), 2 liste in tutto.

## Design sezione 3 (previsione attesa)
Rossi: `test_book_seat_changes_only_that_seat`, `test_add_seat_grows_only_that_row` e `test_free_per_row_counts_free_seats` (quest'ultimo solo se Nick nota il `str(...)` leggendo il codice; non è un errore di modello non prevederlo). Verdi: gli altri cinque, compreso `test_close_row_closes_only_that_row`.

## Design sezione 4 (esperimento atteso)
Esempio: `hall = build_hall(3, 2); print(hall[0] is hall[1], hall[1] is hall[2])`. Se ha ragione (righe condivise): `True True`; se ha torto (la causa è altrove, es. `book_seat`): `False False`. Esce `True True`.

## Sezione A
Output sul codice originale: `3 failed, 5 passed`. Cause: gruppo 1 = `test_book_seat_changes_only_that_seat` + `test_add_seat_grows_only_that_row` (file condivise); gruppo 2 = `test_free_per_row_counts_free_seats` (restituisce stringhe).

## Sezione B (codice originale, `hall = build_hall(3, 2)`)
- `hall[row][seat] = TAKEN` → modifica un oggetto (la lista condivisa); dopo: `hall[0]`, `hall[1]`, `hall[2]` la guardano tutte, quindi il posto cambia in ogni fila.
- `hall[row] += [FREE]` → modifica sul posto la lista condivisa e poi riassegna la stessa lista alla posizione `row` (nessuna etichetta cambia di fatto); dopo: tutte e tre le posizioni guardano la lista allungata.
- `hall[row] = [CLOSED] * len(hall[row])` → sposta la posizione `hall[row]` su una lista nuova; dopo: solo `hall[row]` guarda la nuova lista, le altre due posizioni guardano ancora quella condivisa. Per questo il test di `close_row` passa.

## Sezione D (esperimento)
Sul codice originale: `hall = build_hall(2, 2); hall[0] = hall[0] + ["free"]; print(len(hall[0]), len(hall[1]))` → `3 2`; con `hall[0] += ["free"]` → `3 3`. Il test di `add_seat` diventerebbe verde con `= ... +`, ma `book_seat` resta rotto: il difetto è in `build_hall`, non in `add_seat`. Chi riscrive `add_seat` ha curato un sintomo e ha cambiato il comportamento solo nel punto in cui il test lo guarda.

## Sezione G
Riga attesa: `E       AssertionError: assert ['3', '3'] == [3, 3]` (e `At index 0 diff: '3' != 3`). Sinistra: lista di due stringhe (gli apici sono la rappresentazione di una stringa in un contenitore); destra: lista di due interi. Causa: `str(row.count(FREE))` in `free_per_row`. Correzione: togliere `str(...)`.

## Sezione K (se fatta)
Con `hall` corretta: `before = hall[0]; hall[0] += [FREE]; print(hall[0] is before)` → `True` (la lista è modificata sul posto, la posizione la riassegna uguale). Con `hall[0] = hall[0] + [FREE]` → `False`. Con `names = ["A", "B"]; alias = names[0]; names[0] += "*"; print(alias is names[0])` → `False`, e `alias` resta `'A'` (stringa nuova, posizione spostata).

## Forma attesa dell'output di pytest
Dopo la correzione: `N passed` con N = 8 (test base) + test di regressione di Nick.
