# 006 — Chi possiede il dato?
Modulo: M01 (esercizio 5, design) | Difficoltà: 3 | Tempo: 60 minuti | Tipo: nuovo (contratto di proprietà) + ripasso E001/E003/E004, E009

## Teoria essenziale
Quando passi una lista a una funzione, la funzione riceve **lo stesso oggetto**, non una copia. Se lo conserva (in un dict, in un attributo), da quel momento chiamante e funzione hanno due nomi per un oggetto solo, e chiunque lo modifichi lo cambia per l'altro. In 004 l'hai visto: con la correzione `None`, `new_cart("x", items=mine)` seguito da `add_item` modificava `mine`.

Non esiste una scelta giusta in assoluto: esiste una scelta **dichiarata**. Tre contratti legittimi: (1) *condivido*: la funzione usa e modifica l'oggetto del chiamante, e lo dice; (2) *copio*: la funzione tiene una copia sua; (3) *restituisco un oggetto nuovo*: l'argomento resta com'era. Il bug nasce quando il codice fa una cosa e la docstring (o il chiamante) ne assume un'altra. `list(x)` e `dict(x)` copiano un livello: gli oggetti **dentro** restano gli stessi. `copy.deepcopy` copia tutto, con un costo.

```python
import copy
row = [["a"], ["b"]]
shallow = list(row)          # new outer list, same inner lists
deep = copy.deepcopy(row)    # new everything
```
Documentazione: modulo `copy` (le prime righe, "shallow and deep copy operations"); Programming FAQ, "How do I copy an object in Python?".

## Il problema
`plan.py` gestisce i piani dei pasti di un'app di nutrizione. Un piano è un dict `{"owner": str, "meals": [ {"name": str, "kcal": int}, ... ]}`. Le docstring di `new_plan`, `add_meal`, `with_meal` sono il **contratto**; il codice è quello che qualcuno ha scritto in fretta. I test base sono pochi e non coprono tutto il contratto.

## Regole
1. **R1** `new_plan`: il piano tiene una copia sua dei pasti. Accetta qualunque sequenza di dict (lista, tupla...); `None` o vuota = nessun pasto.
2. **R2** `add_meal` modifica il piano ricevuto e restituisce `None`.
3. **R3** `with_meal` restituisce un piano nuovo; l'originale resta com'era, e da quel momento nessuna modifica all'uno si vede nell'altro.
4. **R4** `merge_plans(first, second, owner)` (da scrivere): piano nuovo di `owner` con i pasti di `first` e poi quelli di `second`; nessuno dei due ingressi viene modificato.
5. **R5** Il contratto di `merge_plans` che manca è **tuo**: il risultato possiede i propri dict dei pasti o li condivide con gli ingressi? Scegli, scrivilo in una frase nella docstring, e scrivi in un nuovo `test_ownership.py` almeno un test che dimostra la tua scelta. Includi il caso `merge_plans(p, p, "x")`.
6. **R6** Per ogni funzione che modifichi, in "Durante" una riga: quale parola della docstring rispetti, e un input che i test base non coprono.

Firme invariate, `test_plan.py` intatto. Nomi e codice in inglese, per ruolo; appunti in italiano.

## Cosa fare
1. Leggi `plan.py` e `test_plan.py`. Non eseguire niente. Scrivi "Prima di iniziare" in `appunti.md` (3-5 righe). Includi **una frase che inizia con "Secondo me, dopo `new_plan("ann", mine)`..."** e dice chi possiede la lista: in "Dopo" la riprendi e scrivi se reggeva.
2. **Cancello:** per gli 8 test base, nell'ordine del file, dici rosso o verde sul codice di partenza con una riga di motivo. Solo dopo lanci pytest e incolli l'output. Il confronto è tuo.
3. Due esperimenti, ciascuno con previsione (due esiti possibili) scritta prima e output incollato dopo:
   - **A.** In `with_meal`: la riga `updated["meals"] += [x]` contro `updated["meals"] = updated["meals"] + [x]`. Cosa vede `plan["meals"]` dopo la chiamata, nei due casi? Con la seconda riga, `updated["meals"][0] is plan["meals"][0]`?
   - **B.** Dopo la tua correzione di `new_plan`: `mine = [{"name": "tea", "kcal": 2}]`, poi `plan = new_plan("ann", mine)`, poi `mine[0]["kcal"] = 99`. Cosa vale `plan["meals"][0]["kcal"]`? E `plan["meals"] is mine`?
4. Correggi `new_plan` e `with_meal` (R6 per ciascuna). Scrivi `merge_plans` + docstring + `test_ownership.py` (R4, R5).
5. Scrivi "Dopo" in `appunti.md`: cosa era diverso da come pensavi, la regola che ne ricavi, e la frase "Secondo me..." di prima: reggeva?

## Comandi
```bash
cd /Users/nicolachiarappa/Desktop/Projects/learning/tracks/python/exercises/006-who-owns-the-data
PY=/Users/nicolachiarappa/Desktop/Projects/learning/.venv/bin/python
$PY -m pytest -q                       # test_plan.py + test_ownership.py
$PY -m pytest -q -k merge              # un gruppo da solo
```
Lanciali da questa cartella. `original/plan_original.py` è una copia di riferimento: non modificarla.

## Consegna
Quando i test passano e `appunti.md` ha le tre parti, scrivi "consegno 006". Punto di controllo a 40 minuti: se non hai ancora iniziato `merge_plans`, salta l'esperimento B; mai il cancello, il test di R5 e la frase di "Dopo".
