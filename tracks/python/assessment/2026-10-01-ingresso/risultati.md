# Risultati ingresso — python — 2026-10-10

Test preparato il 2026-10-01, svolto tra il 2026-10-09 e il 2026-10-10. Test eseguiti con Python 3.14.7 e pytest 9.1.1.

## Sintesi

- **Nessuna area raggiunge il livello 3.** Su 49 aree: 41 misurate, di cui 6 a livello 2, 21 a livello 1, 14 a livello 0. Il livello reale è "principiante che usa Python per imitazione": la sintassi di base c'è, il modello del linguaggio (riferimenti, attributi, iteratori, eccezioni) no.
- **Scrittura codice: 10/28 test base, 14/166 test nascosti.** Due esercizi su cinque consegnati (in 60 min ciascuno contro 20-30 previsti, il primo con aiuti), tre saltati senza tentativo.
- **Concetti: 13 domande su 20 con "non lo so", 0 risposte complete.** Lettura codice: nessuno snippet con output previsto correttamente, nessuna sezione "Spiegazione" compilata.
- **Calibrazione: buona in basso, sbagliata in alto.** I voti 0-1 sono quasi tutti confermati. Tutti e 5 i voti ≥3 (D1, D4, B1, K1, K2) non sono confermati; D1 è sovrastimata di 3 punti.
- **L'unico segnale sopra la media è nel design**: diagnosi corretta e autonoma dell'esplosione combinatoria in L09 e idea spontanea di "modulo di confine" in D1. È intuizione portata da Java, non ancora tradotta in Python funzionante.

## Tabella competenze

Scala 0-4. "Auto" = autovalutazione. Dove l'evidenza è una sola o indiretta è scritto "(evidenza debole)". Sigle: Cn = domanda di concetti, Lnn = snippet di lettura, Snn = esercizio di scrittura, Dn = domanda di design.

| Area | Auto | Osservato | Evidenza | Categoria |
|---|---|---|---|---|
| A1 Identità, uguaglianza, mutabilità | 1 | 1 | C1 "non lo so". Usa `is None` per abitudine (S02) senza saperlo motivare. S01: `for sub in substrings: sub.strip()` scarta il risultato (immutabilità di `str` non acquisita). Bug `if "grams" or "food" not in ...`: valore di verità di una stringa non capito, serviti indizi di livello 2. | DA IMPARARE |
| A2 Aliasing, copie, default mutabili | 0 | 0 | C2: non sa cosa produce `[[0]*3]*3`, la griglia proposta è sbagliata. L01: 0 righe corrette su 6. | DA IMPARARE |
| A3 Scope, closures | 1 | 1 | C4: prevede l'errore ma la regola enunciata è falsa ("la funzione vede solo le variabili del corpo o gli argomenti"); nessuna delle due correzioni è utilizzabile. L02 closure: "non lo so". | DA IMPARARE |
| A4 Tipi built-in e costi | 1 | 1 | C3 "non lo so" su tutta la linea. S01: usa dict e list ma con una struttura parallela (lista + dict di indici) al posto di un solo dict. | DA IMPARARE |
| A5 Controllo di flusso idiomatico | 1 | 1 | S01: contatore manuale al posto di `enumerate`, nessuna comprehension. L02: unpacking con `*` e walrus dichiarati "non lo so". Precedenza `or` / `not in` non nota. | DA IMPARARE |
| B1 Firme | 3 | 1 | C5: motivo plausibile per keyword-only, nulla su positional-only ("non saprei"). L08: nel proprio redesign mantiene il flag booleano posizionale `send=True`. Tetto massimo 2 (evidenza debole: una domanda). | DA IMPARARE |
| B2 Funzioni come oggetti, lambda | 0 | 1 | S01: usa `sorted(key=itemgetter(...))`. L02: lambda in comprehension "non lo so". | DA IMPARARE |
| B3 Decoratori | 1 | 1 | L07: capisce cosa fa un decoratore semplice e prevede `calling total` / `3`; sbaglia `__name__`, non conosce `__doc__`. C7 "non lo so". S03 non tentato ("non so fare un decoratore"). | DA IMPARARE |
| B4 functools | 1 | 0 | L07: tutta la parte `lru_cache` e `PriceList` senza risposta. C7 `wraps` "non lo so". `partial` (dichiarato "l'ho usato") non misurato. | DA IMPARARE |
| C1 Iteratore vs iterabile, esaurimento | 1 | 1 | C6: intuizione corretta ma dichiarata tale ("ad intuito"). L02: prevede 30 anche per il secondo `sum` e `True` per `4 in squares`. L03: non vede il generatore consumato, cioè il bug più grave dello snippet. | DA IMPARARE |
| C2 Generatori, lazy | 1 | 1 | C6: "non caricare tutto in memoria, ma non so di cosa stiamo parlando davvero". S02: nessun `yield`, costruisce tutta la lista; i due test su stream infiniti non terminano. | DA IMPARARE |
| C3 itertools | 0 | 0 | C8 "non lo so". | DA IMPARARE |
| D1 Classi, attributi di classe/istanza, property | 4 | 1 | C11 "non lo so". L01: 0/6, compreso "Errore, non è definito items" per un attributo di classe. Sa scrivere la sintassi di una classe (L08, L09). `@property` mai citata. | DA IMPARARE |
| D2 Metodi speciali | 1 | 0 | C9 "non lo so". L04 "qui non so nulla". S04 non tentato. | DA IMPARARE |
| D3 dataclasses, NamedTuple, enum | 0 | 0 | C10 "non li ho mai sentiti questi nomi". L04 vuoto. | DA IMPARARE |
| D4 Ereditarietà, MRO, super, mixin | 4 | 2 | L08: ereditarietà singola con metodo da ridefinire, corretta ma solo in pseudo-codice e senza alcuna chiamata a `super()`. C16: risposta sbagliata e non vede perché la domanda abbia senso. MRO, `super()` cooperativo, mixin: 0. | DA POTENZIARE |
| D5 Composizione vs ereditarietà, abc vs Protocol | 0 | 2 | L09: individua da solo i due assi indipendenti e propone di passare il compressore al costruttore. Lo schizzo ha errori (variabili non definite) e il nome del pattern è impreciso. C17 (abc vs Protocol) "non lo so". | DA POTENZIARE |
| D6 classmethod, staticmethod | 1 | non misurato | Coperto solo da S04, non tentato. | — |
| E1 Eccezioni | 2 | 1 | C12: criterio generico, `raise from` sconosciuto. L05: nessun output riga per riga, ragionamento lasciato irrisolto. L03: la correzione proposta cattura `Exception` e fa `print(e)`. S01: eccezioni usate come flusso di controllo, `IndexError` per una chiave assente in un dict. Positivo: L08 "invece di printare facciamo un raise". | DA IMPARARE |
| E2 Context manager | 0 | 0 | C13 "non so cosa sia un context manager" (pur usando `with open`). | DA IMPARARE |
| E3 Gestione delle risorse | 0 | 0 | C13. L08: SMTP senza cleanup non notato. | DA IMPARARE |
| F1 Type hints di base | 1 | 1 | C18: sa che non sono controllati a runtime. Le funzioni di supporto di S01 non sono annotate. | DA IMPARARE |
| F2 Generics, Protocol, TypedDict | 0 | 0 | C18 seconda parte "non so". | DA IMPARARE |
| F3 Type checker | 2 | non misurato | Non coperto dal test. Dato indiretto: non ha saputo interpretare da solo un avviso dell'IDE in S01. Il 2 dichiarato non ha supporto. | — |
| G1 collections | 1 | 1 | S01: non usa `defaultdict` né `Counter` dove sarebbero la scelta naturale (evidenza debole; voce frainteso in origine e corretta dopo chiarimento). | DA IMPARARE |
| G2 pathlib, I/O, encoding | 1 | 1 | L03: nota che l'apertura può fallire, non nota encoding né durata dell'apertura del file. S05 non tentato (evidenza debole). | DA IMPARARE |
| G3 datetime, zoneinfo | 1 | 0 | C15 "non lo so". L06: `day_bounds` "non ho capito come funziona", `is_expired` prevista `False` (non vede il confronto naive/aware), nessun giudizio sulle tre funzioni. | DA IMPARARE |
| G4 json, csv, decimal | 1 | 0 | C14 "non ne ho idea". L03: non cita `float` per gli importi né il modulo `csv`; il controllo proposto sulle virgole è sbagliato. | DA IMPARARE |
| G5 logging | 1 | 1 | C19a "non so rispondere". L08: nello schizzo sostituisce `print` con `logger.debug`. | DA IMPARARE |
| G6 re | 2 | non misurato | Non coperto. | — |
| H1 pytest di base | 1 | 1 | Esegue i test; aiuto per leggere un `AssertionError`, non conosce `-k`, directory di lavoro sbagliata al primo lancio. Nessun test proprio. | DA IMPARARE |
| H2 Fixture, parametrize | 0 | non misurato | Nessun `test_mine_*.py`. | — |
| H3 Mocking | 1 | 0 | C19b "non so rispondere". D1: "come scelgo cosa può essere mockato non lo so". L08 punto 3 senza risposta. | DA IMPARARE |
| H4 Codice testabile | 0 | 1 | D1: "il modulo di confine dipende da uno o più provider" è l'idea giusta, ma confonde un doppio di test con un fallback di produzione. L08: nel redesign nessuna dipendenza iniettata. | DA IMPARARE |
| I1 Thread, processi, async, GIL | 1 | 0 | C20 "non lo so". | DA IMPARARE |
| I2 concurrent.futures | 0 | non misurato | Non citato. | — |
| I3 asyncio | 0 | 0 | C20, L10 "questo argomento non lo so". | DA IMPARARE |
| J1 Moduli, import circolari | 2 | 1 | D2: la spiegazione dell'import circolare non descrive il meccanismo; corretta solo l'idea di mantenere il punto di import esistente. Directory di lavoro sbagliata con pytest. | DA IMPARARE |
| J2 Ambienti virtuali, dipendenze | 2 | non misurato | Non coperto. | — |
| J3 Linting e formattazione | 2 | non misurato | Non coperto. Dato indiretto: import inutilizzato, `print` di debug lasciato, stile incoerente nei file consegnati. | — |
| J4 Debugging, traceback | 2 | 1 | Osservazione diretta: aiuto per leggere un traceback con eccezioni concatenate e l'output di pytest; `print(sessioni)` rimasto in S02 (evidenza da osservazione, non da domanda). | DA IMPARARE |
| J5 Profiling | 0 | non misurato | Non coperto. | — |
| K1 Naming, funzioni piccole | 3 | 2 | Scomposizione in funzioni piccole presente (S01). Naming debole in ogni consegna: nomi in italiano contro la convenzione, nomi che dicono il tipo e non il ruolo (`lista`, `dizionario`, `valore`), `clean_dict` non pulisce nulla, `food_exist` restituisce un indice o solleva. Nel redesign di L08 conserva `d`, `t`, `i` e non segnala i nomi tra i problemi. | DA POTENZIARE |
| K2 Separazione delle responsabilità | 3 | 2 | Riconosce "funzione che fa più cose" (L08), l'esplosione di classi (L09), la direzione delle dipendenze (D2). Il redesign di L08 però rimette parsing, validazione, calcolo, salvataggio e invio in un'unica classe. | DA POTENZIARE |
| K3 Stato e immutabilità | 0 | 0 | C10. L08: lo stato globale è letto come "manca un DB vero", non come stato mutabile condiviso; nel redesign aggiunge stato (`self.d`). | DA IMPARARE |
| K4 Validazione e confini | 1 | 2 | S01: 11 voci non valide su 13 rifiutate. D1: confine che "pulisce e normalizza" enunciato spontaneamente. L03, L08: segnala l'input malformato. Mancano `bool` e infinito, e il formato del messaggio richiesto. | DA POTENZIARE |
| K5 Casi limite | 1 | 1 | Vede il totale zero (L03) ma la correzione controlla la variabile sbagliata. Non vede duplicati, generatore consumato, input vuoto (`rows[0]` in L09: nessun bug latente trovato). S02: timestamp decrescenti e stream infinito ignorati benché scritti nella consegna. | DA IMPARARE |
| K6 SOLID, YAGNI | 2 | 2 | L09: diagnosi corretta. L08: per due formati introduce gerarchia più factory. Nomi dei pattern usati in modo impreciso. D2 "cosa non faresti": "non lo so". | DA POTENZIARE |
| K7 Refactoring sicuro | 0 | 1 | D2: una sola idea valida (compatibilità degli import); nessun ordine dei passi, nessuna rete di sicurezza, nessun criterio di fine. | DA IMPARARE |

Riepilogo: SOLIDO 0, DA POTENZIARE 6 (D4, D5, K1, K2, K4, K6), DA IMPARARE 35, non misurato 8 (D6, F3, G6, H2, I2, J2, J3, J5).

Aree misurate solo in teoria perché gli esercizi 03, 04, 05 non sono stati tentati: B3, B4 (decoratore con stato), D2, D3, G4 `decimal`, E1 con eccezioni custom, G2, G3, G4 `csv`. Per queste il voto viene dalle sole risposte scritte; la pratica resta non misurata. Dato che la teoria è a 0-1, il voto non cambierebbe verso l'alto.

## Calibrazione

**Sovrastime con scarto ≥2**

| Area | Auto | Osservato | Scarto | Dato |
|---|---|---|---|---|
| D1 | 4 | 1 | -3 | "Saprei insegnarlo", ma C11 "non lo so" e L01 0/6. |
| D4 | 4 | 2 | -2 | Usa l'ereditarietà singola; C16 sbagliata, MRO e mixin sconosciuti. |
| B1 | 3 | 1 | -2 | Metà di C5 senza risposta; evidenza debole, tetto 2. |

**Sovrastime con scarto 1** (sotto soglia, ma il valore dichiarato non è confermato): K1 (3→2), K2 (3→2), E1 (2→1), J1 (2→1), J4 (2→1), B4, D2, G3, G4, H3, I1 (tutte 1→0).

**Sottostime con scarto ≥2**

| Area | Auto | Osservato | Scarto | Dato |
|---|---|---|---|---|
| D5 | 0 | 2 | +2 | L09: diagnosi e proposta di composizione autonome. Vale per la metà "composizione vs ereditarietà"; `abc` e `Protocol` restano a 0. |

**Sottostime con scarto 1**: B2, H4, K4, K7.

**Cosa significa**

1. I cinque voti più alti dell'autovalutazione (D1, D4, B1, K1, K2) sono tutti sopra l'osservato. Il 4 su D1 e D4 misura la familiarità con la sintassi delle classi, non la conoscenza del loro funzionamento: Nick confonde "lo scrivo spesso" con "so come funziona".
2. Sui voti bassi la calibrazione è buona: 22 aree misurate su 41 coincidono esattamente, 37 su 41 stanno entro un punto. Nick sa riconoscere ciò che non ha mai visto; non sa riconoscere ciò che usa senza capire.
3. La sicurezza dichiarata sugli esercizi non regge: 4/5 su S01 e S02 con "tutti" i test base passati, contro 6/19 e 7/14 nei test nascosti. Le istruzioni dicevano che i test base non bastano. Sicurezza 3/5 sulla parte 3 senza uno snippet corretto.
4. La sicurezza 2/5 sulle parti 2 e 5 è invece coerente con il risultato.
5. Tempo della parte 3: annotati 150 min, osservati 200. I tempi osservati per le parti 2, 3 e 5 non corrispondono alle stime (30 su 60, 200 su 60, 10 su 40): sforzo concentrato dove si può scrivere codice, minimo dove si deve argomentare.

## Pattern di ragionamento osservati

1. **"Test verdi = finito".** In S01 e S02 si ferma quando passano i test base. Regole scritte nella consegna restano non implementate: formato `index <i>` (S01, regola 5), timestamp decrescenti e laziness (S02, regole 3 e 5), più la nota finale che avvisava della tensione tra le regole 4 e 5. La consegna viene letta come contesto, non come specifica.
2. **Non spiega il perché.** Dieci sezioni "Spiegazione" su dieci vuote; in L08 i problemi non sono ordinati né motivati e i punti 3 e 4 del compito mancano; D1 e D2 liquidate in 10 minuti. Lo dice lui stesso: "non so spiegare perché prendere certe scelte". È il limite principale rispetto all'obiettivo dichiarato di imparare a pensare il codice.
3. **Davanti a un problema di design scrive classi, non analisi.** In L08 e L09 la risposta è uno scheletro di classi con ereditarietà e factory, scritto dentro il file dello snippet. La struttura arriva prima dell'elenco di cosa deve cambiare e perché. I nomi dei pattern vengono usati come soluzione ("Abstract Factory") senza verificare che corrispondano al problema.
4. **Evita ciò che non sa già fare.** Tre esercizi su cinque saltati, rifiutando anche un tentativo di 20 minuti con nota sul punto di blocco. Nessun `NOTE.md`, nessuna firma, nessuna riga. Un tentativo fallito avrebbe mostrato dove si ferma; così manca il dato. In positivo: scrive "non lo so" invece di inventare, come richiesto.
5. **Modello mentale del linguaggio assente, lavora per tentativi.** Il bug `if "grams" or "food" not in ...` è stato vissuto come comportamento "assurdo" del linguaggio, non come ipotesi da verificare. Aiuto necessario per leggere un traceback, un'asserzione di pytest, un avviso del type checker. Non scompone l'espressione, non prova nel REPL di sua iniziativa.
6. **Casi limite: ne vede uno, quello dell'input malformato.** Segnala con costanza file mancante, riga malformata, divisione per zero. Non considera mai: input vuoto, duplicati, ordine, iteratore consumato, valori speciali (`bool`, infinito), volumi grandi.
7. **Naming che descrive il tipo, non il ruolo**, e in italiano contro la convenzione del progetto. Messaggi d'errore misti italiano/inglese e a volte falsi (`"grams non trovato"` quando manca `food`).
8. **Segnale positivo specifico:** quando il problema è strutturale e riconoscibile (L09: due assi indipendenti; D1: confine tra API e sistema; D2: direzione delle dipendenze) la diagnosi è corretta e autonoma. Le domande poste durante la parte 3 (classi o funzioni, `DB` errore o semplificazione) mostrano che si interroga sul design. Manca il passaggio dalla diagnosi a codice Python corretto.

## Esercizi di scrittura

Totale: test base 10/28, test nascosti 14/166.

| Esercizio | Base | Nascosti | Tempo | Stato |
|---|---|---|---|---|
| 01-aggregate-portions | 5/5 | 6/19 | 60 min (stima 20-25) | consegnato, con aiuti |
| 02-split-sessions | 5/5 | 7/14 | 60 min (stima 30) | consegnato |
| 03-ttl-cache | 0/6 | 0/22 | 0 | non tentato |
| 04-money | 0/7 | 1/67 | 0 | non tentato |
| 05-meal-import | 0/5 | 0/44 | 0 | non tentato |

**01-aggregate-portions.** Aggregazione, normalizzazione e ordinamento corretti, anche a parità di totale e con un generatore in ingresso. Falliscono tutti i 13 test di validazione: in 11 casi l'errore viene sollevato ma il messaggio non contiene `index <i>` come richiesto dalla regola 5; in 2 casi (`True` e infinito come grammi) non viene sollevato nulla e il valore entra nel totale. Il valore non numerico "NaN" è rifiutato per caso, non per un controllo. Struttura: lista di tuple più dict di indici mantenuti in parallelo, con un'eccezione `IndexError` usata per dire "chiave assente"; un ciclo che non ha effetto; import inutilizzato; l'eccezione originale viene sostituita perdendo il motivo. Risultato non autonomo: quattro interventi dell'orchestratore, di cui uno su un bug di logica. Il 6/19 è un limite superiore.

**02-split-sessions.** Corretto solo il raggruppamento su input finito e ordinato. La funzione costruisce tutte le sessioni in memoria e restituisce una lista: non è un iteratore, legge l'intero stream alla chiamata, non termina su stream infiniti (i due test relativi sono stati interrotti dopo 2 secondi; contati come falliti). Nessun controllo sui timestamp decrescenti (regola 3 ignorata). `print(sessioni)` lasciato nel codice. L'errore su `max_gap` alla chiamata funziona solo perché la funzione non è un generatore: la tensione indicata nella consegna non è stata affrontata.

**03-ttl-cache.** Non tentato. Nota nel file: "Non so fare né un decoratore né una cache questo esercizio lo salto".

**04-money.** Non tentato; scheletro intatto. L'unico test nascosto verde dipende dallo scheletro fornito, non da codice di Nick.

**05-meal-import.** Non tentato; `NOTE.md` vuota. Era l'esercizio con la scelta di design: su questo punto il test non ha prodotto dati.

## Note sullo svolgimento

- Gli snippet `03_find_the_bugs_shares.py`, `08_design_order_processing.py` e `09_design_exporters.py` sono stati modificati inserendo le risposte nel file. Non incide sulla valutazione.
- Autovalutazione: le righe G1 e D5 sono state corrette dopo un chiarimento sul significato delle voci, prima di aprire la parte 2.
- La `.venv` non è stata creata nella cartella del test come da istruzioni; i test sono stati eseguiti con quella alla radice del repository.
