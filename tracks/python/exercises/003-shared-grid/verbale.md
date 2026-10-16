# Verbale — 003 La griglia condivisa

Scritto dall'orchestratore il 2026-10-16. Lavoro svolto tra il 2026-10-15 e il 2026-10-16 (sessione aperta il 2026-10-12).

## Stato alla consegna
- `pytest -q` lanciato da Nick dalla cartella dell'esercizio: `13 passed` (8 di `test_seating.py`, 5 di `test_regression.py`).
- Modifiche a `seating.py`: `build_hall` (ciclo con `append` di una lista nuova per fila), `close_row` (assegnazione per indice di ogni posto invece di riassegnare la fila), `free_per_row` (tolto `str`). `add_seat` non toccata.
- **Mancano** (Nick ha consegnato senza completarli, nonostante tre richieste):
  - output del rosso di `test_regression.py` su `original/seating_original.py`. Nick dice di averlo lanciato e che "sono tutti rossi", ma non ha incollato l'output. Non l'ho verificato al suo posto. Previsione test per test chiesta prima del lancio: non scritta.
  - stima numerica dei test nascosti su 10: in "Dopo" scrive "mi aspetto di fallire tutti i test che riguardano [i casi limite], il resto credo di superarli".
  - regola che si porta via.
- Prove su `build_hall` e `close_row` fatte senza documentarle: ricostruite a posteriori in "Prove ricostruite dopo" (segnalato in testa alla sezione).

## Chiacchierata finale
Domande poste in chat, risposte senza eseguire codice (dichiarato da Nick).

**D1.** Nell'esperimento del dubbio 2 `correct_close_row` (`for seat in hall[row]: seat = "close"`) seguita da `hall[2] != third_row` → `False`, e la frase "ora `hall[2]` contiene tutte stringhe close". Cosa dimostrava quell'esperimento, e con quale output ti avrebbe dato torto?
> "ho testato male la funzione, incorrect close modifica effettivamente i valori mentre correct_close li lascia intatti è per questo che torna false, sarebbe stato meglio testare con is o con l'id, in ogni caso la mia correct_close non funziona dovrei correggerla come ho fatto nella prova1."

Nota: la prima formulazione della domanda (prima che compilasse la prova 1) chiedeva cosa contenesse `hall[row]` dopo il ciclo. Nick ha risposto compilando la prova 1 in `appunti.md` ("seat non punta più all'oggetto della lista, ho solo spostato il label"). La domanda è nata da un mio intervento precedente (vedi Indizi).

**D2.** `add_seat`: `hall[row] += [FREE]` sposta una posizione di `hall` o modifica un oggetto? Sul codice originale cosa succede alle altre file dopo `add_seat(hall, 0)`?
> "hall[row] += [FREE] modifica la lista stessa, aggiugne una nuova stringa, nel codice originale toccava l'unica lista istanziata e quindi la modifica si vedeva su tutti gli elementi di hall."

Non dice nulla sulla posizione `hall[row]` (se viene anche riassegnata).

**D3.** Prova 5: quante volte viene eseguito `list(free_row)` in `[list(free_row)] * 2`? Nell'originale `[free_row for _ in range(rows)]`, quante liste nuove vengono create?
> "in quella riga una sola volta viene eseguito, nel codice originale viene creata una sola lista nuova"

**D4.** Scrivi un `build_hall` sbagliato che violi R9 e passi `test_two_hall_are_independent`.
- Nick ha chiesto prima se "nessuna cosa in comune" significasse contenuto diverso o liste interne non condivise. **Chiarimento della consegna dato dall'orchestratore** (non contato come indizio): R9 riguarda gli oggetti, non i valori; due sale nuove sono uguali nel contenuto.
- Prima risposta: `hall_obj` globale con `append` a ogni chiamata. **Si è corretto da solo** con una seconda versione: lista vuota a livello di modulo (`default_last_row`) aggiunta in fondo a ogni sala.
- Ha proposto un test più forte (unione degli `id` delle file delle due sale). Prima versione con `SyntaxError` (set comprehension con due `for` separati da virgola); corretta da lui con `ids1.union(ids2)`. Lanciato contro `incorrect_build_hall`: rosso `assert 7 == (4 + 4)`, output mostrato da me in chat (non incollato da lui in `appunti.md`; lì c'è il codice della funzione e del test).
- Durante questo passaggio aveva messo `incorrect_build_hall` in `seating.py` e fatto chiamare al test la funzione sbagliata; su mia segnalazione ha rimesso `build_hall` e tolto la funzione sbagliata (un `ImportError` residuo l'ha letto e risolto lui).

## Indizi e aiuti sul contenuto
- **Livello 1** (1): domanda sull'esperimento di `correct_close_row` ("quale output ti avrebbe smentito? cosa contiene `hall[2]`?"). Da lì ha compilato la prova 1.
- **Livello 1** (1): "il test controlla l'identità delle file: copre tutta R2? '…e dopo qualunque sequenza di operazioni'". Dopo, `test_all_lists_independent` include `book_seat`, `add_seat`, `close_row`, `free_per_row`.
- Domande socratiche senza contenuto nuovo: tre domande per passare dal difetto all'`assert`; promemoria che in "Durante" aveva già scritto che `free_per_row` restituisce stringhe ("è un secondo bug?"); criterio bug/scelta per `close_row` ("viola una regola R1-R9?").
- Teoria (non indizio): cos'è un test pytest (esempio su `slugify`, dominio diverso), cos'è un test di regressione (rosso sull'originale, verde sul corretto), come importare `original.seating_original`; tre modi di testare originale e corretto (import da scambiare, test separato, `parametrize` + `xfail`), consigliato il primo.
- Forma segnalata e poi corretta da lui: `from seating import *`, nome `test_r2`, docstring in italiano.

## Tempi
Non misurati con precisione. Lavoro su due giorni (2026-10-15 pomeriggio, 2026-10-16 mattina; ultimo salvataggio di `appunti.md` alle 12:23).
Tempo di ambiente consistente, separato dal lavoro: rimappatura del backtick (Karabiner, poi Ukelele: layout salvato in `/Library/Keyboard Layouts/ita.bundle`), Local History di PyCharm per ricostruire le prove, live template/macro di PyCharm, come lanciare pytest (una volta dalla radice del repo, con errori di raccolta di 001/002).

## Cosa ha sistemato l'orchestratore nella forma
- Ha riformattato in `appunti.md` le cinque prove incollate in chat da Nick (blocchi di codice, indentazione, etichetta della funzione dedotta), sotto "Prove ricostruite dopo" con la nota che non erano previsioni scritte prima. Le righe "Cosa mi aspettavo / uscito / ne ricavo" le ha compilate Nick.
- Nient'altro nei file di Nick.
