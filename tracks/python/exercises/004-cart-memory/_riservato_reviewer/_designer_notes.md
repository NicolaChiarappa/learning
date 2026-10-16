# Note del designer — 004 (per il reviewer e l'orchestratore, Nick non le apre)

Formato leggero. `pytest.ini` raccoglie solo `test_cart.py` e `test_regression.py`; i nascosti si lanciano con il file esplicito. Esiti attesi in `chiave.md`.

## Cosa allena
- Concetto nuovo unico: i default sono valutati alla definizione, uno solo, conservato in `__defaults__`. `created_at=time.time()` è lì per separare "mutabile" da "valutato una volta": chi ha capito solo "default mutabile = male" corregge `items` e lascia `created_at` (nascosti R3 rossi).
- Ripassi dentro il lavoro: E005 (esperimento B, `+=` contro `= ... +` con alias, indice a sinistra), E007 (esperimento C: `==` e `is` divergono sul corretto), E006 (test 4: `'750' == 750`, da leggere), E001/E004 (test 5 verde: `cart["items"] = []` sposta la posizione fuori dallo stato condiviso).
- P02 (esito alternativo scritto prima), P04 (stima dei nascosti su 12), processo: rosso iniziale incollato e previsione test per test.
- Criterio di uscita M01 (parte "corregge un default mutabile in codice non suo spiegando il meccanismo").

## Casi limite che ho in mente (elenco completo)
1. `items` passato esplicitamente vuoto (`[]`): la fix `items = items or []` lo sostituisce con una lista nuova, quindi il carrello non guarda più la lista del chiamante; con `is None` la tiene. Non specificato: non è un errore, ma chiedere in chiacchierata di che lista parla il chiamante.
2. Proprietà della lista passata: `new_cart("a", items=mine)` poi `add_item`: `mine` cambia? Non specificato in README di proposito (anticipa M01 es. 5). Nessun test: osservarlo e chiedere se la scelta è stata fatta o capitata.
3. `items=None` passato esplicitamente: con sentinella `None` equivale a "non passato"; accettabile, va dichiarato.
4. `created_at=0` o `0.0` passato: con `if not created_at` viene sostituito (bug); con `is None` no. Aggiungere un nascosto se Nick usa la truthiness.
5. Carrello vuoto: `total_cents` -> `0` int.
6. `empty_cart` su un carrello che condivide il default (originale): verde, ma il default conserva gli elementi.
7. `empty_cart` poi `add_item` sullo stesso carrello; `add_item` dopo `empty_cart` non deve toccare altri.
8. Prezzi non int, nomi duplicati, prezzi negativi, `customer` vuoto: non specificati, nessun test.
9. Orologio: `time.time()` non è monotono né iniettabile; non è richiesto (arriva in M11/M16).
10. Fix con `copy`/`deepcopy` del default dentro la funzione o `items = list(items)`: funziona ma cambia la proprietà (caso 2).

## Trappole di design tipiche
1. Pezza su `add_item` (`cart["items"] = cart["items"] + [...]`): test 1-3 verdi, `new_cart.__defaults__[0]` ancora condiviso. R7 la intercetta se il test usa `is not`.
2. Correggere `items` e dimenticare `created_at` (modello "mutabile = male").
3. `items=None` + `if not items:`; `created_at` con `if not created_at`.
4. Spostare il default in una costante di modulo (`EMPTY = []`): stesso difetto riscritto.
5. Test di regressione con `==` (E007), o che aggiunge e guarda solo il carrello modificato.
6. Cambiare la firma (togliere i default) rompe R1 e il test 1.
7. Correggere `total_cents` (`str`) e credere che sia la stessa causa: sono tre cause (items, created_at, str).

## Buona contro eccellente
- Buona: tutti i test verdi, `None` come sentinella per entrambi, test di regressione con `is not` che fallisce sull'originale, regola finale con "valutato una volta alla definizione".
- Eccellente: prevede i 3 rossi/3 verdi compreso il test 5 verde con la ragione giusta (posizione spostata, default intatto); nota che il test 3 è verde da solo; prova la pezza su `add_item` e mostra che R7 la distingue; dichiara il caso 1 o 4; motiva "None come sentinella invece di X" con un'alternativa vera; stima i nascosti (attesi 12/12 con la sentinella `is None`); scrive in "Dopo" la regola per `default=list` in Django.

## Compromesso sul tempo
Previsti 60 minuti: 6 previsioni, 3 esperimenti, 1 test, 1 correzione. In 003 Nick ha impiegato più del doppio; punto di controllo a 40 minuti già nel README (si taglia B, mai il rosso). Tempo di ambiente da registrare a parte.
