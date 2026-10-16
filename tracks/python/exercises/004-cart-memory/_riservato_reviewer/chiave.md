# Chiave — 004 (solo reviewer)

## Il difetto
`def new_cart(customer, items=[], created_at=time.time())`: i due default sono valutati una volta, quando `def` viene eseguita. `items` è una lista unica per tutti i carrelli creati senza argomento (`new_cart.__defaults__[0] is cart["items"]`); `created_at` è un float fissato all'import (stesso valore per tutte le chiamate: il difetto esiste anche con un immutabile). `add_item` usa `cart["items"] += [...]`, che modifica sul posto la lista condivisa: è la riga che fa trapelare lo stato. `total_cents` ha `str(total)` (causa diversa, E006).

## Esiti attesi sul codice originale
Test base, ordine del file: 1 verde (primo a toccare il default), 2 verde (il default diventa `[tea]`), 3 ROSSO solo in sequenza (da solo verde: `-k items_keep` -> 1 passed), 4 ROSSO sempre (`assert '750' == 750`, sinistra str, destra int), 5 VERDE (`empty_cart` fa `cart["items"] = []`: sposta la posizione `items` di quel carrello su una lista nuova, il default non viene toccato; è lo stesso meccanismo di `close_row` in 003), 6 ROSSO sempre (stesso `created_at`). Totale 3 rossi / 3 verdi. Il test 5 verde è il punto E001/E004: chi prevede rosso "perché la lista è condivisa" ripete l'errore di 003.

## Esperimenti attesi
- A: `new_cart.__defaults__` -> `([], <float>)`; dopo `add_item(new_cart("x"), "tea", 300)` il primo elemento è `[('tea', 300)]` e `new_cart("y")["items"] is new_cart.__defaults__[0]` -> `True`.
- B: con `+=`, `mine == [('tea', 300)]` e `is` -> `True` (stesso oggetto, modificato sul posto); con `= ... +`, `mine == []` e `is` -> `False` (nuova lista, posizione `items` spostata). Dentro `add_item` la riga che fa trapelare il default è `+=`; con `= ... +` i test 1-3 diventano verdi lasciando il difetto (il default resta condiviso: lo vede `cart["items"] is new_cart.__defaults__[0]`, o `.append`/`.extend` fatti altrove).
- C sull'originale: `==` -> `True`, `is` -> `True` (con carrelli vuoti, senza add). Sul corretto: `==` -> `True`, `is` -> `False`. Il caso in cui `==` e `is` divergono è il corretto: per provare l'indipendenza serve `is`. Segnalare chi prova R2 con `==` (E007).
- Test di regressione: deve usare `is not` (o `id`) tra due carrelli freschi, oppure aggiungere a uno e guardare l'altro DOPO aver creato entrambi; un test che si limita ad aggiungere a un carrello e guardare quello stesso non vede il difetto. R7: non deve diventare verde con la sola modifica di `add_item` (con `= ... +` un test "aggiungo e guardo l'altro" diventa verde; `is not` no).

## Forma attesa dei risultati
Dopo la correzione: `N passed`, N = 6 + test di regressione di Nick. Nascosti: `$PY -m pytest -q _riservato_reviewer/test_hidden.py` (12 test; sull'originale 3 verdi, 9 rossi).
