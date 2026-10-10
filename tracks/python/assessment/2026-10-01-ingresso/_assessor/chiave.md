# Chiave di valutazione — uso esclusivo dell'assessor (fase VALUTA)

Test preparato il 2026-10-01. Gli output degli snippet sono stati verificati con Python 3.14.
I test nascosti sono stati validati contro una soluzione di riferimento non salvata: 166/166 verdi; contro gli scheletri vuoti 165 falliscono.

Esecuzione in fase di valutazione (dalla cartella del test):
```
.venv/bin/pytest -q                 # test base (04-scrittura-codice)
.venv/bin/pytest -q _assessor -rA   # test nascosti
```

## Mappa domande/snippet/esercizi → aree

| Item | Aree |
|---|---|
| C1 | A1 |
| C2 | A2 |
| C3 | A4 |
| C4 | A3 |
| C5 | B1 |
| C6 | C1, C2 |
| C7 | B3 |
| C8 | C3 |
| C9 | D2 |
| C10 | D3, K3 |
| C11 | D1 |
| C12 | E1 |
| C13 | E2, E3 |
| C14 | G4 |
| C15 | G3 |
| C16 | D4 |
| C17 | D5 |
| C18 | F1, F2, F3 (parziale) |
| C19a | G5 |
| C19b | H3, H4 |
| C20 | I1, I3 (I2 solo se citato) |
| L01 | A2, D1 |
| L02 | A3, C1, A5, B2 |
| L03 | C1, K5, G2, G4 |
| L04 | D2, D3 |
| L05 | E1 |
| L06 | G3 |
| L07 | B3, B4 |
| L08 | K1, K2, G5, H4, K4, H3 |
| L09 | D4, D5, K6, K2 |
| L10 | I3 |
| S01 | A4, A5, G1, K4, K5 |
| S02 | C1, C2, K5 |
| S03 | B3, B4, H4, A3 |
| S04 | D1, D2, D3, D6, G4, E1, K3 |
| S05 | G2, G3, G4, E1, K2, K4, K5, nota di design |
| D1 | K2, K4, H4, D5, K6 |
| D2 | J1, K7, K2 |

Non coperte o coperte solo marginalmente: F3 e J2-J5 (J1 solo in D2). Segnarle come "non misurato" salvo evidenze indirette (per esempio J3: codice formattato in modo coerente; H1/H2: test propri `test_mine_*.py`, se presenti).

## Concetti: punti attesi (per un 3 servono quasi tutti; per un 4 anche il perché e i trade-off)

1. `None` è singleton; `==` chiama `__eq__` sovrascrivibile; `is` per singleton/sentinelle. Esempio errato: `is` su interi/stringhe (caching degli interi piccoli, interning).
2. `[[0,0,0]]*3` crea 3 riferimenti alla stessa lista → `[[1,0,0],[1,0,0],[1,0,0]]`. Corretto: comprehension.
3. list `in` O(n), set `in` O(1) medio, `pop(0)` O(n) (shift) → `deque`, `pop()` O(1). Hash serve per il bucket; se l'hash cambia, l'oggetto è "perso" (non ritrovabile, possibili duplicati).
4. `UnboundLocalError`: l'assegnazione rende `count` locale per tutta la funzione (decisione a compile time). Fix: `nonlocal` (preferibile) oppure stato mutabile/classe. `global` è sbagliato.
5. keyword-only: un flag booleano posizionale è illeggibile (`transfer(a, b, 10, True)`), permette di aggiungere parametri senza rompere. Positional-only: nomi dei parametri non sono API (si possono rinominare), evita conflitti con `**kwargs`, parametri senza un nome significativo.
6. Iterabile ha `__iter__` che restituisce un nuovo iteratore; iteratore ha `__next__` e `__iter__` che restituisce sé stesso; stato interno → si esaurisce. Pipeline: memoria costante, un elemento alla volta, composizione.
7. `wraps` copia `__name__`, `__doc__`, `__module__`, `__qualname__`, `__dict__`, imposta `__wrapped__`; senza: debug/log/traceback, introspezione (`inspect.signature`), framework che usano il nome (es. registrazione di URL/endpoint, pytest), doppio decoratore. Con argomenti: `retry(times=3)` viene chiamato e deve restituire il vero decoratore.
8. Raggruppa solo elementi **consecutivi** con la stessa chiave: bisogna ordinare prima. Progettato così perché è lazy/streaming e funziona su iteratori infiniti senza memoria; bonus: i gruppi condividono l'iteratore sottostante (vanno consumati prima di avanzare).
9. `a == b` ⇒ `hash(a) == hash(b)`. Solo `__eq__` → `__hash__ = None` → unhashable, perché l'hash ereditato basato sull'identità violerebbe il contratto.
10. Criteri: immutabilità e hashability (frozen, NamedTuple); validazione/comportamento (classe o dataclass con `__post_init__`); NamedTuple è anche tupla (unpacking, indicizzazione, uguaglianza con tuple: rischio); dict/TypedDict ai confini (JSON), nessuna validazione a runtime; slots/memoria.
11. Lettura: istanza poi classe. Assegnazione via `self.x =` crea un attributo di istanza (shadowing); mutazione via `self.x.append` modifica quello di classe. Property: attributi derivati economici, compatibilità API; male se fa I/O o calcoli pesanti o ha effetti collaterali (il chiamante si aspetta un accesso economico).
12. Si cattura dove si può fare qualcosa di sensato (recupero, traduzione al confine di livello, aggiunta di contesto); altrimenti si lascia propagare. Senza `from`: contesto implicito "During handling of the above exception another exception occurred" (`__context__`); `from e`: causa esplicita "The above exception was the direct cause" (`__cause__`); `from None`: sopprime il contesto (`__suppress_context__`), adatto quando il dettaglio interno non serve o lo nasconde.
13. Garantisce che `__exit__` venga chiamato all'uscita dal blocco (anche con eccezione, return, break); non garantisce nulla se `__enter__` fallisce o il processo muore (kill, os._exit). `__exit__` che ritorna True sopprime l'eccezione. Con contextmanager: `try: yield ... finally: cleanup`; senza `try`, se il blocco solleva un'eccezione il cleanup dopo `yield` non viene eseguito.
14. Rappresentazione binaria IEEE 754: 0.1 non è rappresentabile esattamente. `Decimal(0.1)` eredita l'errore del float; `Decimal("0.1")` è esatto. Importi: Decimal o interi in centesimi, arrotondamento esplicito, mai float, attenzione a JSON e al DB.
15. Naive = senza tzinfo, ambiguo; aware = istante preciso. UTC: nessuna ambiguità, confronti e ordinamenti corretti; conversione al locale solo in visualizzazione. Bug due volte l'anno: cambio dell'ora legale (job alle 02:30 saltato o doppio, durata di 23/25 h, `+ timedelta(hours=24)` vs giorno di calendario).
16. `super()` segue l'MRO dell'**istanza** (C, A, B, Base, object): in A chiama B, non Base. Questo permette catene cooperative in cui ogni classe chiama `super()` e `Base.__init__` viene chiamato una sola volta. Servono firme compatibili (`**kwargs`).
17. ABC: tipizzazione nominale (bisogna ereditare), controllo a istanziazione dei metodi astratti, si possono fornire implementazioni condivise. Protocol: strutturale (duck typing statico), senza ereditare; utile per tipi di terze parti e per disaccoppiare; `runtime_checkable` è limitato (controlla solo l'esistenza dei metodi).
18. Gli hints non sono controllati a runtime (salvo librerie come pydantic). `list` è invariante perché mutabile: si potrebbe inserire un `Cat` in una `list[Dog]` → errore del type checker. `Sequence` è covariante (sola lettura) e accetta anche le tuple: annotare il minimo necessario.
19a. `getLogger(__name__)`: gerarchia di logger, configurazione lasciata all'applicazione; `basicConfig` in una libreria impone la configurazione a chi la usa. Il formato `%s` viene risolto in modo lazy, solo se il record viene emesso; i record con lo stesso messaggio sono raggruppabili (Sentry); dà meno problemi con oggetti costosi da formattare.
19b. `from payments import charge` copia il riferimento in `orders`: va patchato `orders.charge`. Non mockare: il codice sotto test, le funzioni pure, i value object, le strutture dati; preferire fake o dependency injection ai patch; mockare solo i bordi (rete, tempo, casualità, sistemi esterni).
20. A (I/O-bound): thread o asyncio, perché il GIL viene rilasciato durante l'I/O. B (CPU-bound in Python puro): processi (`ProcessPoolExecutor`), perché il GIL serializza il bytecode. Bonus: build free-threaded 3.13+ come nota. `time.sleep` blocca l'intero event loop: tutte le altre coroutine si fermano.

## Lettura codice: output esatti e punti attesi

**L01**
```
['apple', 'bread']
['water', 'milk']
['apple', 'bread']
['vip']
['new', 'promo']
True
```
Atteso: `items` di classe condiviso; `b.items = ...` crea un attributo di istanza che fa shadowing; default mutabile `tags=[]` condiviso tra `a` e `b`; `c` ha la propria lista.

**L02**
```
[30, 30, 30]
30
0
False
[(1, 2), (3, 4), (5, 6)]
a ['b', 'c', 'd'] e
3 items
```
Atteso: late binding delle closure (fix `lambda x, i=i:` o `functools.partial`); generatore esaurito; `zip` sullo stesso iteratore; `*middle` produce una lista; walrus.

**L03** (in ordine di gravità)
1. Il generatore viene consumato da `sum` → il secondo ciclo è vuoto → `{}` **silenzioso**. Il bug più grave.
2. Categorie duplicate: assegnazione al posto della somma → percentuali sbagliate.
3. Input vuoto o totale 0 → `ZeroDivisionError`.
4. `float` per gli importi; `round` sulle percentuali → la somma può non fare 100.
5. `split(",")`: virgole nei campi, righe vuote o senza virgola → `ValueError` sull'unpacking; meglio il modulo `csv`.
6. `open` senza `encoding`; il file resta aperto finché il generatore non viene esaurito o chiuso.
7. Importi negativi (rimborsi) non gestiti.
Fix atteso per il punto 1: materializzare (`list`) oppure accettare `Sequence` nella firma, o un solo passaggio che accumula per categoria.

**L04**
```
True
TypeError: cannot use 'Tag' as a set element (unhashable type: 'Tag')
TypeError: unhashable type: 'list'
False
False
1
```
Atteso: `@dataclass` con `eq=True` e non frozen → `__hash__ = None`; frozen genera l'hash dai campi, ma `list` non è hashable; chiave mutata: la ricerca con `p` cade nel bucket di "B2" (False); `Product("A1")` trova il bucket ma `__eq__` con la chiave memorizzata (sku ora "B2") è False; la voce è irraggiungibile ma ancora presente.

**L05**
```
parsed
42
bad value
parsed
None
finally wins
KeyError True
TypeError
```
(Più un `SyntaxWarning` a compile time su Python 3.14 per il `return` nel `finally`, PEP 765; un bonus se lo cita.) Atteso: `finally` eseguito prima che il `return` arrivi al chiamante; `return` nel `finally` **inghiotte** l'eccezione (anche KeyboardInterrupt/SystemExit); `from e` imposta `__cause__` e `__suppress_context__=True`; l'ultima: `1["x"]` → TypeError (int non subscriptable), non KeyError.

**L06**
```
2026-10-26 00:00:00+01:00
1 day, 0:00:00
1 day, 1:00:00
TypeError (confronto tra naive e aware) sollevato dentro is_expired
```
Atteso: `is_expired` **sbagliata** (naive `now()` contro aware → TypeError; correzione: `datetime.now(tz=...)`; e la scadenza va calcolata in UTC o in tempo assoluto). `next_reminder` **corretta**: l'aritmetica tra aware con lo stesso tzinfo ZoneInfo è "wall clock"; corretta solo se `last` è in ROME (se fosse in UTC, sbaglierebbe al cambio d'ora). `day_bounds` **corretta** nel risultato (la mezzanotte successiva, sempre grazie all'aritmetica wall clock), ma `end - start` dice 24 h mentre la durata reale è 25 h; è fuorviante: `timedelta(hours=24)` comunica "24 ore" mentre l'intento è "il giorno dopo" (meglio `timedelta(days=1)` o costruire la data successiva). Chi dichiara tutte e tre sbagliate per "DST" senza distinguere: comprensione al massimo 2. Chi le capisce tutte e tre: 4.

**L07**
```
wrapper None
calling total
3
computing
6
6
TypeError
10
10
```
Problemi di `PriceList`: (1) valore stantio, la cache non sa che `self.prices` è cambiato (visibile); (2) la cache a livello di classe tiene un riferimento forte a `self` → memory leak, le istanze non vengono mai liberate (non visibile); inoltre richiede che `self` sia hashable e la cache è condivisa tra le istanze; `maxsize=None` è illimitata.

**L08** (attesi, in ordine approssimativo): la funzione fa troppo (parsing di due formati + regole di business + persistenza + email); I/O non iniettabile (SMTP hardcoded, `DB` globale, `datetime.now`) → non testabile; stato globale mutabile (`processed`, `DB`); `float` per gli importi; parametri booleani e stringhe (`send`, `fmt`, `debug`) → flag argument; `print` invece di `logging`; il formato sconosciuto restituisce `None` silenziosamente invece di sollevare; nessuna validazione (chiavi mancanti, CSV con una sola riga, email); lo sconto `>100` è un numero magico; l'email viene inviata dentro l'elaborazione (se l'invio fallisce, il DB è già scritto: atomicità/ordine); `smtplib` senza context manager né cleanup in caso di errore; nomi `d`, `t`, `i`, `s`; `datetime.now()` naive. Ristrutturazione attesa: parser per formato → oggetto `Order` validato; funzione pura `compute_total(order) -> Decimal`; repository e notifier iniettati; orchestrazione sottile. Test: funzioni pure senza mock; fake per repository e notifier.

**L09** (attesi): esplosione combinatoria delle sottoclassi (formato × header × compressione); la compressione è un aspetto ortogonale → composizione/decoratore (`Compressed(inner, codec)`); l'header è un'opzione del CSV, non un tipo; `get_exporter` è una catena di if che cresce in modo quadratico, con un caso "not supported" arbitrario; `Exporter` dovrebbe essere ABC/Protocol; restituire bytes in memoria (stream per volumi grandi). Bug latenti: `rows[0]` con input vuoto → IndexError; l'header viene preso dalle chiavi della prima riga mentre i valori seguono l'ordine delle chiavi di ogni riga (dict con ordine diverso → colonne sfasate; chiavi mancanti → righe corte); header non escapato in CSV (virgole e virgolette nei nomi) e costruito a mano invece che con `writer`; `.encode()` senza encoding esplicito (in pratica UTF-8 di default, accettabile); `JsonExporter` è il fallback per qualunque `kind` sconosciuto (anche `"xlsx"`) → errore silenzioso.

**L10**
```
a b 2
['c', 'd'] 1
['e', 'f'] 2
0
g 1
timeout 1.5
```
Atteso: `await` in sequenza → 2 s; `gather` concorrente → 1 s; `time.sleep` blocca il loop → 2 s; creare una coroutine non la esegue (0), parte solo all'`await` (1); `t0` non viene resettato prima del `wait_for`, quindi 1 + 0.5 = 1.5; `wait_for` cancella il task; `asyncio.TimeoutError` è un alias di `TimeoutError` dalla 3.11.

## Scrittura: cosa discriminano i test nascosti
- S01: tie-break per nome, generatore in input, `bool` come grams, NaN/inf, stringa `"100"`, chiavi mancanti → ValueError (non KeyError), whitespace interno con tab e newline, messaggio con `index 2`.
- S02: `ValueError` **alla chiamata** (richiede wrapper non generatore + generatore interno); stream infiniti; numero di elementi letti; liste indipendenti (bug tipico: `current.clear()` dopo `yield`); ValueError lazy sulla decrescenza.
- S03: confine `>= seconds`; collisione tra args e kwargs (`f(1, ("a", 1))` vs `f(1, a=1)`) se la chiave è `args + tuple(sorted(kwargs.items()))`; kwargs non hashable (il bug tipico è calcolare `frozenset(kwargs.items())` fuori dal try); valori falsy in cache (`if cached:`); eccezioni non messe in cache; `__wrapped__`; cache separate.
- S04: `InvalidOperation` non è un ValueError (va tradotta); `bool` è un int; `__eq__` con altri tipi (NotImplemented); `__radd__` con 0 per `sum`; `__rmul__`; confronti con valuta diversa; `allocate` con ratio 0, negativi, un centesimo; valuta non ASCII `ÈUR` (`isalpha` da solo non basta).
- S05: header in ordine diverso, maiuscole, colonne extra; BOM; CRLF; campo tra virgolette con una virgola (chi usa `split(",")` fallisce); numerazione delle righe vuote; errori multipli nell'ordine canonico anche con l'header riordinato; orario inesistente (richiede il round-trip UTC); orario ambiguo con fold=0; `Z` e offset; `round()` del float vs `ROUND_HALF_UP` (0.25 → 0.3); `Decimal("inf")` / `"NaN"` accettati da Decimal ma da rifiutare; tz non valido prima della lettura.

Nota: il README di S05 vincola solo gli attributi. Valutare il design dei tipi (dataclass frozen? errori come dati? separazione parsing/validazione/costruzione?) e la coerenza con `NOTE.md`, scritta prima del codice.
