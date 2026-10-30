# Verbale — 005 (chiacchierata finale, 2026-10-30)

## Domande e risposte (risposte di Nick trascritte fedelmente, senza REPL né codice aperto)
1. *Con la tua versione, cosa restituisce `grams_label(40.5)`? Cosa chiede la docstring?*
   "la mia funzione restituisce unknown, la funzione chiede qualsiasi valore tranne None"
   → Risposta immediata, senza esitazione. Riconosce che la sua versione (`type(grams) is not int`) viola la docstring.
2. *Con la tua versione, cosa restituisce `portion_or_default("\t\n", 100)`?*
   "credo che torni raw perché \t\n non sono catturati dal replace"
   → Giusto, con un "credo". Riconosce che `.replace(" ", "")` non copre "only whitespace" della docstring.
3. *`is_new_food` era corretta e l'hai riscritta: perché? Che rischio c'è nel riscrivere una funzione che funziona?*
   "comporta che potrbbe variare il comportamento se non si fa bene, nel mio caso credo di averla modificata bene ottenendo una maggiore leggibilità, non ho modificato l'interfaccia quindi chi la usa non si accorge"
   → Motivo (leggibilità) dato solo qui: non fornito al momento della modifica nonostante la richiesta. Non cita i test verdi come prova che il comportamento è invariato.
4. *Con `request.GET.get("page")`, come scegli tra `if not value:` e `if value is None:`?*
   "if not restituisce true anche quando la stringa è vuota oltre che quando è None, is None controlla solo che sia effettivamente None ovvero un oggetto singletono in tutto Python"
   → Differenza giusta. Non dice quale sceglierebbe per `page` e perché: la parte di decisione manca.

## Dove ha esitato o si è corretto (durante l'esercizio, dettagli in `appunti.md`)
- Regola su `or`/`and` prima rovesciata, poi "è il contrario" accettato da Nick dopo che l'orchestratore l'ha detto, senza verifica. Previsione dell'Esperimento 0: 3/5 sbagliate (ragiona in `True`/`False`).
- Regola "operando su cui si ferma" arrivata dopo due ipotesi smentite dai dati e 4-5 domande guidate; risposte vaghe intermedie ("dipende dall'operando", "dall'operatore").
- "Secondo me" v1: `("grams" or "food") → true`, in contraddizione con la regola appena ricavata.
- `has_required_fields` descritta come "ritorna sempre true" (restituisce sempre `False`); corretto dopo una domanda.
- `is_new_food` giudicata "tutta sbagliata": era corretta (test 13 verde); spiegato bene dopo l'output con le parentesi giuste.
- Test 3 e 4 previsti rossi "per gli apici" (E006).
- Dopo la correzione previsti 15 verdi: al primo lancio `portion_or_default(0, 100)` va in errore (`.replace` su int). Output non riportato; corretto da solo aggiungendo `type(raw) is str`.
- Verifica di `"  "` nel REPL senza previsione scritta prima ("non lo sapevo"); protesta sul senso della previsione.

## Risposte arrivate dopo un aiuto
- Regola completa su `and`/`or` (Esperimento 0).
- Parentesi giuste su `"grams" or "food" not in row` (v2), dopo la correzione dell'orchestratore sulla lettura della tabella.
- `has_required_fields` restituisce `False`.
- Lato destro di `or` mai valutato in "Secondo me" v2.
- "Gli apici dicono che è una stringa": dopo spiegazione di teoria e due domande.

## Indizi e aiuti dati
- Liv. 1 (non richiesti, socratici): domande su quale operatore si applica prima e se `or` guarda a destra; "in quale operando si è fermato?"; "rileggi il corpo" (`has_required_fields`); "rileggi la docstring" (`portion_or_default`); "dove mette le parentesi" (`is_new_food`).
- Liv. 2: indicata la tabella "Operator precedence" della Language Reference come dove guardare. **Errore dell'orchestratore**: detto che la tabella va dalla priorità più bassa alla più alta; nella documentazione attuale è il contrario. La v1 di "Secondo me" ne è conseguenza per la parte sulle parentesi (annotato in `appunti.md`).
- Teoria su richiesta: `str` contro `repr`, apici come delimitatori (E006).
- Nessun indizio di livello 3.

## Tempi
- Lavoro: sessione avviata il 2026-10-28 (dopo la chiusura di 004 nello stesso giorno), ripresa il 2026-10-30 dopo 2 giorni. Durata effettiva non rilevata.
- Ambiente: REPL di Python 3.14 che con un blocco incollato mostra solo l'ultima espressione (due tentativi; un'indicazione sbagliata dell'orchestratore sui `;`), risolto con una tupla. Comandi copiati nella clipboard dall'orchestratore su richiesta di Nick.

## Cosa ha sistemato l'orchestratore nella forma
- Tutto `appunti.md` trascritto dalla chat (processo deciso il 2026-10-28).
- Totale dei rossi previsti contato dall'orchestratore sulla lista di Nick (8).
- Elenco dei 6 scarti preparato dall'orchestratore come base per "Dopo"; le spiegazioni sono di Nick.
- Output del secondo lancio di pytest eseguito dall'orchestratore (15 passed); primo lancio riferito a voce.
