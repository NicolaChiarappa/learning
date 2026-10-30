# Note del designer — 006 (per il reviewer, Nick non le apre)

## Cosa allena
- Unica difficolta`: contratto di proprieta` dei dati. Tre mosse: leggere la docstring come specifica (E009), distinguere livello esterno e interno di una copia (E004), scegliere e dichiarare per `merge_plans` (decisione di design con alternativa reale: costo contro isolamento).
- Ripassi dentro il lavoro: E001/E004 (test 7 verde e` la trappola: `dict(plan)` fa un oggetto nuovo ma `meals` e` condiviso; `+=` con indice a sinistra, esperimento A), E003 (`list(meals)` copia la lista ma non i dict; `[] ` esplicito), E009 (parole "any sequence", "dict inside", "dict included": nessun test base le verifica; R6 chiede la riga di verifica), E005 (esp. A, ormai risolto: riconferma).
- Processo: cancello su 8 test base (rosso/verde con motivo prima di pytest), frase "Secondo me, dopo new_plan(...)" da riprendere in "Dopo". Tempo atteso: 60 minuti; il punto di controllo a 40.

## Casi limite che ho in mente
1. `new_plan` con tupla; poi `add_meal` (con `meals` tenuta cosi` com'e` fallisce con AttributeError).
2. `new_plan` con lista vuota esplicita: il piano non deve guardare la lista del chiamante.
3. Dict interni mutati dal chiamante dopo la chiamata (copia superficiale non basta).
4. Lo stesso dict due volte nell'ingresso (`[d, d]`): con `deepcopy` unico resta un oggetto condiviso fra le due posizioni dentro il piano (memo): accettabile, il piano possiede i suoi.
5. `with_meal` su piano vuoto; su piano costruito da tupla; scrittura dal risultato verso l'originale e viceversa.
6. `with_meal` correzione "pezza" (`= ... + [...]`): livello lista a posto, dict interni ancora condivisi.
7. `merge_plans(p, p, "x")`: stesso piano due volte. Con condivisione dei dict, lo stesso dict compare in due posizioni del risultato e una modifica si vede in entrambe, e anche nell'ingresso. Con `copy.deepcopy((first["meals"], second["meals"]))` in una sola chiamata il memo mantiene l'identita` interna: due posizioni = un dict, anche se separato dall'ingresso. Con due `deepcopy` separati, due dict. Tutte e tre dichiarabili; l'unica inaccettabile e` quella non dichiarata o dichiarata a rovescio.
8. `merge_plans` con ingressi vuoti o con owner uguale a uno degli ingressi.
9. Non specificati, nessun test: `kcal` negativo o non int, nomi duplicati, `meals` come generatore (non e` una sequenza: `list(meals)` lo accetta; va bene), `owner` vuoto, thread-safety.
10. Valore di `plan` mutato tra due `with_meal` consecutive: la catena `with_meal(with_meal(p, ...), ...)` non deve toccare `p`.

## Trappole di design tipiche
1. `new_plan`: `list(meals)` e basta (livello esterno): test base verdi, nascosti sui dict rossi.
2. `meals = meals or []` o `if not meals`: per `[]` esplicito crea una lista nuova per caso; pericoloso solo se letto come "il contratto e` quello", chiedere in chiacchierata perche`.
3. `type(meals) is list` o `isinstance(meals, list)` per "essere sicuro": restringe "any sequence" (E009).
4. `with_meal`: `copy.copy(plan)` o `dict(plan)` seguito da `+=` (invariato) o da `= ... + [...]` (pezza).
5. `deepcopy` ovunque senza motivo e senza dirlo: giusto, ma E004 non e` chiuso se non sa dire cosa avrebbe fatto `list()`. Chiedere.
6. `merge_plans`: scrivere la docstring a posteriori adattandola al codice (e` ok) o senza la frase sulla proprieta` (R5 mancato); test_ownership che prova l'opposto di cio` che la docstring dice, o che usa `==` al posto di `is` (E007).
7. Test di R5 che non usa `merge_plans(p, p, ...)` anche se richiesto.

## Buona contro eccellente
- Buona: base verdi, tutti gli esercizi sistemati, docstring di `merge_plans` con una frase di proprieta`, test con `is`/modifica che la dimostra, R6 compilata.
- Eccellente: prevede 4 rossi/4 verdi con le ragioni giuste (test 7 verde per "dict nuovo, lista condivisa"); nota che `+=` con indice a sinistra modifica in place e anche riassegna; B previsto giusto (`plan["meals"][0]["kcal"]` = 99 con `list()`, `is` False); sceglie `merge_plans` motivando con un'alternativa vera (condivido = O(1), pericoloso se un ingresso e` un piano vivo; copio = isolamento, costo); individua da solo il caso `merge_plans(p, p)`; in "Dopo" riprende la frase iniziale con una risposta onesta.
- Cosa guardare nella consegna: la riga R6 per `new_plan` cita "any sequence" o "dict inside"? Se cita solo il test base, E009 si ripete.

## Per il reviewer
Test nascosti: 20, vedi chiave. Nessun requisito aggiunto da qui. Un eventuale requisito nuovo del reviewer deve indicare quale ne toglie (limite 60 minuti).
