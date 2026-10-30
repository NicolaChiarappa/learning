# Note del designer 005

Allena: valore di verita degli oggetti, `is None` vs verita, precedenza `not`/`and`/`or`/`in`, `or` restituisce un operando.
Atteso sull'originale: ROSSI 5/15: required_fields_complete_row, label_zero_grams, default_when_blank_text, default_keeps_zero, review_confirmed_high_kcal. Verdi 10, di cui molti verdi "per caso" (e il punto della previsione: missing_grams verde con condizione sbagliata; i 3 test di is_new_food verdi con condizione corretta ma ambigua).

Casi limite che il base NON copre (per il reviewer):
- has_required_fields: riga vuota; chiave presente con valore vuoto/None (presenza != valore); row non dict.
- grams_label: 0.0, False (bool!), "" (stringa vuota, non None), Decimal("0").
- portion_or_default: "" , "\t\n", [] (non e str: resta []), False, 0.0, Decimal("0"), default falsy.
- needs_review: bordi 1000/900 (stretto >), confirmed mancante (KeyError), confermato + entrambi grandi, non confermato solo kcal grande (oggi True anche sull'originale), grams None.
- is_new_food: food "" (stringa vuota: e un nome? spec dice "not None" => "" non in seen -> True), chiave "food" assente (get -> None -> False), seen_foods come set/generatore.

Trappole: 
- `if grams is None` vs `if grams == None`; usare `if grams != 0` o `isinstance` inutili.
- portion_or_default: `raw.strip() or default` rompe 0 e None; `if not raw or not str(raw).strip()` perde lo 0 e [].
- needs_review: spostare solo la parentesi sbagliata (`(not confirmed and grams>1000) or ...` e un no-op). Verificare se scrive la parentesi sul pezzo giusto o riscrive con if annidati (ok).
- is_new_food: Nick potrebbe "correggerla" cambiando comportamento senza motivo, o dire che non funziona. Verificare se spiega che `not x in y` e `not x is y` sono analizzati come `not (x in y)` (not ha precedenza piu bassa degli operatori di confronto).
- Esperimento A: `"grams" or ...` restituisce `'grams'` (REPL con apici, print senza): E006. `bool(...)` True. La membership non viene mai valutata (cortocircuito).
- Esperimento C: `not "a" in ["b"]` -> True; `(not "a") in ["b"]` -> False. `True or False and False` -> True; `(True or False) and False` -> False.

Buona vs eccellente: buona = test verdi, minimi cambiamenti. Eccellente = distingue is None da verita per ogni funzione motivandolo, prevede i rossi giusti prima, nota che "0" resta truthy, spiega il cortocircuito di A, e aggiunge da solo casi limite (False come grams, "" in is_new_food) prima del reviewer.
