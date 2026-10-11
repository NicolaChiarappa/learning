# Note del designer — 003 (per il reviewer e l'orchestratore, Nick non le apre)

Formato leggero (CLAUDE.md, dal 2026-10-12). La chiave con gli esiti attesi è in `chiave.md`. `pytest.ini` raccoglie solo `test_seating.py` e `test_regression.py`: i test nascosti si lanciano con il file esplicito (`pytest -q test_hidden.py`).

## Perimetro rispetto alla versione a campi
- Tolti: design.md, risposte.md, test_delivery.py, sezione K (estensione stringhe), punti di controllo e cancelli.
- R8 (negativi) resta numerata ma facoltativa. Se non la implementa, il test nascosto 8 è rosso per scelta: non penalizzare, tenerne conto nella calibrazione ("su 10", con 9 attesi se salta R8).
- Tenuto `free_per_row` con `str(...)`: costa una riga di correzione e porta E006 senza campi aggiuntivi.
- E005 sulle stringhe (`names[0] += "*"`) non è più coperto: da chiedere in 004 se E005 resta aperto.

## Cosa allena (emerge da codice, test e chiacchierata, non da campi)
- E001/E003: chi guarda quale lista dopo la costruzione (tre posizioni, una lista).
- E004/E005 (ambito `contenitore[chiave] += ...`): `hall[row] += [FREE]` modifica sul posto la lista guardata; `hall[row] = hall[row] + [FREE]` crea una lista nuova e sposta la posizione. `close_row` verde perché usa `=`.
- E006: `assert ['3', '3'] == [3, 3]` letto correttamente.
- P02 (esperimenti con esito alternativo diverso scritto prima), P04 (stima dei test nascosti), P07 (casi limite dalle regole).

## Il difetto
`build_hall` crea una sola `free_row` e la mette in tutte le posizioni: `hall[0] is hall[1] is hall[2]`. La lista è creata prima della comprehension, che sembra costruire file nuove a ogni giro.

## Test base
Verdi (5): forma, zero file, una fila, `close_row`, `book_seat` che restituisce `None`. Rossi (3): `test_book_seat_changes_only_that_seat`, `test_add_seat_grows_only_that_row` (aliasing), `test_free_per_row_counts_free_seats` (stringhe, causa diversa: verificare che non finiscano nello stesso gruppo).

## Test nascosti suggeriti (10)
1. R1 forma `build_hall(3, 4)`. 2. R2 nessuna coppia di file con `is` uguale. 3. R2/R3 `book_seat` su file diverse in sequenza. 4. R4 `add_seat` su file diverse, lunghezze `[3, 2, 3]`. 5. R5 `close_row` poi `add_seat` su fila chiusa e su un'altra. 6. R6 `type(n) is int` per tutti. 7. R7 `build_hall(0, 5) == []`, `build_hall(3, 0) == [[], [], []]` e `add_seat` su una sola fila. 8. R8 `pytest.raises(ValueError, match="rows")` / `match="seats_per_row"` (facoltativo). 9. R9 `None` di ritorno e due `build_hall` indipendenti. 10. Sequenza mista (book, add, close, book) contro un modello costruito a mano.

## Casi limite che ho in mente
- Zero file; zero posti con più file (l'aliasing resta con liste vuote: `add_seat` fa crescere tutte).
- Negativi: nel codice originale non sollevano (`range(-1)` vuoto, `[FREE] * -1` vuoto).
- `rows=1`: il difetto non si vede.
- `close_row` poi `book_seat` su un'altra fila: difetto nascosto perché la fila chiusa è uscita dal gruppo.
- Fila chiusa di lunghezza 0 resta di lunghezza 0.
- `book_seat` su posto già `taken`/`closed`, indici fuori limiti o negativi, tipi non int: non specificati, nessun test; chi li nota guadagna.
- Costante a livello modulo con la riga di partenza: secondo aliasing (R9).

## Trappole di design tipiche
1. Correggere il sintomo: `add_seat` con `hall[row] = hall[row] + [FREE]` rende verde un test e lascia `book_seat` rotto (chi lo fa e non lo nota non ha il modello).
2. Copie difensive in `book_seat`/`add_seat` (`hall[row] = list(hall[row])`): le operazioni funzionano, la sala resta con file condivise (R2).
3. `[[FREE] * n] * rows`: lo stesso difetto riscritto.
4. `deepcopy(free_row)` per ogni fila: corretto ma pesante; ammesso se motivato.
5. Cambiare firme o test base.
6. Attribuire tutti i rossi alla stessa causa (`free_per_row` è indipendente).
7. Esperimento che non può fallire (esito alternativo identico o impossibile).
8. Spiegazione per tipo ("le liste sono mutabili"): non spiega perché `close_row` non mostra il difetto.
9. Test di regressione che fallisce per la causa sbagliata (stringhe) o che passa sul codice originale.
10. Output incollato che sembra riscritto: chiedere di rilanciare.

## Buona contro eccellente
- Buona: una lista nuova per fila, creata dentro il giro; test base verdi; `free_per_row` corretto; R7 rispettata; regressione che fallisce prima e passa dopo; "chi guarda cosa" corretto.
- Eccellente: previsione giusta prima di eseguire, usata poi (rossi attesi esatti, `close_row` verde); spiega che `close_row` esce dal gruppo condiviso e gli altri due no; regressione con sequenza che nessun test base usa e verifica con `is`; conclude che il difetto è in `build_hall` e non in `add_seat`; regola finale che distingue `=` su una posizione (la sposta) da `+=` su un oggetto modificabile sul posto; stima dei nascosti corretta e coerente con le regole che ammette di non coprire; nomi in inglese e per ruolo.

## Domande per la chiacchierata finale (orchestratore, a voce; 3-4 su 6, scegliere sui punti deboli emersi)
1. Dopo `hall = build_hall(3, 2)` nel codice originale, quante liste esistono in tutto e chi guarda ciascuna? Disegnalo a parole.
   - Solida: due liste (esterna e una interna), le tre posizioni guardano la stessa; ragiona sulle posizioni, non sul tipo. A memoria: "le liste sono mutabili" o "sono riferimenti" senza contare gli oggetti; numero sbagliato di liste.
2. Nel codice originale `close_row` non mostrava il problema e `book_seat` sì. Cosa fa diversamente la prima riga della seconda?
   - Solida: distingue ciò che agisce sulla posizione della lista esterna da ciò che agisce sull'oggetto guardato, e dice cosa guarda `hall[row]` dopo. A memoria: "una crea una lista nuova" senza dire dove finisce la nuova e chi resta sulla vecchia; spiega con il tipo.
3. Se in `add_seat` scrivessi `hall[row] = hall[row] + [FREE]` invece di `+=` e lasciassi tutto il resto com'è, cosa cambierebbe nei test, e cosa resterebbe com'è? Perché?
   - Solida: prevede senza eseguire che `add_seat` diventa verde e `book_seat` no, e spiega con "lista nuova per quella posizione" e "la lista condivisa non viene toccata". A memoria: "sono equivalenti" o "`+=` è più veloce"; prevede tutto verde o tutto rosso senza motivo.
4. Perché dopo la tua correzione le file sono indipendenti? Cosa succede, riga per riga, quando `build_hall` costruisce la terza fila?
   - Solida: la costruzione della lista è dentro il giro, quindi un oggetto nuovo a ogni iterazione; sa dire cosa sarebbe cambiato spostandola fuori. A memoria: "perché ho copiato" o "perché ho usato la comprehension" senza dire quando la lista viene creata.
5. Leggi questa riga di pytest: `assert ['3', '3'] == [3, 3]` con `At index 0 diff: '3' != 3`. Cosa restituisce la funzione, cosa si aspetta il test, perché si vedono gli apici?
   - Solida: sinistra = valore restituito, lista di stringhe; destra = atteso, interi; gli apici sono la rappresentazione delle stringhe nei contenitori; la differenza è nel tipo, non nel valore stampato. A memoria: "è un problema di tipi" senza dire quale lato è quale, o dubbio su quale sia l'atteso.
6. Il tuo test di regressione: se lo lanciassi sul codice originale, per quale motivo esatto fallirebbe? Esisterebbe un modo di farlo fallire per un'altra causa?
   - Solida: indica la causa (file condivise) e vede che un test sulle stringhe fallirebbe per un'altra; sa che sequenza o `is` isola l'aliasing. A memoria: "fallisce perché il codice è sbagliato"; test che mescola le due cause.
