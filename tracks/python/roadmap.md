# Roadmap — python
Ultimo aggiornamento: 2026-10-10 — fonte: `tracks/python/assessment/2026-10-01-ingresso/risultati.md`

## Obiettivo finale della track
Alla fine Nick scrive Python partendo dalla specifica e non dai test: da una consegna ricava da solo l'elenco delle regole e dei casi limite, scrive una nota di design motivata, implementa con gli strumenti giusti del linguaggio (generatori, context manager, dataclasses, eccezioni proprie, type hints) e consegna codice che passa test che non ha visto. Sa prevedere l'output di codice che non ha scritto e spiegare perché, cioè ha un modello mentale del linguaggio e non lavora per tentativi. Obiettivo misurabile: livello 3 sulle aree A-H e K, livello 2 su I e J, alla verifica finale.

## Valutazione onesta della durata
La sequenza di `CLAUDE.md` (Python nelle settimane 1-5, Django dalla 3) **non è realistica con il livello misurato** e va allungata.

- Dati: 0 aree a livello 3 su 41 misurate, 35 DA IMPARARE, 14 a livello 0. Test nascosti 14/166. Tempi osservati 2-3 volte le stime sugli esercizi consegnati.
- Stima: 23 moduli, **74 giorni di lavoro** sui moduli, più circa 8 giorni tra mini-verifiche e ripassi. A 5 giorni a settimana sono **16-17 settimane** per la track completa in sequenza. Forbice realistica: 14-20 settimane.
- La stima è incerta: la velocità di Nick sugli esercizi è nota da due sole consegne. La prima mini-verifica (V1) serve anche a ricalibrare le durate.
- Proposta di sequenza (da confermare con Nick, vedi "Decisioni aperte"):
  - Python Fasi 1-3 da solo: settimane 1-11 circa.
  - Django/Ninja: test d'ingresso alla fine della Fase 3, cioè **verso la settimana 12** invece della 3. Da lì Python (Fase 4) prosegue in parallelo a circa metà ritmo e finisce verso la settimana 21-22.
  - TypeScript/React/Expo: non prima della chiusura della Fase 4 di Python, circa settimana 22 invece della 5.
  - Capstone: circa 3 settimane dopo l'avvio di TypeScript, quindi non prima della settimana 25 invece della 8.
- Perché non partire prima con Django: Nick lo usa già in produzione senza il modello sottostante (attributi di classe vs istanza a livello 1, iteratori a 1, decoratori a 1, context manager a 0, type hints a 0-1). Una track Django adesso produrrebbe altra imitazione. I moduli di questa roadmap agganciano comunque Django dove è utile, così il lavoro quotidiano diventa materiale di studio.

## Calendario indicativo
Ipotesi: inizio 2026-10-12, 5 giorni a settimana, 3-4 ore al giorno di pratica deliberata. Il resto delle ore va in lettura della teoria e di sorgenti, non in altri esercizi.

| Fase | Moduli | Giorni | Settimane (indicative) | Cosa sblocca |
|---|---|---|---|---|
| 1 — Modello del linguaggio e metodo | M01-M05 | 15 | 1-3 | Prevedere cosa fa il codice; lavorare da specifica |
| 2 — Eccezioni, oggetti, iterazione | M06-M10 | 15 | 4-6 | Classi e generatori capiti, non imitati |
| 3 — Strumenti per Django e capstone | M11-M16 | 19 | 7-11 | Prerequisiti di Django/Ninja e del capstone |
| 4 — Design, test, progetto | M17-M23 | 25 | 12-16 da solo, 12-22 in parallelo con Django | Livello 3 su design e qualità |

**Mini-verifiche (assessor, modalità verifica), ogni 2 settimane**: V1 il 2026-10-23, poi 2026-11-06, 2026-11-20, 2026-12-04, 2026-12-18, e così via. Ogni verifica occupa circa mezza giornata, copre i moduli chiusi nelle due settimane e riprende almeno un'area di moduli più vecchi. Dopo ogni verifica il planner aggiorna questa roadmap. Le date si spostano se l'inizio effettivo cambia.

## Metodo: vale in ogni modulo
Il test ha mostrato che il limite principale non è la sintassi ma il modo di lavorare. Queste regole non sono un modulo: sono parte della consegna di ogni esercizio e della sua valutazione.

1. **Nota di design prima del codice** (`design.md`, regola 2 di `CLAUDE.md`). In Fase 1 è corta: 5-10 righe. Cresce con i moduli.
2. **Elenco delle regole ricavato dalla consegna.** Prima di scrivere codice Nick numera in `design.md` ogni regola della consegna. A fine esercizio la spunta una per una, indicando il test che la copre. Contrasta "test verdi = finito".
3. **Elenco dei casi limite con griglia fissa**: vuoto, None, duplicati, ordine, valori speciali (`bool`, zero, negativo, infinito, NaN), iteratore consumato, grandi volumi, errore esterno. Per ogni voce: "si applica / non si applica, perché".
4. **Motivazione scritta delle scelte**: almeno una scelta per esercizio con l'alternativa scartata e il motivo ("ho usato X invece di Y perché..."). Una scelta senza alternativa non conta.
5. **Analisi prima della struttura**: nei problemi di design, prima "cosa cambia e perché", poi le classi. Vietato nominare un pattern prima di aver scritto il problema che risolve.
6. **Previsione e sicurezza dichiarate prima della verifica**: Nick scrive cosa si aspetta (output, numero di test nascosti che passeranno) e poi confronta. Il reviewer registra lo scarto. Serve alla calibrazione.
7. **Ipotesi, non "è assurdo"**: davanti a un comportamento inatteso Nick scrive un'ipotesi e la verifica nel REPL o con un test prima di chiedere aiuto.
8. **Tentativo minimo obbligatorio**: nessun esercizio si salta. Se Nick non sa da dove partire, lavora 20 minuti e consegna una nota con il punto esatto di blocco. Quella nota è una consegna valida e viene valutata.
9. **Dimensione degli esercizi**: in Fase 1 ogni esercizio dura 20-45 minuti e tocca un solo concetto nuovo. In Fase 2 fino a 60-90 minuti. Esercizi più grandi solo dalla Fase 3. Formati iniziali: prevedi e verifica, trova e correggi il bug, scrivi una funzione piccola da specifica.
10. **Codice in inglese, nomi per ruolo e non per tipo**: vale da M01; il reviewer lo valuta sempre (K1).

Nessuna area è risultata SOLIDA, quindi non ci sono esercizi di solo consolidamento fino al modulo finale. Le 6 aree DA POTENZIARE (D4, D5, K1, K2, K4, K6) sono trattate con esercizi che espongono le crepe, senza teoria di base.

## Panoramica
| # | Modulo | Tipo | Stima | Prerequisiti | Stato |
|---|---|---|---|---|---|
| M01 | Nomi, oggetti, riferimenti | DA ZERO | 3 gg | — | da fare |
| M02 | Dalla specifica ai test: casi limite, pytest, traceback | DA ZERO | 3 gg | M01 | da fare |
| M03 | Tipi built-in, costi, `collections` | DA ZERO | 3 gg | M01, M02 | da fare |
| M04 | Controllo di flusso idiomatico | DA ZERO | 2 gg | M03 | da fare |
| M05 | Funzioni: firme, scope, closures | DA ZERO | 4 gg | M01, M04 | da fare |
| M06 | Eccezioni | DA ZERO | 3 gg | M02, M05 | da fare |
| M07 | Classi: attributi di classe e istanza, property, classmethod | DA ZERO | 3 gg | M01, M05 | da fare |
| M08 | Metodi speciali | DA ZERO | 3 gg | M07 | da fare |
| M09 | Iteratori e generatori | DA ZERO | 4 gg | M05, M08 | da fare |
| M10 | `itertools` e pipeline lazy | DA ZERO | 2 gg | M09 | da fare |
| M11 | Decoratori e `functools` | DA ZERO | 4 gg | M05, M07 | da fare |
| M12 | Context manager e gestione delle risorse | DA ZERO | 3 gg | M06, M08, M09, M11 | da fare |
| M13 | `dataclasses`, `enum`, immutabilità | DA ZERO | 3 gg | M08 | da fare |
| M14 | Type hints e type checker | DA ZERO | 3 gg | M05, M13 | da fare |
| M15 | Importi e serializzazione: `decimal`, `json`, `csv` | DA ZERO | 3 gg | M06, M13 | da fare |
| M16 | `datetime` e `zoneinfo` | DA ZERO | 3 gg | M13 | da fare |
| M17 | Ereditarietà, MRO, `super()`, mixin | POTENZIAMENTO | 3 gg | M07, M08 | da fare |
| M18 | Composizione, `abc` e `Protocol`, quando astrarre | POTENZIAMENTO | 3 gg | M14, M17 | da fare |
| M19 | Testing: fixture, parametrize, mock, codice testabile | DA ZERO | 4 gg | M02, M18 | da fare |
| M20 | Moduli, package, strumenti, logging | DA ZERO | 3 gg | M06 | da fare |
| M21 | Refactoring sicuro e separazione delle responsabilità | POTENZIAMENTO | 4 gg | M18, M19, M20 | da fare |
| M22 | Concorrenza: thread, processi, `asyncio` | DA ZERO | 4 gg | M09, M12 | da fare |
| M23 | Progetto di sintesi: import di pasti | CONSOLIDAMENTO | 4 gg | M12, M15, M16, M19, M21 | da fare |

Totale: 23 moduli, 74 giorni di lavoro.

Copertura delle aree non misurate: D6 in M07, F3 in M14, G6 in M15, H2 in M19, J2 e J3 in M20, I2 in M22, J5 in M03 e M10. Per queste il primo esercizio del modulo funziona da misura: se Nick è già a livello 2 o più, il planner riduce il modulo.

## Moduli

## Fase 1 — Modello del linguaggio e metodo

### M01 — Nomi, oggetti, riferimenti
- **Aree**: A1, A2. Metodo: regole 6 e 7 (previsione, ipotesi).
- **Perché**: prima lacuna indicata dall'assessor. C1 e C2 "non lo so", L01 0 righe su 6, `sub.strip()` con il risultato scartato in S01, bug `if "grams" or "food" not in ...` vissuto come "assurdo". Senza questo modello tutto il resto resta imitazione. In Django lo stesso errore compare come default mutabile in una funzione o in un campo (`default=[]` invece di `default=list`) e come lista condivisa tra richieste.
- **Obiettivi**:
  - Prevede l'output di snippet con aliasing, copie e mutazione attraverso un argomento, e spiega ogni riga con il modello "nome → oggetto".
  - Distingue `is` da `==` e sa dire quando ciascuno è corretto, oltre l'abitudine di `is None`.
  - Riconosce e corregge un default mutabile e una struttura annidata costruita con `*`.
  - Sceglie tra copia superficiale e profonda motivando.
  - Dice quale valore di verità ha un oggetto e scompone un'espressione booleana con `or`, `and`, `not in`.
- **Teoria da introdurre**: nomi come etichette su oggetti (`id`, `is`); mutabile vs immutabile e cosa restituiscono i metodi di `str`; passaggio di argomenti per riferimento all'oggetto; `copy` e `deepcopy`; truthiness e precedenza degli operatori booleani.
- **Esercizi previsti**:
  1. *Prevedi e verifica*: 8-10 snippet brevi; previsione scritta, poi REPL, poi spiegazione di ogni scarto. Focus: modello nome → oggetto.
  2. *La griglia condivisa*: un bug da trovare in una funzione che costruisce una matrice. Focus: aliasing in strutture annidate.
  3. *Il carrello che ricorda*: funzione con default mutabile che passa i test presi singolarmente e fallisce in sequenza. Focus: default valutati alla definizione.
  4. *Truthiness e condizioni composte*: riscrivere 5 condizioni sbagliate o ambigue, compresa quella di S01. Focus: valore di verità, precedenza.
  5. *Chi possiede il dato?* (design): una funzione riceve una lista e un dict dal chiamante; decidere se muta, copia o restituisce un oggetto nuovo, e scrivere il contratto. Focus: proprietà dei dati tra chiamante e chiamato.
- **Focus di design**: decidere e dichiarare se una funzione modifica i propri argomenti. È la prima scelta di design con un'alternativa reale e si può motivare in tre righe.
- **Criterio di uscita**: su un set nuovo di 10 snippet prevede correttamente almeno 8 output, con spiegazione scritta per ciascuno, senza REPL e senza indizi; corregge un default mutabile e un aliasing in codice non suo spiegando il meccanismo.
- **Risorse**: Tutorial ufficiale, sezioni su liste e su "Default Argument Values"; Language Reference, "Data model" (prime tre sezioni: objects, values, types); modulo `copy`; "Programming FAQ" nella documentazione ufficiale (default condivisi, liste multidimensionali); Fluent Python 2ed, capitolo "Object References, Mutability, and Recycling"; pythontutor.com per visualizzare i riferimenti.

### M02 — Dalla specifica ai test: casi limite, pytest, traceback
- **Aree**: K5, K4, H1, J4. Metodo: regole 2, 3, 6, 8.
- **Perché**: terza lacuna indicata dall'assessor e pattern 1 del test ("test verdi = finito"): 6/19 e 7/14 nei nascosti con sicurezza dichiarata 4/5. Regole della consegna non implementate (formato `index <i>`, timestamp decrescenti). Aiuto necessario per leggere un `AssertionError`, un traceback concatenato, per usare `-k`. Va fatto subito perché da qui in poi ogni modulo chiede a Nick di scrivere i propri test.
- **Obiettivi**:
  - Da una consegna estrae un elenco numerato di regole e, con la griglia fissa, un elenco di casi limite.
  - Scrive test pytest propri, uno per regola, con nomi che dicono il comportamento atteso.
  - Legge da solo un traceback (anche concatenato) e l'output di un test fallito, e indica la riga da cui partire.
  - Usa `pytest -k`, `-x`, `-q` e `breakpoint()` al posto di `print`.
  - Valida gli input al confine, compresi `bool` come numero e infinito/NaN.
- **Teoria da introdurre**: struttura di un test (arrange, act, assert) e `pytest.raises`; anatomia di un traceback; griglia dei casi limite; `bool` sottoclasse di `int`, `math.isfinite`; differenza tra "il test passa" e "la regola è coperta".
- **Esercizi previsti**:
  1. *Leggi il traceback*: 5 traceback e output di pytest già prodotti; per ciascuno scrivere causa e prima riga da guardare, senza eseguire nulla. Focus: J4.
  2. *Solo l'elenco*: una consegna di 8 regole; si consegnano soltanto regole numerate e casi limite, niente codice. Focus: leggere la consegna come specifica.
  3. *Test prima*: per una funzione già implementata e con 3 bug, scrivere i test che li fanno emergere a partire dalla specifica. Focus: H1, K5.
  4. *Validazione al confine*: funzione piccola di aggregazione con regole sul formato del messaggio d'errore (variante di S01, dati diversi). Focus: K4, valori speciali, rispetto letterale della specifica.
  5. *Quanti ne passo?*: prima dei test nascosti Nick dichiara quanti ne passerà e quali regole ritiene non coperte; poi confronto. Focus: calibrazione.
- **Focus di design**: dove mettere la validazione (una sola volta al confine o sparsa nel calcolo) e che informazione deve portare il messaggio d'errore per chi lo legge.
- **Criterio di uscita**: su un esercizio nuovo consegna elenco di regole, casi limite e test propri prima del codice; passa almeno l'80% dei test nascosti; lo scarto tra test nascosti previsti e ottenuti è al massimo del 20%; nessun indizio per leggere traceback o output di pytest.
- **Risorse**: documentazione pytest, "Get Started" e "How to write and report assertions in tests"; Tutorial ufficiale, "Errors and Exceptions" (solo la lettura dei traceback, il resto è in M06); modulo `pdb`, sezione su `breakpoint()`; modulo `math` (`isfinite`, `isnan`).

### M03 — Tipi built-in, costi, `collections`
- **Aree**: A4, G1, primo contatto con J5 (`timeit`).
- **Perché**: C3 "non lo so su tutta la linea". In S01 una lista di tuple più un dict di indici tenuti in parallelo al posto di un solo dict, e `IndexError` usata per "chiave assente". `defaultdict` e `Counter` non usati dove erano la scelta naturale.
- **Obiettivi**:
  - Sceglie tra list, tuple, dict, set motivando con le operazioni necessarie e il loro costo.
  - Sa quali oggetti possono essere chiavi di dict o elementi di set e perché.
  - Usa `defaultdict`, `Counter`, `deque` quando semplificano il codice e sa dire quando non servono.
  - Verifica con `timeit` un'affermazione sul costo invece di fidarsi dell'intuito.
- **Teoria da introdurre**: complessità delle operazioni principali (appartenenza, inserimento, rimozione in testa); hashabilità; ordine di inserimento nei dict; `dict.get`, `setdefault`, `defaultdict`, `Counter`; `deque` contro `list.pop(0)`.
- **Esercizi previsti**:
  1. *Quale struttura?*: 6 scenari brevi; scegliere e motivare per iscritto, poi misurare due di essi con `timeit`. Focus: A4, ipotesi e verifica.
  2. *Una struttura sola*: riscrivere un'aggregazione che tiene due strutture parallele. Focus: eliminare lo stato duplicato.
  3. *Conteggi e gruppi*: tre piccole funzioni di conteggio e raggruppamento su dati tipo log. Focus: `Counter`, `defaultdict`.
  4. *Deduplicare mantenendo l'ordine* (design): la consegna lascia aperto cosa significa "duplicato" e quale occorrenza tenere; vanno decise e scritte. Focus: K5 su duplicati e ordine.
- **Focus di design**: la struttura dati come decisione che determina la semplicità del codice; due strutture che devono restare sincronizzate sono un rischio.
- **Criterio di uscita**: in un esercizio nuovo la nota di design motiva la struttura scelta con le operazioni e i costi, il codice non contiene strutture parallele né eccezioni usate per l'assenza di una chiave, e i test nascosti su duplicati, ordine e input vuoto passano.
- **Risorse**: Tutorial ufficiale, "Data Structures"; documentazione di `collections`; wiki Python "TimeComplexity"; modulo `timeit`; Fluent Python 2ed, capitoli "An Array of Sequences" e "Dictionaries and Sets"; sorgente `Lib/collections/__init__.py` (classe `Counter`).

### M04 — Controllo di flusso idiomatico
- **Aree**: A5, rinforzo di K1.
- **Perché**: contatore manuale al posto di `enumerate`, nessuna comprehension, unpacking con `*` e walrus dichiarati "non lo so" in L02, un ciclo senza effetto in S01.
- **Obiettivi**:
  - Usa `enumerate`, `zip`, unpacking (anche con `*`) al posto di indici manuali.
  - Scrive comprehension di list, dict e set e sa quando un ciclo esplicito è più leggibile.
  - Legge `match` e walrus in codice altrui e sa dire quando non usarli.
  - Usa `sorted` con `key`, `any`, `all`, `min`/`max` con `default`.
- **Teoria da introdurre**: comprehension e loro limiti di leggibilità; unpacking e `zip(strict=True)`; `any`/`all` su sequenze vuote; `match` strutturale in breve; walrus.
- **Esercizi previsti**:
  1. *Riscrivi senza indici*: 6 cicli da rendere idiomatici, con una riga sul perché la nuova versione è migliore o no. Focus: A5.
  2. *Comprehension o ciclo?*: 4 casi in cui decidere; almeno uno in cui la risposta giusta è il ciclo. Focus: leggibilità come criterio.
  3. *Tabella da due liste*: funzione che combina sequenze di lunghezza diversa; la specifica dice cosa fare in caso di disallineamento. Focus: `zip`, input vuoto, K5.
  4. *Rinomina* (design): codice funzionante con nomi per tipo (`lista`, `valore`, `d`); rinominare per ruolo senza cambiare il comportamento, con i test come rete. Focus: K1.
- **Focus di design**: leggibilità come trade-off esplicito, non come gusto; il nome di una funzione come promessa su ciò che restituisce.
- **Criterio di uscita**: in una consegna nuova non compaiono indici manuali né contatori quando esiste un costrutto diretto, ogni nome descrive il ruolo, e Nick spiega per iscritto una scelta "ciclo invece di comprehension" o viceversa.
- **Risorse**: Tutorial ufficiale, "More Control Flow Tools" e "Looping Techniques"; PEP 8 (sezione sui nomi); PEP 636 (tutorial su `match`); documentazione delle funzioni built-in.

### M05 — Funzioni: firme, scope, closures
- **Aree**: B1, A3, B2, primo uso di F1 (annotazioni sulle firme, obbligatorie da qui in poi).
- **Perché**: B1 autovalutata 3 e osservata 1 (positional-only "non saprei", flag booleano posizionale `send=True` mantenuto nel redesign di L08). C4: regola sullo scope enunciata falsa. L02: closure e lambda in comprehension "non lo so". Prerequisito diretto dei decoratori (M11).
- **Obiettivi**:
  - Progetta una firma con keyword-only e positional-only motivando; elimina i flag booleani posizionali.
  - Spiega la regola LEGB e prevede il risultato di snippet con `global`, `nonlocal` e variabili libere.
  - Scrive una closure che mantiene stato e spiega cosa viene catturato (la variabile, non il valore).
  - Passa e restituisce funzioni; sa quando una `lambda` peggiora la leggibilità.
  - Annota parametri e ritorno di ogni funzione che scrive.
- **Teoria da introdurre**: `*args`, `**kwargs`, `/` e `*` nella firma; LEGB e momento in cui un nome diventa locale; closure e late binding; funzioni come oggetti (`key=`, callback); annotazioni di base.
- **Esercizi previsti**:
  1. *Prevedi lo scope*: 8 snippet con previsione scritta, compreso l'`UnboundLocalError` di C4. Focus: A3.
  2. *Ripara la firma*: tre funzioni con firme ambigue (flag booleani, molti posizionali) da riprogettare senza rompere i chiamanti indicati. Focus: B1.
  3. *Contatore e accumulatore*: due closure piccole con stato. Focus: `nonlocal`, cosa cattura una closure.
  4. *Il bug delle lambda nel ciclo*: trovare, spiegare e correggere il late binding. Focus: A3, B2.
  5. *Strategia come funzione* (design): un calcolo con una regola variabile (ad esempio arrotondamento o sconto); decidere tra parametro funzione, flag, o più funzioni, e motivare. Focus: B2, K6.
- **Focus di design**: la firma come interfaccia: cosa è obbligatorio, cosa ha un default, cosa il chiamante deve nominare. In Django corrisponde a progettare le funzioni di servizio chiamate dalle view.
- **Criterio di uscita**: prevede correttamente almeno 7 snippet su 8 su scope e closures con spiegazione; scrive senza indizi una closure con stato che passa i test nascosti; in una revisione di firme altrui individua e motiva almeno 3 problemi su 4.
- **Risorse**: Tutorial ufficiale, "More on Defining Functions"; Language Reference, "Naming and binding"; PEP 3102 e PEP 570; Programming FAQ (lambda definite in un ciclo); Fluent Python 2ed, capitolo "Functions as First-Class Objects".

## Fase 2 — Eccezioni, oggetti, iterazione

### M06 — Eccezioni
- **Aree**: E1, rinforzo di K4 e J4.
- **Perché**: `raise from` sconosciuto (C12); in L03 la correzione proposta cattura `Exception` e fa `print(e)`; in S01 eccezioni come flusso di controllo ed eccezione originale sostituita perdendo la causa; L05 non risolto.
- **Obiettivi**:
  - Prevede il flusso di `try`/`except`/`else`/`finally` riga per riga.
  - Definisce una piccola gerarchia di eccezioni proprie e sceglie da quale built-in derivare.
  - Usa `raise ... from` per conservare la causa e sa quando sopprimerla.
  - Decide dove catturare e dove lasciar propagare, motivando.
- **Teoria da introdurre**: gerarchia delle eccezioni built-in; `else` e `finally`; concatenazione (`__cause__`, `__context__`); eccezioni proprie; regola "cattura solo ciò che sai gestire, nel punto in cui puoi farlo".
- **Esercizi previsti**:
  1. *Prevedi il flusso*: 6 snippet in stile L05 con output riga per riga. Focus: E1.
  2. *Il `except Exception` che nasconde*: codice che inghiotte un bug; trovarlo e restringere la cattura. Focus: quando non catturare.
  3. *Errori di dominio*: per un parser piccolo, definire le eccezioni e conservare la causa originale. Focus: eccezioni proprie, `raise from`.
  4. *Chi gestisce cosa?* (design): tre livelli (lettura, validazione, chiamante); scrivere prima una tabella "errore → chi lo gestisce → cosa vede l'utente", poi il codice. Focus: confini, K4.
- **Focus di design**: il contratto d'errore di una funzione fa parte della sua interfaccia. In Django: quando sollevare `ValidationError`, quando un `Http404`, quando lasciar arrivare l'errore al middleware.
- **Criterio di uscita**: 5 snippet su 6 previsti correttamente; in un esercizio nuovo nessun `except` generico, la causa originale è conservata, ogni eccezione sollevata è coperta da un test di Nick, e la tabella degli errori è nella nota di design.
- **Risorse**: Tutorial ufficiale, "Errors and Exceptions"; Library Reference, "Built-in Exceptions" (albero della gerarchia); sorgente `django/core/exceptions.py`.

### M07 — Classi: attributi di classe e istanza, property, classmethod
- **Aree**: D1, D6.
- **Perché**: scarto di calibrazione più grande del test: autovalutazione 4 ("saprei insegnarlo"), osservato 1. C11 "non lo so", L01 0/6 compreso "Errore, non è definito items" per un attributo di classe, `@property` mai citata. Nick scrive classi ogni giorno in Django, dove campi e `Meta` sono attributi di classe: la familiarità con la sintassi copre l'assenza del meccanismo.
- **Obiettivi**:
  - Spiega la ricerca di un attributo (istanza, poi classe) e prevede snippet con attributi di classe mutabili condivisi.
  - Distingue lettura da assegnazione su `self.x` quando `x` esiste sulla classe.
  - Usa `@property` per un valore derivato o validato e sa quando è eccessiva.
  - Scrive un costruttore alternativo con `@classmethod` e sa quando `@staticmethod` è solo una funzione fuori posto.
- **Teoria da introdurre**: `__dict__` di istanza e di classe; ordine di ricerca degli attributi; attributi di classe mutabili; `property` (getter, setter); `classmethod` come costruttore alternativo.
- **Esercizi previsti**:
  1. *Prevedi L01, versione nuova*: 8 snippet su attributi di classe e istanza; previsione, verifica, spiegazione. Focus: D1.
  2. *Lo stato che trapela*: una classe con una lista come attributo di classe che contamina le istanze; trovare e correggere. Focus: D1, A2.
  3. *Property o metodo?*: una classe con tre valori derivati; decidere per ciascuno e motivare. Focus: `@property`.
  4. *Costruttori alternativi*: una classe creata da stringa e da dict, con validazione in un solo punto. Focus: D6, K4.
  5. *Serve una classe?* (design): tre problemi piccoli; per ciascuno decidere tra funzione, classe o dict, per iscritto, prima di scrivere codice. Focus: contrasto al riflesso "scrivo classi".
- **Focus di design**: quando una classe è giustificata (stato più invarianti) e quando è una funzione travestita. Collegamento Django: perché i campi di un Model stanno sulla classe e i valori sull'istanza.
- **Criterio di uscita**: almeno 7 snippet su 8 previsti correttamente con spiegazione; spiega per iscritto, con le sue parole e un esempio, la ricerca degli attributi; in un esercizio nuovo sceglie tra property e metodo motivando, e i test nascosti sullo stato condiviso tra istanze passano.
- **Risorse**: Tutorial ufficiale, "Classes" (in particolare "Class and Instance Variables"); documentazione di `property`, `classmethod`, `staticmethod`; "Descriptor HowTo Guide" (solo l'introduzione); sorgente `django/utils/functional.py` (`cached_property`).

### M08 — Metodi speciali
- **Aree**: D2.
- **Perché**: C9 "non lo so", L04 "qui non so nulla", S04 (`Money`) non tentato. Serve per iteratori (M09), context manager (M12), dataclasses (M13).
- **Obiettivi**:
  - Implementa `__repr__` e `__str__` e sa a chi serve ciascuno.
  - Implementa `__eq__` e `__hash__` coerenti e spiega cosa succede in un set o come chiave di dict se non lo sono.
  - Implementa l'ordinamento (`__lt__`, `functools.total_ordering`) e restituisce `NotImplemented` quando il tipo non è supportato.
  - Implementa il protocollo dei contenitori (`__len__`, `__contains__`, `__getitem__`).
- **Teoria da introdurre**: il data model come insieme di protocolli; contratto `__eq__`/`__hash__`; `NotImplemented` contro `NotImplementedError`; operatori riflessi; duck typing.
- **Esercizi previsti**:
  1. *Un `__repr__` utile*: per due classi date, con criterio "leggendolo nel log capisco l'oggetto". Focus: D2.
  2. *Uguali ma non nel set*: bug da trovare su `__eq__` senza `__hash__`. Focus: contratto di hash.
  3. *Versione ordinabile*: classe piccola per numeri di versione, con confronto e ordinamento. Focus: `__lt__`, tipi estranei.
  4. *Un contenitore su misura*: classe che si comporta come una collezione in sola lettura. Focus: protocollo dei contenitori.
  5. *Uguaglianza: per valore o per identità?* (design): due entità (una con id, una senza); decidere e motivare cosa significa "uguale" per ciascuna. Focus: oggetti valore contro entità, come nei Model di Django.
- **Focus di design**: definire cosa significa uguaglianza per un tipo prima di scrivere il metodo.
- **Criterio di uscita**: implementa senza indizi una classe con `__repr__`, `__eq__`, `__hash__` e ordinamento che passa i test nascosti su set, dict, `sorted` e confronto con tipi estranei; spiega per iscritto perché una classe mutabile con `__eq__` non dovrebbe essere hashabile.
- **Risorse**: Language Reference, "Data model", sezione "Special method names"; Fluent Python 2ed, capitoli "The Python Data Model" e "A Pythonic Object"; sorgente `Lib/fractions.py` come esempio di tipo numerico completo.

### M09 — Iteratori e generatori
- **Aree**: C1, C2.
- **Perché**: seconda lacuna indicata dall'assessor. L02: prevede 30 anche per il secondo `sum` su un generatore consumato; L03: non vede il generatore consumato, il bug più grave dello snippet; S02: nessun `yield`, lista intera in memoria, i test su stream infiniti non terminano, tensione tra validazione immediata e laziness non affrontata. In Django è il modello dietro ai QuerySet lazy.
- **Obiettivi**:
  - Distingue iterabile da iteratore e prevede cosa succede a un iteratore già consumato.
  - Scrive una classe iteratore con `__iter__` e `__next__`, poi la stessa cosa con una funzione generatore.
  - Scrive generatori che elaborano uno stream senza caricarlo e che funzionano su input infinito.
  - Sa quando il corpo di un generatore viene eseguito e risolve il problema "validare gli argomenti alla chiamata".
  - Usa `yield from` e le generator expression.
- **Teoria da introdurre**: protocollo di iterazione e cosa fa davvero un `for`; `StopIteration`; funzione generatore ed esecuzione sospesa; generator expression contro list comprehension; lazy contro eager e relativi costi.
- **Esercizi previsti**:
  1. *Prevedi l'esaurimento*: 8 snippet con previsione scritta, compresi quelli di L02. Focus: C1.
  2. *Il `for` a mano*: riscrivere un ciclo `for` con `iter` e `next`, poi una classe iteratore piccola. Focus: protocollo.
  3. *Lettura a blocchi*: generatore che raggruppa uno stream in blocchi di dimensione fissa; deve funzionare su input infinito e vuoto. Focus: C2.
  4. *Validare subito, produrre dopo*: funzione lazy che deve sollevare l'errore sugli argomenti alla chiamata e non al primo `next`. Focus: la tensione ignorata in S02.
  5. *Sessioni, di nuovo* (design): problema analogo a S02 con dati diversi; la nota di design deve dire cosa viene tenuto in memoria e per quanto. Focus: stato minimo in un generatore, timestamp non ordinati.
  6. *Lista o iteratore?*: tre API; decidere cosa restituire e motivare con ciò che serve al chiamante. Focus: trade-off lazy/eager.
- **Focus di design**: cosa restituire da una funzione (lista, iteratore, generatore) è una decisione di interfaccia con conseguenze su memoria, riutilizzo e momento in cui emergono gli errori.
- **Criterio di uscita**: almeno 7 snippet su 8 previsti; scrive senza indizi un generatore che passa test nascosti su stream infinito, input vuoto, input già consumato ed errore sugli argomenti alla chiamata; nella nota di design indica lo stato tenuto in memoria.
- **Risorse**: Tutorial ufficiale, "Iterators", "Generators", "Generator Expressions"; "Functional Programming HOWTO" (sezioni su iteratori e generatori); PEP 255; Fluent Python 2ed, capitolo "Iterators, Generators, and Classic Coroutines"; sorgente `django/db/models/query.py` (`QuerySet.__iter__` e la cache dei risultati) e documentazione Django "When QuerySets are evaluated".

### M10 — `itertools` e pipeline lazy
- **Aree**: C3, rinforzo di C2, J5.
- **Perché**: C8 "non lo so". Modulo corto che fissa M09 componendo generatori.
- **Obiettivi**:
  - Usa `chain`, `islice`, `groupby`, `accumulate`, `product` nei casi adatti.
  - Conosce le trappole di `groupby` (input non ordinato, gruppi consumati) e di `tee`.
  - Compone una pipeline di 3-4 stadi lazy e ne misura la memoria rispetto alla versione a liste.
- **Teoria da introdurre**: `itertools` come blocchi componibili; `groupby` richiede input ordinato per chiave; `islice` su stream infiniti; `itertools.batched` e `pairwise`; misurare con `tracemalloc` o `timeit`.
- **Esercizi previsti**:
  1. *Sostituisci il ciclo*: 5 cicli da riscrivere con uno strumento di `itertools`, quando migliora. Focus: C3.
  2. *Il `groupby` che perde gruppi*: bug da trovare. Focus: precondizioni di `groupby`.
  3. *Pipeline su un log grande*: lettura, filtro, raggruppamento, aggregazione, tutto lazy; misura contro la versione eager. Focus: C2, J5.
  4. *Dove materializzare?* (design): una pipeline in cui uno stadio ha bisogno di due passate; decidere dove creare la lista e motivare. Focus: trade-off.
- **Focus di design**: scegliere il punto in cui una pipeline lazy deve diventare concreta.
- **Criterio di uscita**: costruisce senza indizi una pipeline lazy a più stadi che passa i test nascosti su input vuoto e non ordinato, e riporta nella consegna una misura a sostegno della scelta lazy/eager.
- **Risorse**: documentazione di `itertools` (comprese le "recipes" in fondo alla pagina); modulo `tracemalloc`.

## Fase 3 — Strumenti per Django e capstone

### M11 — Decoratori e `functools`
- **Aree**: B3, B4.
- **Perché**: L07: capisce un decoratore semplice ma sbaglia `__name__` e non conosce `__doc__`; `wraps` e `lru_cache` "non lo so"; S03 (`ttl-cache`) saltato con "non so fare né un decoratore né una cache". Nick usa decoratori ogni giorno in Django (`@login_required`, `@transaction.atomic`) senza sapere come funzionano.
- **Obiettivi**:
  - Scrive un decoratore semplice con `functools.wraps` e spiega cosa si perde senza.
  - Scrive un decoratore con argomenti e spiega i tre livelli di funzione.
  - Scrive un decoratore con stato (conteggio, cache) e indica dove vive lo stato.
  - Usa `lru_cache`/`cache`, `partial`, `cached_property`, e conosce il problema di `lru_cache` sui metodi e con argomenti non hashabili.
- **Teoria da introdurre**: `@` come chiamata di funzione; `wraps` e metadati; decoratori con argomenti; cache: chiave, invalidazione, dimensione; `partial`.
- **Esercizi previsti**:
  1. *Decoratore a mano*: applicare un decoratore senza `@`, poi con; prevedere `__name__` e `__doc__`. Focus: B3.
  2. *Misura del tempo*: decoratore di timing con `wraps`. Focus: decoratore semplice.
  3. *Retry con parametri*: decoratore con argomenti (tentativi, eccezioni da ritentare). Focus: tre livelli, E1.
  4. *Cache con scadenza*: il problema di S03 ripreso da capo; l'orologio deve poter essere sostituito nei test. Focus: stato, dipendenza iniettata, H4.
  5. *Quando la cache è un bug* (design): tre funzioni; decidere per quali la cache è sicura e perché no per le altre (argomenti mutabili, dati che cambiano, metodi). Focus: B4, K3.
- **Focus di design**: un decoratore nasconde comportamento: decidere cosa è giusto nascondere; rendere esplicita la dipendenza dal tempo.
- **Criterio di uscita**: scrive senza indizi un decoratore con argomenti e stato che passa i test nascosti, compresi metadati conservati, argomenti keyword, eccezioni non messe in cache e scadenza con orologio simulato. L'esercizio 4 non può essere saltato: vale la regola del tentativo minimo.
- **Risorse**: documentazione di `functools`; Fluent Python 2ed, capitolo "Decorators and Closures"; sorgente `Lib/functools.py` (`wraps`, `lru_cache`); sorgenti `django/contrib/auth/decorators.py` e `django/utils/functional.py`.

### M12 — Context manager e gestione delle risorse
- **Aree**: E2, E3, G2.
- **Perché**: C13 "non so cosa sia un context manager" pur usando `with open`; in L08 la connessione SMTP senza cleanup non è stata notata; in L03 non nota encoding né durata dell'apertura del file. Area a 0 necessaria per il capstone e per capire `transaction.atomic` in Django.
- **Obiettivi**:
  - Spiega cosa garantisce `with` e in quale ordine vengono chiamati `__enter__` e `__exit__`, anche con eccezione.
  - Scrive un context manager come classe e con `contextlib.contextmanager`.
  - Decide se `__exit__` deve sopprimere o propagare un'eccezione.
  - Usa `pathlib` e apre i file con encoding esplicito; gestisce più risorse con `ExitStack`.
- **Teoria da introdurre**: protocollo `__enter__`/`__exit__` e valore di ritorno di `__exit__`; `@contextmanager` e `try`/`finally` attorno a `yield`; `ExitStack`; `pathlib.Path`; encoding e modalità di apertura.
- **Esercizi previsti**:
  1. *Prevedi l'ordine*: 6 snippet con stampa di ingresso, uscita, eccezione. Focus: E2.
  2. *Cronometro*: context manager come classe e poi con `@contextmanager`. Focus: le due forme.
  3. *Modifica temporanea*: context manager che cambia uno stato e lo ripristina anche in caso di errore. Focus: cleanup garantito.
  4. *Scrittura atomica su file*: scrivere su un file temporaneo e sostituire solo se tutto va bene; `pathlib`, encoding esplicito. Focus: E3, G2.
  5. *Chi chiude cosa?* (design): un importatore che apre N file e una connessione; decidere chi possiede ogni risorsa e per quanto resta aperta. Focus: proprietà delle risorse, `ExitStack`.
- **Focus di design**: proprietà e durata di vita di una risorsa; tenere aperto il minimo necessario.
- **Criterio di uscita**: scrive senza indizi un context manager con gestione delle eccezioni che passa i test nascosti (eccezione nel blocco, eccezione in ingresso, uso annidato, riuso), e spiega per iscritto perché `transaction.atomic` può essere usato sia come decoratore sia con `with`.
- **Risorse**: Language Reference, "The with statement"; documentazione di `contextlib` e `pathlib`; PEP 343; sorgente `Lib/contextlib.py` (`_GeneratorContextManager`, `ContextDecorator`); sorgente `django/db/transaction.py` (`Atomic`).

### M13 — `dataclasses`, `enum`, immutabilità
- **Aree**: D3, K3.
- **Perché**: C10 "non li ho mai sentiti questi nomi"; K3 a 0: in L08 lo stato globale è letto come "manca un DB vero" e il redesign aggiunge stato. Prerequisito del capstone e punto di contatto con gli Schema di Django Ninja.
- **Obiettivi**:
  - Sostituisce dict e tuple "nudi" con dataclass e sa cosa viene generato.
  - Usa `frozen`, `field(default_factory=...)`, `__post_init__` per gli invarianti.
  - Usa `Enum` al posto di stringhe e costanti sparse.
  - Individua lo stato mutabile condiviso in un programma e lo riduce.
- **Teoria da introdurre**: metodi generati da `@dataclass`; `frozen` e hashabilità; `default_factory` (collegamento a M01); `Enum` e `StrEnum`; oggetti valore immutabili contro entità mutabili.
- **Esercizi previsti**:
  1. *Da dict a dataclass*: convertire un modulo che passa dict tra funzioni; elencare gli errori che diventano impossibili. Focus: D3.
  2. *Invarianti in `__post_init__`*: tipo con vincoli (intervallo, quantità non negativa). Focus: validazione alla costruzione, K4.
  3. *Stati con `Enum`*: sostituire stringhe magiche in una piccola macchina a stati. Focus: `enum`.
  4. *Via lo stato globale*: rifattorizzare un modulo con variabili globali mutabili. Focus: K3.
  5. *Frozen o no?* (design): tre tipi; decidere per ciascuno e motivare con chi li modifica e chi li condivide. Focus: immutabilità come scelta.
- **Focus di design**: rendere impossibili gli stati non validi; scegliere l'immutabilità quando un oggetto è condiviso.
- **Criterio di uscita**: modella senza indizi un piccolo dominio con dataclass ed enum che passa i test nascosti su invarianti, uguaglianza, hashabilità e default non condivisi; elimina lo stato globale da un modulo dato senza cambiare il comportamento verificato dai test.
- **Risorse**: documentazione di `dataclasses` ed `enum`; "Enum HOWTO"; PEP 557; Fluent Python 2ed, capitolo "Data Class Builders".

### M14 — Type hints e type checker
- **Aree**: F1, F2, F3.
- **Perché**: F1 a 1, F2 a 0, F3 non misurato con un dato indiretto negativo (non ha saputo interpretare un avviso dell'IDE). Django Ninja è costruito sulle annotazioni: senza questo modulo la track Django riparte dall'imitazione.
- **Obiettivi**:
  - Annota funzioni e classi con collezioni generiche, `| None`, `Literal`, `TypedDict`.
  - Esegue pyright o mypy su un modulo e corregge gli errori capendoli, senza `# type: ignore` di comodo.
  - Scrive una funzione generica con `TypeVar` e un `Protocol` semplice.
  - Sa cosa i type hints non garantiscono a runtime.
- **Teoria da introdurre**: annotazioni e controllo statico; restringimento dei tipi (`is None`, `isinstance`); `TypedDict` e `Literal`; generics; `Protocol` e tipizzazione strutturale.
- **Esercizi previsti**:
  1. *Annota e fai passare il checker*: un modulo delle fasi precedenti da annotare fino a zero errori. Focus: F1, F3.
  2. *Leggi l'errore*: 8 errori di type checker da spiegare e correggere. Focus: F3.
  3. *Il `None` dimenticato*: codice che il checker segnala e che ha un bug reale. Focus: restringimento, K5.
  4. *Funzione generica*: una utility che conserva il tipo degli elementi. Focus: `TypeVar`.
  5. *Quanto tipizzare?* (design): un confine con dati esterni; decidere tra `dict[str, Any]`, `TypedDict`, dataclass, e motivare. Focus: F2, K4.
- **Focus di design**: i tipi come documentazione verificabile dei confini; dove `Any` è accettabile.
- **Criterio di uscita**: un modulo di almeno 150 righe scritto da Nick passa il type checker in modalità strict senza ignore non motivati; spiega correttamente 7 errori su 8; da qui in poi il type checker pulito è condizione di consegna.
- **Risorse**: documentazione di `typing`; documentazione di mypy ("Type hints cheat sheet") o di pyright; PEP 484 e PEP 544; Fluent Python 2ed, capitolo "Type Hints in Functions".

### M15 — Importi e serializzazione: `decimal`, `json`, `csv`
- **Aree**: G4, G6, rinforzo di D2 e K4.
- **Perché**: C14 "non ne ho idea"; in L03 non cita `float` per gli importi né il modulo `csv`, e il controllo proposto sulle virgole è sbagliato; S04 (`Money`) non tentato. Prerequisito del capstone (valori nutrizionali, quantità) e di qualunque codice Django che tocchi importi (`DecimalField`).
- **Obiettivi**:
  - Spiega perché `float` non va usato per gli importi e mostra un caso che fallisce.
  - Usa `Decimal` con costruzione da stringa, `quantize` e una regola di arrotondamento scelta.
  - Legge e scrive CSV con il modulo `csv` gestendo virgolette, righe vuote, encoding.
  - Serializza in JSON tipi non nativi (`Decimal`, date, dataclass) e li ricostruisce.
  - Sa quando una regex è adatta al parsing e quando no.
- **Teoria da introdurre**: rappresentazione binaria dei float; `Decimal`, contesto e arrotondamento; `csv.DictReader` e dialetti; `json` con `default` e limiti del formato; regex di base (`re.fullmatch`, gruppi) e alternative.
- **Esercizi previsti**:
  1. *Il centesimo che sparisce*: trovare e correggere errori di arrotondamento in un calcolo con float. Focus: `decimal`.
  2. *Dividere un importo*: ripartire una cifra in N parti senza perdere centesimi; la regola per il resto va decisa. Focus: K5, design.
  3. *`Money`*: il problema di S04 ripreso da capo come oggetto valore (valuta, aritmetica, confronto). Focus: D2, D3, invarianti.
  4. *CSV sporco*: importare righe con virgolette, campi mancanti, separatori nei valori; errori raccolti e non al primo fallimento. Focus: `csv`, E1.
  5. *Andata e ritorno in JSON*: serializzare e ricostruire un oggetto con `Decimal` e date. Focus: `json`, perdita di informazione.
  6. *Regex o no?*: tre formati da validare; scegliere lo strumento per ciascuno e motivare. Focus: G6.
- **Focus di design**: scegliere e documentare la regola di arrotondamento; decidere cosa fare delle righe non valide (fermarsi, saltare, raccogliere).
- **Criterio di uscita**: implementa senza indizi un oggetto valore per gli importi che passa i test nascosti (aritmetica, valute diverse, arrotondamento, hashabilità, confronto con tipi estranei), e un importatore CSV che passa i test su input malformati. L'esercizio 3 non può essere saltato.
- **Risorse**: documentazione di `decimal` (compresa la FAQ in fondo), `csv`, `json`, `re`; "Regular Expression HOWTO"; Tutorial ufficiale, "Floating-Point Arithmetic: Issues and Limitations".

### M16 — `datetime` e `zoneinfo`
- **Aree**: G3.
- **Perché**: C15 "non lo so"; L06: `day_bounds` non capita, confronto naive/aware non visto. In Django con `USE_TZ = True` questi errori sono bug reali in produzione; nel capstone il "giorno" di un utente dipende dal suo fuso.
- **Obiettivi**:
  - Distingue datetime naive e aware e prevede cosa succede a confrontarli.
  - Converte tra fusi con `zoneinfo` e conserva UTC come formato interno.
  - Calcola i confini di un giorno locale e gestisce i giorni di cambio dell'ora.
  - Rende testabile il codice che dipende da "adesso".
- **Teoria da introdurre**: naive contro aware; UTC come riferimento e conversione ai bordi; `ZoneInfo`, `astimezone`, `replace` e la differenza tra i due; ora legale: ore inesistenti e ripetute; aritmetica con `timedelta`.
- **Esercizi previsti**:
  1. *Prevedi L06, versione nuova*: 6 snippet su confronto, conversione, aritmetica. Focus: G3.
  2. *Il giorno dell'utente*: dato un istante UTC e un fuso, calcolare i confini del giorno locale. Focus: conversioni.
  3. *La notte del cambio dell'ora*: funzione di durata e di ricorrenza giornaliera che attraversa il cambio. Focus: K5.
  4. *"Adesso" come parametro*: rifattorizzare una funzione che chiama `datetime.now()` al suo interno. Focus: H4.
  5. *Cosa salvo?* (design): per tre dati (istante di un pasto, data di nascita, promemoria ricorrente alle 8:00) decidere cosa memorizzare e motivare. Focus: modellazione del tempo.
- **Focus di design**: distinguere istante, data civile e ora locale ricorrente; il tempo come dipendenza esplicita.
- **Criterio di uscita**: 5 snippet su 6 previsti; implementa senza indizi una funzione sui confini del giorno locale che passa i test nascosti nei giorni di cambio dell'ora e su fusi con offset non intero; nessuna chiamata diretta a `now()` nella logica.
- **Risorse**: documentazione di `datetime` (sezione "Aware and Naive Objects") e `zoneinfo`; PEP 615; documentazione Django "Time zones"; sorgente `django/utils/timezone.py`.

## Fase 4 — Design, test, progetto

### M17 — Ereditarietà, MRO, `super()`, mixin
- **Aree**: D4.
- **Perché**: autovalutazione 4, osservato 2. Usa l'ereditarietà singola (L08) ma senza alcuna chiamata a `super()`; C16 sbagliata; MRO, `super()` cooperativo e mixin a 0. Le class-based view di Django sono catene di mixin: Nick le usa senza poter prevedere quale metodo viene chiamato.
- **Obiettivi**:
  - Prevede l'MRO di una gerarchia con ereditarietà multipla e lo verifica con `__mro__`.
  - Spiega che `super()` segue l'MRO e non "la classe madre", e scrive `__init__` cooperativi.
  - Scrive un mixin piccolo e ne dichiara le aspettative sulla classe ospite.
  - Riconosce quando l'ereditarietà viola la sostituibilità.
- **Teoria da introdurre**: MRO e linearizzazione C3 a livello operativo; `super()` cooperativo e firme con `**kwargs`; mixin come comportamento senza stato proprio; principio di sostituzione; override e metodi template.
- **Esercizi previsti**:
  1. *Prevedi l'MRO*: 6 gerarchie con previsione dell'ordine e dell'output, compresa quella di C16. Focus: D4.
  2. *Il `super()` mancante*: gerarchia in cui un `__init__` non viene mai chiamato; trovare e correggere. Focus: cooperazione.
  3. *Segui la chiamata in una CBV*: data una view con tre mixin, scrivere l'ordine dei metodi eseguiti leggendo il sorgente di Django, senza eseguirla. Focus: lettura di codice reale.
  4. *Mixin o funzione?* (design): un comportamento comune a tre classi; scegliere tra mixin, funzione, composizione, e motivare. Focus: K6.
- **Focus di design**: l'ereditarietà come accoppiamento forte; cosa promette una sottoclasse.
- **Criterio di uscita**: prevede correttamente 5 MRO su 6 con l'output; ricostruisce per iscritto la catena di chiamate di una class-based view con mixin; scrive una gerarchia cooperativa che passa i test nascosti sull'ordine di inizializzazione.
- **Risorse**: Tutorial ufficiale, "Multiple Inheritance"; documentazione di `super()`; "The Python 2.3 Method Resolution Order" (HOWTO nella documentazione ufficiale); Fluent Python 2ed, capitolo "Inheritance: For Better or for Worse"; sorgenti `django/views/generic/base.py` e `django/contrib/auth/mixins.py`.

### M18 — Composizione, `abc` e `Protocol`, quando astrarre
- **Aree**: D5, K6.
- **Perché**: unico segnale sopra la media del test: in L09 Nick individua da solo i due assi indipendenti e propone di passare il compressore al costruttore. Ma lo schizzo ha errori, `abc` e `Protocol` sono a 0 (C17), e in L08 introduce gerarchia più factory per due soli formati. I nomi dei pattern Java sono usati come soluzione senza verificare il problema. Il modulo trasforma l'intuizione in Python corretto e la disciplina con YAGNI.
- **Obiettivi**:
  - Traduce una diagnosi "due assi indipendenti" in codice Python funzionante per composizione.
  - Sceglie tra funzione passata come argomento, `Protocol` e classe astratta, motivando.
  - Scrive prima l'analisi "cosa varia, cosa resta, cosa non farei" e solo dopo la struttura.
  - Riconosce un'astrazione prematura e la rimuove.
- **Teoria da introdurre**: composizione e iniezione delle dipendenze dal costruttore; `abc.ABC` e `abstractmethod`; `Protocol` e duck typing verificato; in Python molti pattern sono una funzione o un dict; YAGNI e "regola del tre".
- **Esercizi previsti**:
  1. *Exporter, di nuovo*: il problema di L09 con dati diversi, fino a codice che passa i test. Focus: D5.
  2. *Tre modi per dire "interfaccia"*: lo stesso punto di estensione risolto con callable, `Protocol`, `ABC`; confronto scritto. Focus: abc contro Protocol.
  3. *Togli la factory*: codice sovra-ingegnerizzato in stile Java da semplificare senza perdere comportamento. Focus: K6, YAGNI.
  4. *Solo analisi*: un problema di design da consegnare senza classi né codice: cosa varia, quali decisioni sono reversibili, cosa non si fa adesso. Focus: analisi prima della struttura, la domanda D2 "cosa non faresti".
  5. *Nuovo requisito*: al codice dell'esercizio 1 arriva un requisito inatteso; misurare quante righe cambiano e commentarlo. Focus: verifica del design.
- **Focus di design**: tutto il modulo. La regola è: analisi scritta, alternativa scartata, poi il codice.
- **Criterio di uscita**: su un problema nuovo consegna un'analisi con almeno due alternative confrontate e una voce "non lo faccio perché", e un'implementazione per composizione che passa i test nascosti e assorbe un requisito aggiuntivo modificando un solo punto. Il reviewer non trova nomi di pattern usati senza il problema corrispondente.
- **Risorse**: documentazione di `abc` e di `typing.Protocol`; PEP 544 e PEP 3119; Fluent Python 2ed, capitoli "Interfaces, Protocols, and ABCs" e "Design Patterns with First-Class Functions"; sorgente `Lib/collections/abc.py`.

### M19 — Testing: fixture, parametrize, mock, codice testabile
- **Aree**: H2, H3, H4.
- **Perché**: H3 a 0 (C19b e D1: "come scelgo cosa può essere mockato non lo so"); in D1 confonde un doppio di test con un fallback di produzione; nel redesign di L08 nessuna dipendenza iniettata. H2 non misurato. È il modulo che precede il refactoring e il progetto finale.
- **Obiettivi**:
  - Usa fixture, `parametrize`, `tmp_path`, `monkeypatch`.
  - Decide cosa sostituire con un doppio (confini: rete, orologio, filesystem) e cosa no (logica propria).
  - Distingue fake, stub e mock e sceglie il più semplice che basta.
  - Riprogetta una funzione non testabile separando calcolo ed effetti.
- **Teoria da introdurre**: fixture e loro ambito; test parametrici; doppi di test e dove applicare `patch`; funzioni pure al centro ed effetti ai bordi; test fragili legati all'implementazione.
- **Esercizi previsti**:
  1. *Dieci test in uno*: riscrivere test ripetitivi con `parametrize` e fixture. Focus: H2.
  2. *File senza toccare il disco vero*: testare codice di I/O con `tmp_path`. Focus: H2.
  3. *Il client esterno*: testare un modulo che chiama un'API, prima con un fake scritto a mano, poi con `unittest.mock`; confronto scritto. Focus: H3.
  4. *Il test che non verifica niente*: tre test troppo mockati che passano anche con il codice rotto; trovarli e riscriverli. Focus: cosa non mockare.
  5. *Rendilo testabile* (design): funzione che legge, calcola, salva e invia; separare prima sulla carta, poi nel codice. Focus: H4, K2.
- **Focus di design**: la testabilità come conseguenza di dipendenze esplicite; il confine tra logica ed effetti.
- **Criterio di uscita**: per un modulo con dipendenze esterne scrive una suite che non usa rete, orologio reale o disco fuori da `tmp_path`, e che fallisce quando il reviewer introduce 5 mutazioni nel codice (almeno 4 rilevate su 5).
- **Risorse**: documentazione pytest ("How to use fixtures", "How to parametrize", "How to monkeypatch"); documentazione di `unittest.mock`, sezione "Where to patch".

### M20 — Moduli, package, strumenti, logging
- **Aree**: J1, J2, J3, G5.
- **Perché**: J1: la spiegazione dell'import circolare non descrive il meccanismo, directory di lavoro sbagliata con pytest; `.venv` non creata come da istruzioni. G5: C19a "non so rispondere". J3 non misurato, ma nei file consegnati c'erano import inutilizzati e `print` di debug.
- **Obiettivi**:
  - Spiega cosa succede all'esecuzione di un `import` e perché nasce un import circolare.
  - Struttura un package con `pyproject.toml`, dipendenze dichiarate e ambiente virtuale.
  - Configura ruff (lint e formato) e lo tiene pulito.
  - Configura `logging` una sola volta all'ingresso e usa logger per modulo con livelli sensati.
- **Teoria da introdurre**: `sys.modules`, `sys.path` ed esecuzione del modulo all'import; import assoluti e relativi, `__init__.py`, `__main__`; `pyproject.toml` e ambienti virtuali (uv o pip); gerarchia dei logger, handler, livelli; perché una libreria non configura il logging.
- **Esercizi previsti**:
  1. *Rompi e ripara un import circolare*: riprodurlo, spiegarlo passo per passo, risolverlo in due modi e confrontarli. Focus: J1.
  2. *Da script a package*: trasformare un file unico in un package installabile con test che girano da qualunque directory. Focus: J1, J2.
  3. *Zero avvisi*: configurare ruff e type checker sul package e portarli a zero. Focus: J3.
  4. *Dai `print` ai log*: sostituire i `print` di un modulo con logging; decidere i livelli e cosa non va mai scritto nei log. Focus: G5.
  5. *Chi dipende da chi?* (design): disegnare il grafo delle dipendenze di un package piccolo e proporre i confini tra moduli. Focus: K2, direzione delle dipendenze.
- **Focus di design**: confini tra moduli e direzione delle dipendenze. In Django: confini tra app e import tra `models`, `services`, `views`.
- **Criterio di uscita**: consegna un package installabile con `pyproject.toml`, ruff e type checker puliti, test eseguibili da qualunque directory, logging configurato in un solo punto; spiega per iscritto il meccanismo di un import circolare su un esempio nuovo.
- **Risorse**: Tutorial ufficiale, "Modules"; Language Reference, "The import system"; "Logging HOWTO" e "Logging Cookbook"; documentazione di ruff e di uv; Python Packaging User Guide (scrittura di `pyproject.toml`).

### M21 — Refactoring sicuro e separazione delle responsabilità
- **Aree**: K7, K2, K1.
- **Perché**: K7: in D2 una sola idea valida, nessun ordine dei passi, nessuna rete di sicurezza, nessun criterio di fine. K2: riconosce la funzione che fa troppe cose ma nel redesign di L08 rimette parsing, validazione, calcolo, salvataggio e invio in un'unica classe. K1: nomi `d`, `t`, `i` conservati e non segnalati.
- **Obiettivi**:
  - Prima di toccare codice esistente scrive i test di caratterizzazione che ne fissano il comportamento.
  - Pianifica un refactoring in passi piccoli, ciascuno con i test verdi, e dichiara un criterio di fine.
  - Separa parsing, validazione, calcolo ed effetti in unità con dipendenze esplicite.
  - Ordina i problemi di un codice per gravità e motiva l'ordine.
- **Teoria da introdurre**: test di caratterizzazione; passi di refactoring elementari (estrarre, rinominare, spostare, introdurre un parametro); accoppiamento e coesione; mantenere compatibilità durante lo spostamento; quando fermarsi.
- **Esercizi previsti**:
  1. *Fissa il comportamento*: scrivere test di caratterizzazione per una funzione legacy di 80 righe senza modificarla. Focus: rete di sicurezza.
  2. *Classifica i problemi*: per un codice dato, elenco dei problemi ordinato per gravità con motivazione; niente codice. Focus: analisi, K2.
  3. *Il piano prima*: piano di refactoring in passi numerati con criterio di fine, valutato prima dell'esecuzione. Focus: K7.
  4. *Esegui il piano*: refactoring di un elaboratore di ordini in stile L08, con i test verdi a ogni passo. Focus: K2, K1.
  5. *Sposta senza rompere*: spostare funzioni tra moduli mantenendo validi gli import dei chiamanti, come in D2. Focus: J1, compatibilità.
- **Focus di design**: sequenza e reversibilità dei cambiamenti; refactoring guidato da un obiettivo e non dal gusto.
- **Criterio di uscita**: su un codice legacy nuovo consegna test di caratterizzazione, piano in passi e risultato in cui ogni unità ha una sola responsabilità e dipendenze esplicite; i test nascosti di comportamento passano prima e dopo; il piano contiene un criterio di fine rispettato.
- **Risorse**: catalogo su refactoring.com; "Refactoring" di Martin Fowler (capitoli 1-3 e 6); "Working Effectively with Legacy Code" di Michael Feathers (capitoli sui test di caratterizzazione).

### M22 — Concorrenza: thread, processi, `asyncio`
- **Aree**: I1, I2, I3.
- **Perché**: C20 e L10 "questo argomento non lo so". Serve per le view async di Django e per React/Expo in modo indiretto (modello a eventi). È il modulo meno urgente: va fatto prima di affrontare l'async in Django, non prima di iniziare Django.
- **Obiettivi**:
  - Spiega cosa comporta il GIL e sceglie tra thread, processi e async in base al tipo di carico.
  - Usa `concurrent.futures` per parallelizzare lavoro di I/O e di CPU.
  - Scrive coroutine con `await`, `gather`, `TaskGroup`, timeout.
  - Riconosce una chiamata bloccante dentro codice async e sa quando async non serve.
- **Teoria da introdurre**: I/O-bound contro CPU-bound; GIL; executor e future; event loop, coroutine, task; cancellazione e timeout; race condition sullo stato condiviso.
- **Esercizi previsti**:
  1. *Misura prima*: stesso carico di I/O e di CPU in sequenza, con thread, con processi; previsione e misura. Focus: I1, I2.
  2. *Prevedi l'ordine*: 6 snippet `asyncio` con previsione dell'output, compreso L10. Focus: I3.
  3. *Scaricare in parallelo con un limite*: coroutine con concorrenza limitata, timeout ed errori parziali. Focus: I3, E1.
  4. *Il blocco nascosto*: codice async lento per una chiamata bloccante; trovarla e correggerla. Focus: I3.
  5. *Serve davvero?* (design): tre scenari Django; decidere tra sincrono, thread, async o coda di lavori, e motivare. Focus: trade-off.
- **Focus di design**: la concorrenza come costo da giustificare con una misura.
- **Criterio di uscita**: 5 snippet su 6 previsti; implementa senza indizi un downloader concorrente con limite, timeout e gestione degli errori parziali che passa i test nascosti; motiva per iscritto, con una misura, la scelta dello strumento.
- **Risorse**: documentazione di `concurrent.futures` e `asyncio` (sezione "Coroutines and Tasks"); Fluent Python 2ed, capitoli "Concurrency Models in Python" e "Asynchronous Programming"; documentazione Django "Asynchronous support".

### M23 — Progetto di sintesi: import di pasti
- **Aree**: integrazione di E, G, H, K; verifica su D3, C2, F.
- **Perché**: S05 (`meal-import`) era l'esercizio con la scelta di design ed è stato saltato: su quel punto il test non ha prodotto dati. Chiude il cerchio sull'evitamento e fa da ponte verso il capstone (app nutrizionale).
- **Obiettivi**:
  - Parte da una specifica lunga e produce regole numerate, casi limite, nota di design con alternative.
  - Realizza un importatore completo: lettura lazy, validazione al confine, modello con dataclass e `Decimal`, date aware, errori raccolti, risorse chiuse.
  - Consegna con test propri, type checker e linter puliti.
  - Dichiara prima dei test nascosti cosa passerà e cosa no.
- **Teoria da introdurre**: nessuna nuova. Solo integrazione.
- **Esercizi previsti**:
  1. *Specifica e design*: solo documenti: regole, casi limite, alternative, piano dei moduli. Valutato prima di scrivere codice. Focus: metodo completo.
  2. *Nucleo puro*: modello e regole di validazione e calcolo, senza I/O. Focus: K2, K3.
  3. *Bordi*: lettura dei file, report degli errori, logging. Focus: E, G.
  4. *Nuovo requisito*: un secondo formato di ingresso arrivato a progetto finito; misurare cosa cambia. Focus: K6, verifica del design.
  5. *Retrospettiva*: confronto scritto tra il design iniziale e quello finale, con le scelte che rifarebbe diversamente. Focus: motivazione delle scelte.
- **Focus di design**: tutto. È l'esercizio in cui la difficoltà è la progettazione e non la sintassi.
- **Criterio di uscita**: almeno l'85% dei test nascosti; scarto tra previsione e risultato entro il 10%; il secondo formato viene aggiunto senza modificare il nucleo; nota di design con almeno tre scelte motivate con alternativa. Questo modulo vale come prova finale pratica della track, insieme alla verifica finale dell'assessor.
- **Risorse**: `tracks/capstone/brief.md`; i propri esercizi di M09, M12, M13, M15, M16.

## Decisioni aperte (richiedono la scelta di Nick)
1. **Sequenza delle track.** Proposta: Django dopo la Fase 3 (circa settimana 12), in parallelo con la Fase 4 di Python. Alternative: (a) Django solo a track Python conclusa, più pulito ma Django slitta alla settimana 17; (b) Django dopo la Fase 2 (circa settimana 7), prima ma senza decoratori, context manager e type hints, cioè con il rischio di ripetere l'imitazione.
2. **Giorni a settimana.** Le stime usano 5 giorni. Con 6 giorni la track in sequenza scende a circa 14 settimane, ma con più rischio di calo di resa a fine settimana.
3. **Concorrenza (M22).** Può restare in fondo alla track Python oppure essere spostata dentro la track Django, subito prima delle view async. La seconda opzione accorcia Python di 4 giorni.
4. **Riuso dei problemi saltati nel test.** M11, M15 e M23 riprendono i problemi di S03, S04 e S05. Se vengono usati come esercizi, l'assessor non potrà riusarli come misura nelle verifiche e dovrà crearne di nuovi.
