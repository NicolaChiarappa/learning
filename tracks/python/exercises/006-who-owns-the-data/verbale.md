# Verbale — 006 (chiacchierata finale, 2026-10-30)

## Domande e risposte (risposte di Nick trascritte fedelmente, senza REPL né codice aperto)
1. *Hai scritto che "quasi niente" era diverso. La tua prima versione corretta di `new_plan` faceva però una cosa in più rispetto alla docstring: quale? Ha qualcosa in comune con l'errore di 005 su `grams_label`?*
   "intendi il fatto che controllava la correttezza della forma del dict? si vero ma perché non ho capito lo standard cosa dice è una scelta autonoma ne abbiamo parlato"
   → Riconosce la validazione aggiunta (`ValueError`) dopo che la domanda ne indica l'esistenza. Non risponde sul legame con 005 (E009: comportamento che si discosta dalla docstring). La attribuisce a uno "standard" non noto, non alla lettura del contratto.
2. *`merge_plans` ricostruisce i pasti con `add_meal(plan, meal["name"], meal["kcal"])`. Con un pasto `{"name": "tea", "kcal": 2, "notes": "no sugar"}`, cosa c'è nel risultato? È un problema rispetto al contratto? (rileggi la docstring del modulo)*
   "non sarebbe un problema quella info verrebbe ignorata la docstring del modulo dichiara la forma che deve avere un dict di plan e meals ci fidiamo di chi lo userà"
   → Immediata e coerente con la scelta su `new_plan` (non validare, contratto nel modulo).
3. *Dopo `result = with_meal(plan, "toast", 180)`, `result` condivide ancora oggetti con `plan`? Se sì quali, e perché la docstring resta rispettata?*
   "condivide gli oggetti di name e kcal ma sono immutabili quindi non possono essere modificati dall'esterno"
   → Giusta nel meccanismo (deepcopy non copia gli immutabili; condividerli è innocuo). Non cita la stringa di `owner`, anch'essa condivisa.

## Dove ha esitato o si è corretto (dettagli in `appunti.md`)
- Previsione dei test base: 7/8 (fatta in chat prima di pytest; il cancello ha funzionato). Scarto sul 4: previsto rosso perché "era già stato aggiunto un toast nel test precedente", cioè stato creduto trascinato da un test all'altro tramite una lista locale. Regola corretta sugli oggetti condivisi tra test (`TEA`, `TOAST`; serve una modifica al dict, non alla lista) arrivata dopo una domanda.
- La frase "Secondo me, dopo `new_plan("ann", mine)`..." e il dubbio/caso limite non sono stati scritti prima del lancio di pytest, nonostante due richieste. In "Dopo" il "reggeva?" è riferito alla prima riga di "Prima di iniziare".
- Prima correzione di `new_plan`: `deepcopy` giusta, più una `ValueError` di validazione non chiesta dalla docstring. Tupla ("any sequence") non gestita; individuata da Nick dopo la domanda R6 su un input non coperto dai test.
- Sulla validazione: prima "è un problema, devo ignorare tutti quelli che non sono meal" (scarto silenzioso, anch'esso fuori contratto), poi "ignorare o modificare la specifica"; la terza opzione (non validare) arrivata con un indizio. Obiezione "lasciare la responsabilità al chiamante non è corretto, è il problema di Python" discussa; scelta finale: non validare.
- Prima versione di `test_ownership.py`: `is not` sulle liste `meals`, quindi non prova la proprietà dei dict (stesso salto di livello di A3). Riconosciuto subito dopo la domanda. Seconda versione: `<=` tra insiemi (passa con condivisione parziale), poi `merge_plans(first, first)` al posto del caso normale; corretto dopo due domande.
- R6 di `with_meal`: parola della docstring indicata, input non coperto dai test non indicato.

## Risposte arrivate dopo un aiuto
- Regola sugli oggetti condivisi tra i test (dopo domanda "c'è un oggetto usato da più di un test?").
- Tupla in `new_plan` (dopo la domanda R6).
- Terza opzione sulla validazione (dopo "cosa faceva l'originale?").
- Test di proprietà sui dict e non sulla lista; intersezione al posto di `<=`; `len(merged_ids) == len(merged_plan["meals"])` per il caso `(p, p)`.
- D1 (validazione come comportamento in più).

## Indizi e aiuti dati
- Liv. 1 (socratici, non richiesti): oggetti condivisi tra test; input non coperto dai test (R6); "quale frase della docstring chiede la ValueError?"; "una versione con lista nuova ma stessi dict passerebbe il tuo test?"; caso misto e caso `(p, p)` nel test; "se merge_plans mettesse due volte lo stesso dict nuovo?".
- Liv. 2: "guarda `original/plan_original.py`: cosa faceva con un elemento sbagliato?" (direzione verso la terza opzione).
- Teoria su richiesta: dove validare (al confine contro all'interno, funzioni pubbliche di libreria, type hint e type checker); operatore `&` tra set (sintassi, chiesta da Nick: "l'intersezione ma non so come farla"); chiarito che `first` e `second` di `merge_plans` sono piani (lettura della docstring e dei test).
- Nessun indizio di livello 3.

## Previsioni e calibrazione
- Test base sul codice di partenza: 7/8.
- Esperimento A: 3/3 (A3 `True` previsto con il perché giusto). Due esiti alternativi non scritti.
- Esperimento B: 2/2.
- Test base dopo le correzioni: "tutti verdi" → 8/8. `test_ownership.py` finale: "tutti verdi" → 10/10 totali.
- Nessuna stima dei test nascosti.

## Tempi
- Esercizio pronto alle 14:05; chiacchierata finale chiusa alle circa 16:22. Circa 2 ore e 15 minuti, contro i 45-60 previsti. Una parte (circa 10-15 minuti) è teoria richiesta da Nick sulla validazione. Al controllo dei 75 minuti proposto di fermarsi dopo `with_meal`: Nick ha proseguito.
- Tempo di ambiente: trascurabile.
- Giornata: review e riscaldamento di 005 nella stessa giornata, prima di 006.

## Forma sistemata dall'orchestratore
- Trascrizione in `appunti.md` di tutte le risposte date in chat (regola del 2026-10-28).
- Colonna "pytest" della tabella di confronto compilata su richiesta di Nick; confronto e spiegazione dello scarto fatti da Nick.
- Snippet REPL dell'esperimento A preparato e copiato negli appunti di sistema; esperimento B eseguito dall'orchestratore dopo la previsione di Nick.
- Output di pytest lanciato dall'orchestratore e incollato.
