# Chiave 006 (solo reviewer)

Test base sul codice di partenza: 4 rossi, 4 verdi (pytest.ini raccoglie test_plan.py e test_ownership.py).
- ROSSO `new_plan_ignores_later_appends_to_the_callers_list`: la lista del chiamante e quella del piano sono la stessa.
- VERDE `add_meal_on_one_plan_does_not_touch_another`: il default e` gia` corretto (`None`), come in 004; nessuna condivisione tra piani. Non c'entra col problema.
- VERDE `with_meal_returns_a_plan_with_the_extra_meal` e VERDE `with_meal_returns_a_different_plan_object`: `dict(plan)` e` un dict nuovo, ma `meals` e` la stessa lista. Il secondo e` la trappola E004/E001: "oggetto nuovo" in superficie, stato interno condiviso.
- ROSSO `with_meal_leaves_the_original_plan_alone`: `updated["meals"] += [...]` modifica sul posto la lista condivisa.
- VERDE `new_plan_without_meals_is_empty`.
- ROSSO (NotImplementedError) i due test di `merge_plans`.

Dopo la correzione "pezza" di with_meal (`updated["meals"] = updated["meals"] + [x]`) il rosso diventa verde, ma `updated["meals"][0] is plan["meals"][0]` resta True: nascosti `with_meal_and_meal_dicts_are_not_shared...` rosso.
Dopo `list(meals)` in new_plan: i base diventano verdi, ma nei nascosti restano rossi `copy_is_not_shallow` (dict interni condivisi). Con `meals or []`: il base `ignores_later_appends` resta rosso per una lista non vuota (e la tupla non funziona con `add_meal`); con `[]` esplicito il piano ottiene una lista nuova solo per caso (`[] or []`), quindi `explicit_empty_list` e` verde ma per la ragione sbagliata: chiedere in chiacchierata.
Docstring non verificate dai test base: "any sequence" (tupla), "or to the meal dicts inside it" (dict interni), "meal dicts included" (with_meal), "later changes to the returned plan never show up" (with_meal).

Esiti attesi: originale 2/20 nascosti (rilanciato: 18 rossi). Soluzione di riferimento (deepcopy ovunque) 20/20. Lancio:
    PLAN_MODULE=original.plan_original $PY -m pytest -q -c /dev/null -p no:cacheprovider _riservato_reviewer/test_hidden.py
    $PY -m pytest -q -c /dev/null -p no:cacheprovider _riservato_reviewer/test_hidden.py -s    # stampa le scelte di merge_plans
