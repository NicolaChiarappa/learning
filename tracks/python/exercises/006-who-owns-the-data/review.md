# Review — 006 — 2026-10-30

## Esito
Test base: 10/10 (8 `test_plan.py` + 2 `test_ownership.py`) | Nascosti: 25/25 (20 del designer + 5 del reviewer; sull'originale 3/25) | Indizi: liv. 1 socratici (6), liv. 2 (1), teoria su richiesta (validazione, `&`)
| Correttezza 4 | Casi limite 2 | Design 3 | Leggibilità 2 | Idiomaticità 3 | Processo 2 |
Calibrazione: cancello 7/8, esperimento A 3/3, B 2/2, "tutti verdi" 2/2. Nessuna stima dei nascosti. Tempo: circa 2h15 contro 60 minuti.

## Il punto più importante
Il codice finale rispetta il contratto, ma la docstring l'hai letta solo dove c'era il bug, cioè sulla copia. "any sequence" l'hai mancato, e la prima versione di `new_plan` sollevava una `ValueError` che nessuna riga chiedeva. Sono i due versi dello stesso errore di 005 (E009): il codice segue la tua idea della funzione, non le parole del contratto. Lo strumento c'era già (R6: una parola della docstring e un input che i test non coprono). Per `new_plan` ci sei arrivato dopo la domanda, per `with_meal` l'input manca ancora.

## Casi limite
Previsti prima: i dict interni ("copia profonda... né dentro né fuori"), che è il centro dell'esercizio. Mancati: la tupla, trovata solo dopo la domanda R6; la lista vuota esplicita; il `(p, p)` del test, che il README chiedeva ma che hai scritto giusto solo dopo due domande. Cosa avrebbe dovuto farteli vedere: leggere la firma e la docstring di `new_plan` una parola alla volta e chiedersi, per ognuna, "quale input la mette alla prova?".

## Osservazioni sul codice
1. `merge_plans`, righe 53-56: ricostruisci ogni pasto da `name` e `kcal`, mentre `new_plan` e `with_meal` copiano il dict così com'è. Ci sono due conseguenze misurate nei nascosti. Una chiave in più sparisce solo in `merge_plans`. Un dict ripetuto (`[d, d]`) resta un oggetto solo in `new_plan`/`with_meal` (memo di `deepcopy`) e diventa due in `merge_plans`. Rispetto al contratto va bene (D2 l'hai motivata), ma sono tre funzioni con tre idee di "copia". Chiediti quale delle tre è la regola del modulo.
2. Riga 24: dopo `deepcopy` la lista viene copiata una seconda volta. Funziona, ma chi legge non capisce quale delle due righe garantisce "copia sua" e quale "è una lista". Una riga sola deve dire una cosa sola. Effetto collaterale: un generatore viene rifiutato (`cannot pickle 'generator'`). È fuori contratto, ma è una conseguenza che non hai scelto.
3. `test_ownership.py`: confrontare gli insiemi di `id` con l'intersezione è la forma giusta, e il test boccia tre implementazioni sbagliate che ho provato (dict condivisi, condivisione parziale, `deepcopy` unico con memo). Però `len(merged_ids) == len(...)` dimostra una cosa che la docstring non dice (due posizioni, due oggetti), e la prima versione controllava la lista e non i dict: test e contratto vanno scritti allo stesso livello. Nomi: `diz` è italiano e per tipo, `independency` non esiste in inglese.
4. Docstring di `merge_plans` (righe 45-50): rientro sbagliato, inglese da rivedere ("don't affects on", "neither ... or"), non dice l'ordine dei pasti. La frase sulla proprietà c'è (R5 rispettata).

## Errori registrati
E009 occorrenza 2, ripasso 2026-11-06. E001 occorrenza 5 (test 4 previsto rosso per una lista locale di un altro test), ripasso 2026-11-06. E004 dati positivi (A3, B, D3) con riserva sul primo test, data invariata 2026-11-04. E003 non verificato.

## Domande per te
1. Prima di dire "finito": per ogni parola della docstring, quale input la mette alla prova, e un test base la copre?
2. Il mio test dimostra la frase della docstring, o una frase più forte o più debole?

## Esito modulo
PASSATO CON RISERVA. Codice e contratto di `merge_plans` sono giusti e il test li dimostra. Riserva: tupla, livello del test e caso `(p, p)` sono arrivati dopo domande. La frase "Secondo me..." non è stata scritta nonostante due richieste. R6 di `with_meal` è incompleta. M01 non è chiuso: manca il set di 10 snippet.
