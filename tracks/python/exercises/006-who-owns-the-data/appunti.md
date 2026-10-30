# Appunti — 006

## Prima di iniziare
(3-5 righe, prima di eseguire qualsiasi cosa: cosa pensi non rispetti il contratto, un dubbio concreto, i casi limite. Una frase deve iniziare con "Secondo me, dopo `new_plan("ann", mine)`...".)

- `new_plan` secondo me ha un problema perché quando viene passato un meals non viene fatta copia profonda e questo va contro la specifica, che chiede che le modifiche non devono influenzare né dentro né fuori dalla funzione; questo fa fallire il test `test_new_plan_ignores_later_appends_to_the_callers_list`.
- `add_meal` mi sembra corretto perché fa un append alla stessa lista che viene passata dentro la funzione, quindi modifica l'oggetto originale come da specifica.
- `with_meal` è sbagliata perché modifica la lista sul posto mentre la specifica chiede di fare return di una nuova lista; avrei usato `lista = lista + update`, `return lista`, oppure ancora meglio facendo una copia profonda del plan.


## Durante
(Cancello: rosso/verde per gli 8 test base con motivo, prima di lanciare pytest. Poi esperimenti: previsione prima, output incollato dopo. Una riga R6 per ogni funzione modificata.)

### Previsione test base (prima di lanciare pytest)
1. `test_new_plan_without_meals_is_empty`: V, perché il default è None e viene creata una nuova lista vuota.
2. `test_new_plan_ignores_later_appends_to_the_callers_list`: R, perché new plan non fa una copia quindi vede le modifiche fatte da fuori.
3. `test_add_meal_on_one_plan_does_not_touch_another`: V, perché il default è None e viene costruita una lista vuota diversa ad ogni chiamata.
4. `test_with_meal_returns_a_plan_with_the_extra_meal`: R, perché era già stato aggiunto un toast nel test precedente quindi dovrebbe essere Tea, Toast, Toast.
5. `test_with_meal_returns_a_different_plan_object`: V, perché costruisce un nuovo dizionario esterno anche se gli oggetti interni non sono copie.
6. `test_with_meal_leaves_the_original_plan_alone`: R, perché non essendo copie viene modificato lo stesso oggetto a cui fa riferimento il chiamante.
7. `test_merge_plans_has_the_meals_of_both_in_order`: R, il merge ora dà NotImplementedError, falliscono tutti quelli che fanno riferimento a lui.
8. `test_merge_plans_leaves_both_inputs_alone`: R, stesso motivo del 7.

### Output pytest (rosso iniziale, `pytest -q -rA`)
```
PASSED test_plan.py::test_new_plan_without_meals_is_empty
PASSED test_plan.py::test_add_meal_on_one_plan_does_not_touch_another
PASSED test_plan.py::test_with_meal_returns_a_plan_with_the_extra_meal
PASSED test_plan.py::test_with_meal_returns_a_different_plan_object
FAILED test_plan.py::test_new_plan_ignores_later_appends_to_the_callers_list
FAILED test_plan.py::test_with_meal_leaves_the_original_plan_alone - Assertio...
FAILED test_plan.py::test_merge_plans_has_the_meals_of_both_in_order - NotImp...
FAILED test_plan.py::test_merge_plans_leaves_both_inputs_alone - NotImplement...
4 failed, 4 passed in 0.02s
```

### Confronto (Nick)
- 4: previsto R, uscito V. "Sbagliato perché è la lista mine ad avere toast, non la new_plan di questa funzione di test."
- Oggetti condivisi tra i test (dopo domanda dell'orchestratore: "c'è un oggetto usato da più di un test?"): "TEA e TOAST sono usati da molti test e se modificati da qualsiasi punto la modifica viene riflessa in tutti gli altri, perché non si usa mai una copia ma sempre l'oggetto stesso; ma si deve fare una modifica al dict, non alla lista come fa il test 4 che ho sbagliato."

### Esperimento A (previsione prima di eseguire)
- A1 (`updated["meals"] += [x]`): `plan["meals"]` contiene il contenuto iniziale + x.
- A2 (`updated["meals"] = updated["meals"] + [x]`): `plan["meals"]` contiene il contenuto iniziale.
- A3 (con la riga di A2): `updated["meals"][0] is plan["meals"][0]` → True, perché il primo elemento della lista è condiviso dalle due liste.

Output (REPL):
```
A1: [{'name': 'tea', 'kcal': 2}, {'name': 'toast', 'kcal': 180}]
A2: [{'name': 'tea', 'kcal': 2}]
A3: True
```

### Correzione di `new_plan`
"Così ho coperto il caso di lista di meals dict e quindi valido che siano tutti dei meals, e faccio la deepcopy per evitare modifiche collaterali tra oggetti condivisi."

### Esperimento B (previsione prima di eseguire)
- `plan["meals"][0]["kcal"]` → 2
- `plan["meals"] is mine` → False

Output:
```
B1: 2
B2: False
```

### R6 `new_plan` (dopo domanda dell'orchestratore su un input non coperto dai test base)
- Tupla: "Le tuple non sono modificabili quindi avrei dei problemi, devo convertire dentro la funzione la tupla o qualsiasi collezione in una lista."
- Validazione (`ValueError` su elementi non meal, non chiesta dalla docstring): considerate tre opzioni (ignorare in silenzio, sollevare cambiando la specifica, non validare; la terza dopo indizio dell'orchestratore: "cosa faceva l'originale?"). Scelta: "lascio la responsabilità al chiamante".

### R6 `with_meal`
- Rispetta "later changes to the returned plan never show up in `plan`". (Input non coperto dai test base: non indicato.)

### Test base dopo le correzioni
Previsione: "i test base li supero tutti".
```
........                                                                 [100%]
8 passed in 0.01s
```

### `merge_plans` e `test_ownership.py`
- Scelta: "i dict del risultato li possiede il risultato stesso".
- Prima versione del test: `is not` sulle liste `meals`. Dopo domanda dell'orchestratore ("una versione con lista nuova ma stessi dict passerebbe il tuo test?"): "ah giusto perché io sto testando la proprietà della lista, non dei dizionari".
- Seconda versione: intersezione di id (`&`, sintassi data dall'orchestratore su richiesta: "l'intersezione ma non so come farla"). Caso `(p, p)`: i due dict del risultato devono essere "due oggetti diversi". Controllo `len(merged_ids) == len(merged_plan["meals"])` aggiunto dopo domanda dell'orchestratore ("se merge_plans mettesse due volte lo stesso dict nuovo?").
- Previsione: "saranno tutti verdi".
```
..........                                                               [100%]
10 passed in 0.01s
```



## Dopo
(Cosa era diverso da come pensavi, la regola che ne ricavi, e la frase "Secondo me..." di prima: reggeva?)

- Cosa era diverso: "Quasi niente, la deepcopy era il modo giusto di fare le cose. L'unica cosa: non mi sono accorto che la specifica chiedeva qualsiasi tipo di collezione ma la add dava per scontato che fosse lista, quindi andava modificata internamente. Inoltre nella prima versione del test ho testato la proprietà della lista e non dei dizionari che la componevano."
- Regola: "Bisogna prestare attenzione a chi possiede il dato e chi lo modifica, bisogna dichiararlo nella specifica. Non è un errore in assoluto condividere il dato, tipo add_meal condivide il dato con il chiamante ma lo dichiara."
- Reggeva? (la frase "Secondo me..." non è stata scritta; ripresa la prima riga di "Prima di iniziare" su `new_plan`): "Sì sì, reggeva la mia ipotesi iniziale su new_plan."


