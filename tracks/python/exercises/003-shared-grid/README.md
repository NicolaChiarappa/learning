# 003 — La griglia condivisa
Modulo: M01 (Nomi, oggetti, riferimenti) | Difficoltà: 3 | Tempo stimato: 90 minuti di lavoro (punti di controllo a 40 e 70 minuti, consegna a 100 in ogni caso)
Tipo: nuovo. Riprende dentro il lavoro normale E004 e E005 di `profile/errors.md` (`contenitore[i] = ...` contro `contenitore[i] += ...`, sezione D) ed E006 (sezione G), e riconferma E003.

Primo esercizio di M01 in cui lavori su codice: trovare un difetto, spiegarlo, correggerlo e dimostrare la correzione. Niente snippet da prevedere.

**Cosa copre del criterio di uscita di M01:** la parte "corregge un aliasing in codice non suo spiegando il meccanismo" (prima prova). Restano: 10 snippet nuovi con almeno 8 giusti senza REPL, e il default mutabile (esercizio 4).

**Sul tempo.** Dati tuoi: 001 76 minuti di sole previsioni, 002 132 minuti contro 60 stimati. La stima di 90 minuti tiene già conto del tuo ritmo, ed è lavoro, ambiente escluso. Nelle ultime due consegne il tempo è finito prima del confronto: qui la regola di taglio è scritta sotto e decide cosa si toglie.

## Teoria essenziale

**La domanda, riga per riga** (richiamo da 001-002): questa riga sposta un'etichetta o modifica un oggetto? E dopo, chi altro guarda quell'oggetto? Un'assegnazione non copia mai: crea o sposta un'etichetta, e l'oggetto resta uno solo. La domanda decide dove c'è un indice a sinistra (`x[i] = ...`, `x[i] += ...`) e dove un contenitore ne contiene un altro. Una lista, qui, ha **posizioni**: `hall[0]`, `hall[1]`, ... ciascuna guarda un oggetto, come un nome.

Esempio minimo (non è il difetto che cerchi):
```python
tags_a = ["red"]
catalog = [tags_a, ["blue"]]
catalog[1] = ["green"]          # index on the left of "=": acts on a position of catalog
print(tags_a, catalog)          # ['red'] [['red'], ['green']]
```

**`+=` con un indice a sinistra.** `x[i] += y` e `x[i] = x[i] + y` sono la stessa riga? Non darlo per scontato, e non prenderlo dal README di nessuno: è l'esperimento della sezione D. Language Reference, "Augmented assignment statements", dopo.

**Come Python mostra un valore (`str` contro `repr`).** `print` di una stringa da sola scrive il testo; un contenitore mostra i suoi elementi con la loro rappresentazione, che per una stringa ha gli apici.
```python
print("ab")        # ab
print(["ab"])      # ['ab']
```
pytest mostra sempre la rappresentazione. Come leggere un test fallito: la riga `E  assert <valore restituito dalla funzione> == <valore atteso dal test>`; sotto, `At index N diff: ...` dice il primo punto in cui differiscono. Documentazione: pytest, "How to write and report assertions in tests".

Dopo la correzione (non prima): Python Programming FAQ, "How do I create a multidimensional list?"; Language Reference, "Data model", sezione "Objects, values and types".

## Il problema

Hai ereditato `seating.py`, la mappa dei posti di una piccola sala (una sala è una lista di file, una fila è una lista di posti: `"free"`, `"taken"` o `"closed"`). Nella demo con una fila funziona. In produzione il team dice che "la mappa si comporta in modo strano dopo alcune operazioni" e che "il conteggio dei posti liberi non quadra". Non c'è altro. Il tuo lavoro:

1. riprodurre il problema con un test tuo;
2. spiegare quale riga lo causa e **quali posizioni di `hall` guardano quale lista**;
3. correggerlo cambiando il minimo;
4. dimostrare che la correzione regge.

**Le regole della funzione corretta** (spuntale a fine lavoro, sezione I di `risposte.md`):
- **R1** `build_hall(rows, seats_per_row)` restituisce una lista di `rows` file, ciascuna con `seats_per_row` posti, tutti `"free"`.
- **R2** Le file sono indipendenti: cambiare un posto o la lunghezza di una fila non cambia mai nessun'altra fila, subito dopo `build_hall` e dopo qualunque sequenza di operazioni.
- **R3** `book_seat(hall, row, seat)` mette quel posto a `"taken"` e non cambia nient'altro.
- **R4** `add_seat(hall, row)` aggiunge un posto `"free"` in fondo a quella fila e a nessun'altra.
- **R5** `close_row(hall, row)` mette tutti i posti di quella fila a `"closed"`, la fila resta della stessa lunghezza, le altre file non cambiano.
- **R6** `free_per_row(hall)` restituisce una lista di **int**, uno per fila, con il numero di posti `"free"`.
- **R7** Le dimensioni zero sono valide: `build_hall(0, n)` è `[]`; `build_hall(n, 0)` sono `n` file vuote, indipendenti.
- **R8** Una dimensione negativa solleva `ValueError`, con un messaggio che contiene il nome dell'argomento sbagliato (`rows` o `seats_per_row`).
- **R9** `book_seat`, `add_seat`, `close_row` modificano la sala ricevuta e restituiscono `None`; ogni chiamata a `build_hall` restituisce una sala nuova, senza niente in comune con le altre.

I test base **non coprono tutte** queste regole: coprono i casi normali e un caso limite ovvio. Quali restano scoperte lo scrivi tu nella sezione I.

## Vincoli
- Nomi, codice e commenti di prova in inglese e **per ruolo, non per tipo**. Le spiegazioni in italiano.
- Non cambiare firme, nomi delle funzioni, `test_seating.py` e `original/` (copia del codice di partenza: serve a citare le righe e a confrontare). Cambia `seating.py` il minimo necessario.
- Niente REPL, niente pythontutor, niente esecuzione prima di aver chiuso le sezioni 1-3 di `design.md`. Nella sezione 4 si esegue solo dopo aver scritto le due righe "Se ho ragione" e "Se ho torto".
- **Ogni esperimento ha due esiti scritti prima di eseguire**: "Se ho ragione: `<output esatto>`" e "Se ho torto: `<output esatto, diverso>`". Poi esegui, incolli l'output dal terminale e dici quale dei due è uscito. Se non riesci a scrivere la seconda riga, o se le due righe sono uguali, l'esperimento non verifica niente: cambialo.
- Gli output si incollano dal terminale, mai riscritti a mano. Forma esatta (apici singoli, `True`/`False`) richiesta ovunque.

## Ordine di lavoro
1. **Teoria** (5 minuti).
2. **Leggi** `seating.py`, `test_seating.py` e le regole. Non eseguire niente.
3. **Compila `design.md`**, sezioni 1-3 e sezione 4 fino a "Se ho torto". Lancia `pytest -q test_delivery.py -k gate`: deve passare prima del passo 4.
4. **Esegui** i test base (sezione A di `risposte.md`) e l'esperimento di `design.md` (compila "Output ottenuto" e "È uscito").
5. **Sezione B**: per le tre righe con indice a sinistra, chi guarda cosa dopo.
6. **Sezione C**: scrivi `test_regression.py`, fallo fallire sul codice originale, incolla l'output.
7. **Sezione D**: l'esperimento `+=` contro `=`.
8. **Sezione E e correzione** di `seating.py`: il difetto, `free_per_row`, R7, R8.
9. **Sezioni G, H, F, I, J**, poi K se hai tempo.
10. **Controllo di completezza** e consegna (vedi sotto).

## Punti di controllo e regola di taglio
- **A 40 minuti:** `design.md` chiuso fino a "Se ho torto" con `-k gate` verde, test base lanciati e sezione A incollata. Scrivi ora e una riga nel campo "Punto di controllo" di `risposte.md`. Se a 40 minuti la sezione 1 non c'è, scrivi la tua ipotesi migliore (un "non so" senza ipotesi non conta) e vai avanti.
- **A 70 minuti:** `test_seating.py` e `test_regression.py` verdi, anche se mancano campi.
- **A 100 minuti:** consegna comunque. Tentativo minimo: se ti blocchi per 20 minuti su un punto, compila "Nota di blocco" (punto esatto, cosa hai provato, ipotesi) e consegna: è valida e viene valutata.
- **Si può tagliare, in quest'ordine:** (1) la sezione K (scrivi "tagliata"); (2) R8: se non la implementi, scrivi `rispetto: no` in sezione I (taglio onesto, la stima dei test nascosti ne tiene conto); (3) test di regressione oltre il primo.
- **Non si taglia mai:** l'output di pytest incollato, l'esperimento D con le due righe scritte prima, la sezione F, la sezione I. Se serve velocità, si fanno meno cose, non si verificano meno cose.

## Perché ogni campo c'è
Ogni campo ha una ragione. Se uno ti sembra inutile, contestalo per iscritto con un argomento (in 001 due obiezioni fondate hanno cambiato il formato); i campi senza argomento restano.

| Campo | Perché |
|---|---|
| Ora di inizio, punto di controllo, ora di fine, minuti su ambiente | In 002 il tempo di lavoro e quello di ambiente erano mescolati. I minuti di lavoro non li chiedo: li calcola chi legge. |
| design 1, Posizioni e liste | Il difetto è una domanda su chi guarda cosa: va risposta prima di eseguire, e leggendo, non provando. |
| design 2, Casi limite dalla consegna | I test base non sono la specifica (test d'ingresso: "test verdi = finito"). Le regole sono qui sopra: i casi al limite li ricavi da quelle. |
| design 3, Test che prevedo rossi | Misura il tuo schema contro il codice. Poi lo confronti con la realtà (sezione A) e F ti chiede se reggeva. |
| design 4, due ipotesi e due esiti | Un esperimento che non può smentirti non verifica niente (002, snippet 5). L'ipotesi rivale ti obbliga a pensare a un'altra causa. |
| A, output; previsioni sbagliate; cause raggruppate | L'output è la base di tutto; lo scarto tra previsione e realtà è la calibrazione; non tutti i test rossi devono avere la stessa causa. |
| B, tre righe e confronto | Il "dopo" serve dove c'è un indice a sinistra: lì decide l'effetto. Non lo chiedo sulle altre righe. |
| C, test di regressione | Un difetto è riprodotto quando un test tuo fallisce per quella causa; e dopo la correzione è la prova. |
| D, esperimento `+=` contro `=` | È il punto che in 002 è rimasto aperto (`snapshot["name"] += "!"`). Qui ha conseguenze sulla correzione. |
| E, scelta con alternativa | Metodo della roadmap: una scelta motivata con l'alternativa scartata per esercizio. |
| F, cosa avevo scritto | La nota di design serve se la rileggi quando arrivi alla riga (in 002 l'ipotesi giusta era scritta e non è stata usata). La citazione deve essere letterale: non si può citare senza rileggere. |
| G, leggere un test fallito | Da M02 ogni fallimento ti mostra `'3'` contro `3`; leggerlo è una competenza (E006). |
| H, output finale | "Finito" vale solo con l'output incollato. |
| I, regole e stima | Spuntare le regole contrasta "test verdi = finito"; la stima dei test nascosti misura la calibrazione, e deve essere coerente con i tuoi stessi "no" e "non so". |
| J, regola | La sintesi è una domanda da portare nel prossimo esercizio, con cosa concludi per ogni risposta. |
| Test lasciati rossi | Puoi lasciare un test rosso se dici perché. Senza motivazione è un campo saltato. |

## Prima di scrivere codice
Compila `design.md`, sezioni 1-4 fino a "Se ho torto". Non iniziare a modificare `seating.py` senza.

## Come lanciare i test
```bash
cd /Users/nicolachiarappa/Desktop/Projects/learning/tracks/python/exercises/003-shared-grid
PY=/Users/nicolachiarappa/Desktop/Projects/learning/.venv/bin/python
$PY -m pytest -q test_delivery.py -k gate                    # cancello di design.md
$PY -m pytest -q test_seating.py                             # test base del codice
$PY -m pytest -q test_seating.py test_regression.py          # dopo la correzione
$PY -m pytest -q test_delivery.py                            # controllo di completezza
```
All'inizio i test di `test_seating.py` mostrano alcuni rossi: è il punto dell'esercizio. I test di `test_delivery.py` non giudicano se le risposte sono giuste: controllano che la consegna sia completa e coerente (campi pieni, due esiti diversi per ogni esperimento, output incollato coerente con quanto dichiari, regole spuntate, numeri compatibili).

## Consegna
1. Lancia `pytest -q test_delivery.py` **dal terminale** e incolla l'output all'orchestratore insieme alla frase "consegno 003". **Senza quell'output la review non parte.**
2. Un test può restare rosso solo con una riga in fondo a `risposte.md`: "lo lascio rosso perché ...".
3. L'orchestratore non compila, non confronta e non corregge nessun campo al posto tuo.
