# 005 — Condizioni che mentono
Modulo: M01 | Difficoltà: 3 | Tempo: 50 minuti | Tipo: nuovo (truthiness e precedenza)

Cinque funzioni di validazione di una voce di pasto hanno una condizione scritta male: sbagliata, o giusta per caso. Le leggi, le prevedi, le riscrivi.

## Teoria essenziale
Ogni oggetto ha un valore di verità. Falsy: `None`, `False`, `0`, `0.0`, `""`, `[]`, `{}`, `()`. Tutto il resto è truthy, comprese `"0"`, `" "` e `[""]`. `if x:` chiede "x è non vuoto/non zero?"; `if x is not None:` chiede "x è stato fornito?". Divergono proprio sui falsy validi.

`or` e `and` non restituiscono `True`/`False` ma **uno dei due operandi**: `a or b` dà `a` se `a` è truthy, altrimenti `b`. Precedenza, dalla più forte: confronti e `in`/`not in`/`is` > `not` > `and` > `or`. Quindi `a or b and c` è `a or (b and c)`. Una condizione può leggersi in modo diverso da come è scritta in italiano.

```python
if name == "tea" or "coffee":     # not "tea or coffee": the right operand is a bare string
    ...
```
Documentazione: Language Reference, "Boolean operations", "Operator precedence"; Library, "Truth Value Testing".

## Il problema
`meals.py` ha 5 funzioni, ciascuna con la sua docstring-specifica (leggile: sono il contratto). I test base `test_meals.py` coprono i casi normali e qualcuno ovvio, non tutti. Nota: non è detto che una funzione sbagli; una può già comportarsi bene ed essere solo difficile da leggere.

## Regole
1. Il comportamento è quello scritto nelle docstring. Non cambiare le firme né `test_meals.py`.
2. Cambia il minimo: tocca la condizione, non riscrivere la funzione.
3. Ogni condizione finale deve potersi leggere ad alta voce senza dover ricordare la tabella delle precedenze: se serve, parentesi o confronti espliciti. Per ogni funzione dici in "Dopo" perché hai scelto `is None` oppure la verità dell'oggetto.
4. Niente tentativi a caso con pytest: ogni modifica ha una previsione scritta prima.

## Cosa fare
1. Leggi `meals.py` e `test_meals.py`. Non eseguire niente.
2. Scrivi "Prima di iniziare" in `appunti.md` (c'è la consegna per la frase da riprendere dopo).
3. **Cancello**: in chat, per ciascuno dei 15 test, nell'ordine del file, dì rosso o verde sul codice originale con una riga di motivo. L'orchestratore trascrive. Solo dopo si lancia pytest; incolla il rosso e confronta test per test.
4. Esperimenti nel REPL, previsione prima, output copiato dopo:
   - **A.** `"grams" or "food" not in ["food"]`: cosa viene mostrato nel REPL e con `print(...)`? Quanto vale `bool(...)`? Quale parte è mai stata valutata come membership?
   - **B.** `bool(v)` per `0, 0.0, "", " ", "0", [], [""], {}, None`.
   - **C.** `not "a" in ["b"]`, `(not "a") in ["b"]`, `True or False and False`, `(True or False) and False`.
5. Correggi `meals.py`. Rilancia, poi spiega in "Dopo" le funzioni che il test base non distingueva (dove `if x:` e `is not None` avrebbero dato lo stesso verde).
6. Scrivi "Dopo" in `appunti.md`.

Nomi, codice e commenti in inglese; appunti in italiano.

## Comandi
```bash
cd /Users/nicolachiarappa/Desktop/Projects/learning/tracks/python/exercises/005-truthiness
PY=/Users/nicolachiarappa/Desktop/Projects/learning/.venv/bin/python
$PY -m pytest -q
$PY -m pytest -q -k label        # un gruppo di test
```
Lancia da questa cartella. `original/meals_original.py` è la copia di riferimento: non toccarla.

## Consegna
Test verdi e `appunti.md` con le tre parti: scrivi all'orchestratore "consegno 005".
Se dopo 20 minuti sei bloccato, scrivi in "Dopo" dove, cosa hai provato e che ipotesi hai.
