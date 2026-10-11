# Note del designer — 001 (RISERVATO al reviewer: Nick non lo apre)

La chiave con gli output attesi e le spiegazioni è in `_riservato_reviewer/chiave.md`.

## Cosa allena
Modello nome → oggetto (A1, A2): distinguere "sposta un'etichetta" da "modifica un oggetto"; alias, rebinding, `+` contro `+=`, immutabilità di `str`, `is` contro `==`, mutazione attraverso un argomento, copia superficiale contro profonda. Metodo: regole 6 (previsione e sicurezza dichiarate) e 7 (ipotesi verificata nel REPL). Il vero oggetto di valutazione è la **spiegazione scritta**: è il comportamento che il test d'ingresso ha mostrato assente (10 sezioni "Spiegazione" su 10 vuote).

## Cosa valutare e come
- Registrare lo scarto tra "snippet previsti giusti" dichiarati nell'intestazione e risultato reale, e la sicurezza per snippet contro esito (calibrazione).
- Una previsione giusta con spiegazione sbagliata o assente vale poco: segnalarla come "giusta per caso".
- Per gli scarti: la colonna "cosa avevo sbagliato" deve contenere un meccanismo ("pensavo `+=` creasse un nuovo oggetto"), non una constatazione ("era diverso"). E una prova fatta nel REPL (regola 7).
- Test automatici: controllano solo completezza (design compilato, campi pieni, verifica fatta). Non possono dire se le previsioni sono giuste: farlo a mano con la chiave.
- Nomi nei print di prova eventualmente aggiunti: inglese, per ruolo.
- Soglia di riferimento per il criterio di uscita del modulo (8/10 snippet nuovi): qui ci si aspetta un punto di partenza basso (0-4 su 9 giusti) coerente con il test d'ingresso (0 snippet previsti). Un risultato più alto va letto con prudenza: il test d'ingresso diceva livello 0-1.

## Mappa degli snippet
| # | Concetto | Difficoltà vera | Errore tipico atteso |
|---|---|---|---|
| 1 | alias di lista, `append` | bassa | "backup è una copia" |
| 2 | `b = b + [x]` sposta l'etichetta | media | pensare che `scores` cambi |
| 3 | `b += [x]` modifica sul posto | media-alta | trattare `+=` come `= +` (contrasto con 2) |
| 4 | metodi di `str` restituiscono nuovi oggetti | media | è lo stesso errore visto in S01 (`sub.strip()` scartato) |
| 5 | `is` contro `==`; contenitore che tiene un riferimento | media | `==` confuso con `is`; `history["first"]` ritenuto istantanea |
| 6 | `.copy()`, `==` vero ma `is` falso, modifica indipendente | bassa-media | pensare che `==` implichi `is` |
| 7 | mutazione attraverso argomento contro rebinding locale | alta | "la funzione non modifica l'originale perché fa `return`" |
| 8 | argomenti immutabili, `a = b = []` contro due liste distinte | alta | `bump(visits)` scartato: `visits` cambia? ; `second` vuota |
| 9 | copia superficiale contro profonda, `is` sugli elementi interni | alta | `menu.copy()` ritenuta indipendente anche nei livelli interni |
| 10 | (facoltativo) tupla con lista dentro, `+=` che fallisce ma muta | molto alta | atteso fallimento totale: è una sfida, non un criterio |

Le progressioni 2→3 e 7→8 sono coppie costruite per far emergere l'errore: se Nick sbaglia 3 dopo aver capito 2, il modello non è ancora un modello ma una regola memorizzata.

## Casi limite / trappole che ho in mente
- Snippet 3: `+=` su lista chiama `__iadd__` (estende sul posto); su int/str/tuple crea un nuovo oggetto. Non è richiesto che Nick conosca `__iadd__`: basta il comportamento osservato e un'ipotesi.
- Snippet 4: l'`repr` mostra gli spazi; chi non usa `repr` mentalmente può sbagliare su "stampa" degli spazi. Voluto.
- Snippet 5: `history["first"] == evening` è `False` perché `morning` ha ora 4 elementi e `evening` 3. Chi pensa che `history` contenga una copia risponde `True`.
- Snippet 7: `with_item` non modifica `shopping`; `other is shopping` è `False`. Trappola: confondere `items = items + [item]` (rebind locale) con `items.append`.
- Snippet 8: `bump(visits)` scarta il valore restituito e `visits` resta 5; `bump_all` modifica sul posto. `first = second = []` è un solo oggetto con due etichette.
- Snippet 9: `deep["mains"] is menu["mains"]` è `False`; `shallow["desserts"] = ...` aggiunge una chiave solo a `shallow` (rebinding di una chiave, non mutazione di un oggetto condiviso), mentre `append` su `starters` è visibile in `menu`. Questo è il punto fine: la stessa copia superficiale si comporta in due modi.
- `is` su numeri e stringhe volutamente assente: dipende dall'implementazione (interning, cache dei piccoli interi) e non è oggetto di M01 esercizio 1.
- Non tocca: attributi di classe (M07), default mutabili (esercizio 3 del modulo), griglia `[[0]*3]*3` (esercizio 2), truthiness (esercizio 4). La nota Django facoltativa anticipa il default mutabile solo come ipotesi; non è valutata.

## Trappole di design (della consegna, non del codice)
- Rischio principale: previsioni "di pancia" con spiegazione generica ("perché sono riferimenti"). Richiedere nomi veri e il giudizio riga per riga. Una spiegazione che non cita nessun nome dello snippet va segnalata.
- Rischio: Nick esegue gli snippet prima di prevedere. Non verificabile; l'intestazione con orari e la sicurezza dichiarata sono i soli indizi. Segnalare se previsioni e sicurezza sono tutte alte e tutte giuste con spiegazioni vaghe.
- Rischio: scarto compilato con "ho sbagliato perché non sapevo": non accettare come motivazione.
- Il test di completezza può essere superato con testo riempitivo (soglia 40 caratteri): serve la lettura umana.

## Buona contro eccellente
- **Buona**: previsioni giuste su almeno 6/9, spiegazione che cita i nomi e usa "etichetta/oggetto"; per gli errori, meccanismo corretto e una prova nel REPL.
- **Eccellente**: formula la regola generale prima di verificare ("`+=` su lista muta, `+` no"); sicurezza calibrata (bassa dove sbaglia); nel REPL usa `id()`/`is` di sua iniziativa per falsificare l'ipotesi, non solo per confermarla; nello snippet 9 distingue esplicitamente tra mutare un oggetto condiviso e riassegnare una chiave; nella sintesi finale produce una regola applicabile a codice nuovo; ipotesi sensata sulla nota Django.
- **Segnali di allarme**: previsioni giuste ma tutte con sicurezza 5 e spiegazioni vuote o ripetitive; "Se no" riempito con parafrasi dell'output; consegna parziale senza nota di blocco (violazione della regola 8).
