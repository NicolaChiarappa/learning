# Note del designer — 003 (per il reviewer, Nick non le apre)

La chiave con gli esiti attesi è in `chiave.md` (stessa cartella). Il pytest.ini non raccoglie `test_hidden.py`: lancialo con il file esplicito (`pytest -q test_hidden.py`, dalla cartella dell'esercizio).

## Cosa allena
- E001: il "chi guarda cosa" è il contenuto dell'esercizio (design sezione 1, sezione B), non un campo di compilazione. Solo sulle righe con indice a sinistra e sul contenitore annidato.
- E003 (riconferma): la lista esterna conserva riferimenti; lo stesso oggetto è guardato da tre posizioni.
- E004: riassegnare una posizione (`hall[row] = ...`, `close_row`) contro mutare l'oggetto guardato (`hall[row][seat] = ...`, `book_seat`; `hall[row] += ...`, `add_seat`). Per questo il test di `close_row` è verde sul codice difettoso.
- E005 (ambito `contenitore[chiave] += ...`): `hall[row] += [FREE]` modifica sul posto la lista condivisa; `hall[row] = hall[row] + [FREE]` crea una lista nuova e sposta la posizione. Assorbe la precondizione non svolta di 002 (snippet 5).
- E006: `free_per_row` restituisce `['3', '3']` invece di `[3, 3]`; pytest mostra `assert ['3', '3'] == [3, 3]` e `At index 0 diff: '3' != 3`. Difetto volutamente indipendente dall'aliasing: serve anche a verificare se Nick attribuisce tutti i rossi alla stessa causa (sezione A, "cause raggruppate").
- P02: abitudine a due esiti scritti prima di eseguire (design sezione 4, risposte D, K). P03: spunta delle regole, output incollato, test lasciati rossi con motivazione. P04: stima dei test nascosti, coerente con i "no"/"non so". P07: casi limite ricavati dalle regole, su chiamate concrete. P09/P10: tempo con punti di controllo a 40/70/100 e regola di taglio.

## Il difetto (anche in `chiave.md`)
`build_hall` costruisce una sola lista `free_row` e la mette in tutte le posizioni della lista esterna: `hall[0] is hall[1] is hall[2]`. Due liste in tutto per `build_hall(3, 2)`: l'esterna e quella condivisa. Costume diverso dal test d'ingresso: la lista è creata prima e riusata in una comprehension, che sembra costruire file nuove a ogni giro.

## Perché i test base si comportano così
Verdi sul codice originale (5): forma, zero file, una sola fila, `close_row`, `book_seat` che restituisce `None`. Rossi (3): `test_book_seat_changes_only_that_seat` e `test_add_seat_grows_only_that_row` (aliasing, stessa causa), `test_free_per_row_counts_free_seats` (stringa invece di int, causa diversa).
`close_row` è verde perché `hall[row] = ...` sposta la posizione su una lista nuova: l'unica fila che "esce" dal gruppo condiviso è quella chiusa.

## Test nascosti suggeriti (10, ogni regola almeno un test)
1. R1: forma con più dimensioni (es. `build_hall(3, 4)`), tutti `"free"`.
2. R2: `build_hall(3, 2)`, nessuna coppia di file con `is` uguale; `hall[0] is not hall[1]`.
3. R2/R3: `book_seat` su file diverse in sequenza; verificare tutte le posizioni.
4. R4: `add_seat` due volte su file diverse; lunghezze `[3, 2, 3]` o equivalenti.
5. R5: `close_row` e poi `add_seat` sulla stessa fila e su un'altra (la fila chiusa non deve più condividere né essere condivisa).
6. R6: tipi: `all(type(n) is int for n in result)`; sala con file prenotate diverse.
7. R7: `build_hall(0, 5) == []`; `build_hall(3, 0) == [[], [], []]` e dopo `add_seat(hall, 1)` le altre due restano vuote.
8. R8: `pytest.raises(ValueError, match="rows")` per `build_hall(-1, 2)`; `match="seats_per_row"` per `build_hall(2, -1)`.
9. R9: valore di ritorno `None` di `add_seat` e `close_row`; due chiamate a `build_hall` non condividono file (`build_hall(2,2)[0] is not build_hall(2,2)[0]`, ma soprattutto modificare l'una non cambia l'altra).
10. Correzione robusta: indipendenza dopo una sequenza mista (book, add, close, book) confrontata con un modello ricostruito a mano.

## Casi limite che ho in mente (elenco completo)
- Dimensione zero: file zero; posti zero con file multiple (l'aliasing resta anche con liste vuote: `add_seat` fa crescere tutte).
- Dimensione negativa: `rows` e `seats_per_row`, messaggio con il nome. Nel codice originale non solleva (`range(-1)` vuoto, `[FREE] * -1` vuoto).
- `rows=1`: il difetto non si vede; unico caso in cui i test base passano sul codice originale.
- `add_seat` su `build_hall(n, 0)` (liste vuote condivise).
- Sequenza `close_row` poi `book_seat` su un'altra fila: sul codice originale nascosto dal fatto che la fila chiusa è uscita dal gruppo.
- Sala usata dopo `close_row`: R5 dice la fila resta della stessa lunghezza (anche se 0).
- `book_seat` su posto già `"taken"` o su `"closed"`: la consegna non lo dice. Chi lo nota in design sezione 2 ("la consegna non lo dice") guadagna; non c'è test nascosto e qualunque comportamento dichiarato è accettabile.
- Indici fuori dai limiti (`hall[5]`): `IndexError` naturale, non specificato. Indici negativi: Python accetta; non specificato.
- Tipi non int (`build_hall(2.0, 3)`, `True`): `TypeError` da `range`; `True` vale 1. Non specificato; non penalizzare.
- Grandi volumi: `build_hall(10**6, 10)` regge ma costa memoria: nessun test.
- Stesso oggetto tra chiamate diverse (R9): una costante a livello modulo con la riga di partenza sarebbe un secondo aliasing; verificare che la correzione non l'abbia introdotto.

## Trappole di design tipiche
1. **Correggere il sintomo.** Riscrivere `add_seat` con `hall[row] = hall[row] + [FREE]` rende verde il test di `add_seat` ma lascia `book_seat` rotto: la sezione D esiste per farlo vedere. Chi riscrive solo `add_seat` e dichiara "ho finito" non ha capito.
2. **Correggere in `book_seat`/`add_seat` con copie difensive** (`hall[row] = list(hall[row])` prima di modificare): funziona per le operazioni ma lascia la sala corrotta (R2: sotto `is` le file restano condivise).
3. **`[[FREE] * n] * rows`**: stesso difetto in un'altra veste. Controllare che non sia stato riscritto così.
4. **`copy.deepcopy(free_row)` per ogni file**: corretto ma pesante; ammesso se la scelta (sezione E) lo motiva, preferibile una lista nuova per giro.
5. **Cambiare le firme o i test base** per farli passare: il test di interfaccia lo rileva solo per le firme.
6. **Attribuire tutti i rossi a una sola causa**: `free_per_row` è un difetto diverso. Sezione A: se `test_free_per_row_counts_free_seats` finisce nello stesso gruppo degli altri, la causa è sbagliata (E001, P01).
7. **Esperimento che non può fallire** (P02): es. `print(hall[0] is hall[1])` con "Se ho torto: True"; cercare output uguali nelle due righe (il test lo blocca) e output che il modello rivale non produrrebbe mai.
8. **Spiegazione per tipo**: "le liste sono mutabili quindi si condividono". Non spiega perché `close_row` non mostra il difetto. La sezione B ("dopo:") e il confronto lo mettono alla prova.
9. **Sezione F con citazione non pertinente**: la citazione è letterale (il test lo impone) ma può essere la frase sbagliata. Controllare che parli della riga con il difetto e che "reggeva" sia onesto (confrontare con design sezione 1).
10. **Output ottenuto uguale alle righe previste in modo sospetto** (P03 sezione "riscritto a mano"): il test controlla la coerenza tra campi, non l'origine. Se l'output sembra scritto a mano, chiedere di rilanciare.
11. **Stima dei test nascosti**: confrontare con il numero reale; la regola di coerenza è già nel test.

## Cosa distingue una soluzione buona da una eccellente
- **Buona:** ogni file costruito con una lista nuova; test base verdi; `free_per_row` corretto; R7 e R8 rispettate; regressione che fallisce prima e passa dopo; esperimento D con due esiti diversi e output coerente; "chi guarda cosa" corretto nella sezione 1 (tre posizioni, una lista).
- **Eccellente:** la sezione 1 è giusta prima di eseguire e la 3 la usa (prevede esattamente i due test dell'aliasing rossi, `close_row` verde); la sezione B spiega che `close_row` esce dal gruppo condiviso e gli altri due no; la sezione C testa una sequenza che nessun base usa e include una verifica con `is`; la sezione D conclude che il difetto è in `build_hall` e non in `add_seat`; la validazione è in un solo punto con il nome dell'argomento nel messaggio; la regola finale distingue "indice a sinistra con `=`" (sposta la posizione) da "indice a sinistra con `+=` su un oggetto che si modifica sul posto"; stima dei test nascosti corretta; zero parole "tipo mutabile" come causa. Nomi in inglese e per ruolo in test, esperimenti e codice.

## Cosa verificare dove la precondizione di 002 non è stata chiusa
Sezione D (e K se fatta): Nick deve prevedere con due esiti che `hall[row] = hall[row] + [FREE]` rende verde il test di `add_seat` senza correggere `book_seat`. Se sbaglia la previsione o conclude "basta cambiare add_seat", E005 resta aperto; se spiega che `+=` modifica la lista condivisa e `= ... +` ne crea una nuova per quella posizione, E005 (ambito indice a sinistra) è superato per le liste. Sulle stringhe (`names[0] += "*"`, K) c'è l'altra metà (nuovo oggetto, posizione spostata, alias invariato); se K è tagliata, E005 resta parzialmente aperto per le stringhe: da chiedere in 004.
