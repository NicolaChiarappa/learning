# Risposte — 003

Scrivi qui, direttamente in questo file, dall'inizio alla fine. Un campo vuoto o con solo il suggerimento tra `<!-- -->` fa fallire il controllo di completezza. Gli output si incollano dal terminale: mai riscritti a mano. Prima di compilare, leggi nel README la sezione "Perché ogni campo c'è".

Ora di inizio:
Punto di controllo (scrivi ora e una riga su dove sei quando arrivi a 40 minuti):
Ora di fine:
Minuti persi su ambiente (terminale, IDE, comandi: non contano come lavoro):

---

## A. I test base, prima di toccare il codice
**Output di `pytest -q test_seating.py`:**
```
```
<!-- Incolla l'output completo, lanciato sul codice originale. -->

**Previsioni di design.md sbagliate:**
<!-- Confronta i test che avevi previsto rossi (design.md, sezione 3) con quelli rossi qui sopra. Scrivi i nomi dei test dove la previsione era sbagliata, in un senso o nell'altro, oppure "nessuna". -->

**Cause dei test rossi, raggruppate:**
<!-- Una riga per gruppo: i test rossi che secondo te hanno la stessa causa (nomi), poi → la causa in una frase. Ogni test rosso deve comparire in un gruppo. -->

## B. Chi guarda cosa dopo ogni operazione
Codice originale, `hall = build_hall(3, 2)`. Solo le tre righe di `seating.py` con un indice a sinistra.

**Righe:**
<!-- Tre voci, una per riga, nella forma:
- `riga copiata dal codice` → sposta un'etichetta (quale posizione, verso quale oggetto) / modifica un oggetto (quale); dopo: quali posizioni di `hall` guardano quell'oggetto -->

**Confronto tra close_row e add_seat:**
<!-- Con le tre voci qui sopra: le righe di `close_row` e di `add_seat` si comportano allo stesso modo rispetto al difetto, o in modo diverso? Perché? Almeno 2-3 frasi. -->

## C. Il difetto riprodotto da un test mio
Crea `test_regression.py`: almeno un test con `assert` su valori esatti, che fallisca sul codice originale e che usi una sequenza di operazioni che nessun test base usa.

**Output prima della correzione:**
```
```
<!-- Incolla l'output di `pytest -q test_regression.py` lanciato prima di correggere. Deve mostrare il test rosso. -->

## D. Esperimento: `+=` o `=` su un elemento del contenitore
Sul codice originale. La domanda: se riscrivessi `add_seat` con `hall[row] = hall[row] + [FREE]` al posto di `hall[row] += [FREE]`, il test `test_add_seat_grows_only_that_row` diventerebbe verde? Sarebbe una correzione del difetto?

**Ipotesi:**
<!-- Una frase, con la tua risposta e perché. -->

**Codice:**
```python
```
<!-- Al massimo 8 righe, nomi in inglese e per ruolo. Non modifichi `seating.py`: riproduci le due righe nel REPL o in un file usa e getta. -->

**Se ho ragione:**
<!-- Output esatto. -->

**Se ho torto:**
<!-- Output esatto, diverso dal precedente. -->

**Output ottenuto:**
```
```

**È uscito:**
<!-- ragione / torto / nessuno dei due -->

**Cosa ne concludo per la correzione:**
<!-- Dove va fatta la correzione e cosa sbaglierebbe chi riscrivesse solo `add_seat`. 2-3 frasi. -->

## E. La correzione
Ora correggi `seating.py`: il difetto, `free_per_row` e le regole R7 e R8 se non le rispetta già. Non cambiare firme e nomi.

**Scelta:**
<!-- Come hai corretto, con la forma "ho fatto X invece di Y perché ...": almeno un'alternativa che hai considerato e scartato, e il motivo. -->

## F. Cosa avevo scritto in design.md
**Riga del codice originale con il difetto:**
<!-- Copia la riga tra apici inversi. -->

**Cosa avevo scritto in design.md su questa riga:**
<!-- Rileggi design.md e copia, parola per parola, la frase della sezione 1 (o della sezione 4) che riguarda questa riga. Non parafrasare. -->

**Reggeva:**
<!-- si / no -->

**Se no, cosa cambia nel mio modello:**
<!-- Se hai scritto "si", scrivi "nessun cambiamento". Se hai scritto "no": cosa pensavi, cosa hai scoperto, come lo applicherai alla prossima riga con un indice a sinistra. -->

## G. Leggere un test fallito
Dal tuo output della sezione A: il test `test_free_per_row_counts_free_seats`.

**Riga assert copiata da pytest:**
<!-- La riga che comincia con `E` e contiene `assert`, copiata tale e quale. -->

**Cosa confronta pytest e perché i due valori non sono uguali:**
<!-- A sinistra e a destra del `==`: che cosa c'è, e che differenza c'è tra i due. Con parole tue, almeno 2 frasi. -->

**Riga di seating.py che causa la differenza:**
<!-- Copia la riga tra apici inversi. -->

## H. Verifica finale
**Output di `pytest -q test_seating.py test_regression.py`:**
```
```
<!-- Incolla l'output dopo la correzione. -->

## I. Le regole della consegna
**Regole:**
- R1 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
- R2 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
- R3 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
- R4 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
- R5 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
- R6 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
- R7 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
- R8 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
- R9 → copertura: <nome test o nessuna> | rispetto: <si / no / non so>
<!-- Copertura: i nomi dei test (di test_seating.py o test_regression.py) che verificano la regola, separati da virgola, oppure "nessuna". Rispetto: la tua correzione rispetta la regola? Se non lo sai, "non so". -->

**Test nascosti che prevedo di passare:**
<!-- Un numero da 0 a 10. Il reviewer userà 10 test nascosti; ogni regola ne ha almeno uno. -->

## J. Sintesi
**Regola:**
<!-- Per la prossima volta che incontri una struttura dentro un'altra: una domanda da farti su una riga, e cosa concludi a seconda della risposta ("se ... allora ..."). -->

## K. Estensione facoltativa (si taglia per prima)
Dopo la correzione. Esperimento a due esiti sulla stessa idea della sezione D: con `hall = build_hall(2, 2)` corretta, dopo `before = hall[0]`, la riga `hall[0] += [FREE]` lascia `hall[0] is before` vero o falso? E con `hall[0] = hall[0] + [FREE]`? E se l'elemento è una stringa (`names = ["A", "B"]`, `alias = names[0]`, `names[0] += "*"`), `alias is names[0]`?

**Stato:**
<!-- fatta / tagliata. Se scrivi "tagliata" i campi sotto restano vuoti. -->

**Codice:**
```python
```

**Se ho ragione:**

**Se ho torto:**

**Output ottenuto:**
```
```

**È uscito:**

## Test lasciati rossi e perché
<!-- Scrivi "nessuno" oppure una riga per ogni test che consegni rosso: - nome_test → lo lascio rosso perché ... (almeno 20 caratteri di motivazione) -->

## Nota di blocco (solo se ti blocchi)
<!-- Facoltativa. Se dopo 20 minuti non vai avanti: il punto esatto, cosa hai provato, la tua ipotesi migliore. È una consegna valida. -->
