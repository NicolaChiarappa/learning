# Mappa competenze — Python

Riferimento fisso per assessor e planner. Ogni area si valuta da 0 a 4.
Livello 3 = "lo uso con sicurezza in codice reale". Livello 4 = "so spiegare il perché e i trade-off".

## A. Fondamentali del linguaggio
- A1. Modello dei dati: tutto è un oggetto, identità vs uguaglianza (`is` vs `==`), mutabilità
- A2. Nomi e riferimenti: assegnazione, aliasing, copia superficiale e profonda, argomenti di default mutabili
- A3. Scope: LEGB, `global` e `nonlocal`, closures
- A4. Tipi built-in e loro costi: list, tuple, dict, set, str, bytes; complessità delle operazioni principali
- A5. Controllo di flusso idiomatico: comprehension, `enumerate`, `zip`, unpacking, walrus, `match`

## B. Funzioni
- B1. Firme: positional-only, keyword-only, `*args`, `**kwargs`, valori di default
- B2. Funzioni come oggetti, funzioni di ordine superiore, `lambda` (e quando evitarla)
- B3. Decoratori: semplici, con argomenti, `functools.wraps`, decoratori di classe
- B4. `functools`: `partial`, `lru_cache`/`cache`, `reduce`, `singledispatch`

## C. Iterazione
- C1. Protocollo iteratore: `__iter__`/`__next__`, iterabile vs iteratore, esaurimento
- C2. Generatori: `yield`, `yield from`, valutazione lazy, pipeline di generatori
- C3. `itertools`: `chain`, `groupby`, `islice`, `product`, `accumulate`, `tee`

## D. Programmazione a oggetti
- D1. Classi, istanze, attributi di classe vs istanza, `@property`
- D2. Metodi speciali (dunder): `__repr__`, `__eq__`, `__hash__`, `__lt__`, container protocol, `__enter__`/`__exit__`
- D3. `dataclasses` (frozen, slots, field, post_init), `NamedTuple`, `enum`
- D4. Ereditarietà, MRO, `super()`, mixin
- D5. Composizione vs ereditarietà; classi astratte (`abc`) vs Protocol
- D6. `@classmethod`, `@staticmethod`, costruttori alternativi

## E. Errori e risorse
- E1. Eccezioni: gerarchia, eccezioni custom, `raise from`, quando catturare e quando lasciar propagare
- E2. Context manager: `with`, `contextlib.contextmanager`, `ExitStack`
- E3. Gestione delle risorse: file, connessioni, cleanup garantito

## F. Type hints
- F1. Annotazioni di base, `Optional`, union con `|`, collezioni generiche
- F2. `TypeVar`, generics, `Protocol`, `TypedDict`, `Literal`, `Final`
- F3. Uso di un type checker (mypy o pyright) e lettura dei suoi errori

## G. Libreria standard essenziale
- G1. `collections`: `defaultdict`, `Counter`, `deque`, `OrderedDict`, `ChainMap`
- G2. `pathlib`, I/O su file, encoding
- G3. `datetime` e `zoneinfo`: date naive vs aware, fusi orari, aritmetica sulle date
- G4. `json`, `csv`, serializzazione; `decimal` per gli importi
- G5. `logging` configurato correttamente (non `print`)
- G6. `re`: espressioni regolari di base, quando non usarle

## H. Testing
- H1. pytest: asserzioni, struttura dei test, naming
- H2. Fixture, `parametrize`, `tmp_path`, `monkeypatch`
- H3. Mocking (`unittest.mock`): cosa mockare e cosa no
- H4. Progettare codice testabile: dipendenze esplicite, funzioni pure, effetti collaterali ai bordi

## I. Concorrenza
- I1. Thread vs processi vs async; il GIL e cosa comporta
- I2. `concurrent.futures`
- I3. `asyncio`: coroutine, `await`, `gather`, task, timeout, quando async non serve

## J. Progetto e strumenti
- J1. Moduli, package, import assoluti e relativi, `__init__.py`, import circolari
- J2. Ambienti virtuali, gestione dipendenze (pip, uv o poetry), `pyproject.toml`
- J3. Linting e formattazione (ruff, black)
- J4. Debugging: `pdb`/`breakpoint()`, lettura dei traceback
- J5. Profiling e performance: `timeit`, `cProfile`, scelta degli algoritmi

## K. Design e qualità (trasversale)
- K1. Naming e leggibilità; funzioni piccole con una sola responsabilità
- K2. Separazione delle responsabilità; dipendenze esplicite; accoppiamento
- K3. Gestione dello stato e immutabilità
- K4. Validazione degli input e confini del sistema (fidarsi solo dei dati validati)
- K5. Analisi dei casi limite: input vuoti, None, duplicati, ordine, grandi volumi, errori esterni
- K6. Principi SOLID applicati a Python (senza dogmatismi); YAGNI; quando astrarre
- K7. Refactoring di codice esistente senza romperlo (con i test come rete)
