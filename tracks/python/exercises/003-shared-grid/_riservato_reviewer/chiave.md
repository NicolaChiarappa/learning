# Chiave — 003 (solo reviewer, formato leggero)

## Il difetto
Riga: `return [free_row for _ in range(rows)]`, con `free_row = [FREE] * seats_per_row` creata una volta fuori dal ciclo. `build_hall(3, 2)`: la lista esterna ha tre posizioni, tutte sulla stessa lista interna. Liste in tutto: 2. Correzione attesa: una lista nuova per ogni posizione, creata dentro il giro.

## Cosa dovrebbe esserci in "Prima di iniziare"
`hall[0]`, `hall[1]`, `hall[2]` guardano la stessa lista. Test rossi attesi: `book_seat` e `add_seat` (stessa causa); `close_row` verde; `free_per_row` rosso solo se nota `str(...)` (non è errore di modello non vederlo). Casi limite dalle regole: `rows=1` nasconde il difetto, `seats_per_row=0` con file multiple, negativi (R8, facoltativa), `add_seat` su sala con file vuote.

## Esperimenti attesi (in "Durante")
- Prova del difetto: `hall = build_hall(3, 2); print(hall[0] is hall[1], hall[1] is hall[2])` -> `True True`. Un esperimento valido ha un esito alternativo diverso (`False False`). Segnalare esperimenti che non possono smentire.
- `+=` contro `= ... +`, sul codice originale: `hall = build_hall(2, 2); hall[0] = hall[0] + ["free"]; print(len(hall[0]), len(hall[1]))` -> `3 2`; con `hall[0] += ["free"]` -> `3 3`. Con `= ... +` il test di `add_seat` diventa verde ma `book_seat` resta rotto: il difetto è in `build_hall`.
- Lettura del fallimento: `E  AssertionError: assert ['3', '3'] == [3, 3]`, `At index 0 diff: '3' != 3`. Sinistra = lista di due stringhe (apici = repr di stringa in contenitore), destra = due interi. Causa: `str(row.count(FREE))`; correzione: togliere `str(...)`.
- Test di regressione: deve fallire per la causa giusta (file condivise: `is`, oppure modifica di una fila che compare in un'altra), non per un'altra (es. stringhe). Verificare che fallisca sul codice originale: `seating.py` è identico a `original/` all'inizio.

## Sulla corretta lettura di `close_row`
`hall[row] = [CLOSED] * len(hall[row])` sposta la posizione su una lista nuova: solo quella fila esce dal gruppo condiviso. Per questo il test di `close_row` è verde sul codice originale.

## Forma attesa dei risultati
Dopo la correzione: `N passed`, N = 8 + test di regressione di Nick. Test nascosti: `pytest -q test_hidden.py` (file esplicito, non raccolto da pytest.ini).
