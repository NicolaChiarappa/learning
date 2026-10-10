# Autovalutazione — Python

Compilala **prima** di guardare le altre parti. Per ogni riga scrivi un numero da 0 a 4 nella colonna "Livello". La colonna "Note" è facoltativa: per esempio "lo uso al lavoro ma non so perché funziona".

- 0 = mai visto
- 1 = ne ho sentito parlare
- 2 = lo uso con l'aiuto della documentazione
- 3 = lo uso con sicurezza
- 4 = saprei spiegarlo e insegnarlo

Sii onesto: questa colonna viene confrontata con i risultati del test per misurare quanto la tua percezione è calibrata. Una buona calibrazione è un'abilità in sé.

| Area | Descrizione                                                                                     | Livello (0-4) | Note                                                                                             |
|------|-------------------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------|
| A1   | Modello dei dati: identità vs uguaglianza (`is`/`==`), mutabilità                               | 1             |                                                                                                  |
| A2   | Assegnazione, aliasing, copia superficiale/profonda, default mutabili                           | 0             |                                                                                                  |
| A3   | Scope LEGB, `global`/`nonlocal`, closures                                                       | 1             |                                                                                                  |
| A4   | Tipi built-in e complessità delle operazioni                                                    | 1             |                                                                                                  |
| A5   | Comprehension, `enumerate`, `zip`, unpacking, walrus, `match`                                   | 1             |                                                                                                  |
| B1   | Firme: positional-only, keyword-only, `*args`, `**kwargs`                                       | 3             |                                                                                                  |
| B2   | Funzioni come oggetti, ordine superiore, `lambda`                                               | 0             |                                                                                                  |
| B3   | Decoratori (semplici, con argomenti, `wraps`, di classe)                                        | 1             |                                                                                                  |
| B4   | `functools`: `partial`, `lru_cache`/`cache`, `reduce`, `singledispatch`                         | 1             | partial l'ho usato                                                                               |
| C1   | Protocollo iteratore, iterabile vs iteratore, esaurimento                                       | 1             | credo di aver usato l'iteratore qualche volta                                                    |
| C2   | Generatori, `yield from`, valutazione lazy, pipeline                                            | 1             |                                                                                                  |
| C3   | `itertools`                                                                                     | 0             |                                                                                                  |
| D1   | Classi, attributi di classe vs istanza, `@property`                                             | 4             |                                                                                                  |
| D2   | Metodi speciali (`__repr__`, `__eq__`, `__hash__`, `__lt__`, container, `__enter__`/`__exit__`) | 1             |                                                                                                  |
| D3   | `dataclasses`, `NamedTuple`, `enum`                                                             | 0             |                                                                                                  |
| D4   | Ereditarietà, MRO, `super()`, mixin                                                             | 4             |                                                                                                  |
| D5   | Composizione vs ereditarietà; `abc` vs `Protocol`                                               | 0             | in Java ne ho sentito parlare e l'ho usato per i design pattern, non so se ti riferisci a quello |
| D6   | `@classmethod`, `@staticmethod`, costruttori alternativi                                        | 1             |                                                                                                  |
| E1   | Eccezioni: gerarchia, custom, `raise from`, quando catturare                                    | 2             |                                                                                                  |
| E2   | Context manager, `contextlib`, `ExitStack`                                                      | 0             |                                                                                                  |
| E3   | Gestione delle risorse e cleanup garantito                                                      | 0             |                                                                                                  |
| F1   | Type hints di base, `Optional`, `\|`, generics delle collezioni                                 | 1             |                                                                                                  |
| F2   | `TypeVar`, generics, `Protocol`, `TypedDict`, `Literal`, `Final`                                | 0             |                                                                                                  |
| F3   | Type checker (mypy/pyright) e lettura degli errori                                              | 2             |                                                                                                  |
| G1   | `collections`                                                                                   | 1             |                                                                                                  |
| G2   | `pathlib`, I/O su file, encoding                                                                | 1             |                                                                                                  |
| G3   | `datetime`/`zoneinfo`, naive vs aware, fusi orari                                               | 1             |                                                                                                  |
| G4   | `json`, `csv`, serializzazione, `decimal`                                                       | 1             |                                                                                                  |
| G5   | `logging` configurato correttamente                                                             | 1             |                                                                                                  |
| G6   | `re` e quando non usarle                                                                        | 2             | so cosa sono, a cosa servono ma non so propriamente scriverle                                    |
| H1   | pytest: asserzioni, struttura, naming                                                           | 1             |                                                                                                  |
| H2   | Fixture, `parametrize`, `tmp_path`, `monkeypatch`                                               | 0             |                                                                                                  |
| H3   | Mocking: cosa mockare e cosa no                                                                 | 1             |                                                                                                  |
| H4   | Progettare codice testabile                                                                     | 0             |                                                                                                  |
| I1   | Thread vs processi vs async, GIL                                                                | 1             |                                                                                                  |
| I2   | `concurrent.futures`                                                                            | 0             |                                                                                                  |
| I3   | `asyncio`                                                                                       | 0             |                                                                                                  |
| J1   | Moduli, package, import, import circolari                                                       | 2             |                                                                                                  |
| J2   | Ambienti virtuali, dipendenze, `pyproject.toml`                                                 | 2             |                                                                                                  |
| J3   | Linting e formattazione (ruff, black)                                                           | 2             |                                                                                                  |
| J4   | Debugging: `pdb`/`breakpoint()`, traceback                                                      | 2             | solo breakpoint e logger                                                                         |
| J5   | Profiling e performance                                                                         | 0             |                                                                                                  |
| K1   | Naming, leggibilità, funzioni piccole                                                           | 3             |                                                                                                  |
| K2   | Separazione delle responsabilità, accoppiamento                                                 | 3             |                                                                                                  |
| K3   | Gestione dello stato e immutabilità                                                             | 0             |                                                                                                  |
| K4   | Validazione degli input e confini del sistema                                                   | 1             |                                                                                                  |
| K5   | Analisi dei casi limite                                                                         | 1             |                                                                                                  |
| K6   | SOLID, YAGNI, quando astrarre                                                                   | 2             |                                                                                                  |
| K7   | Refactoring sicuro con i test                                                                   | 0             |                                                                                                  |

Tempo impiegato: 10 min
