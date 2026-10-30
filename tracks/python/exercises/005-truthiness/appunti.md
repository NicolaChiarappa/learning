# Appunti — 005

## Prima di iniziare
(3-5 righe, prima di eseguire qualsiasi cosa: quale pensi sia il difetto di ciascuna delle 5 funzioni, o se non ne vedi; un dubbio concreto; i casi limite. Includi UNA frase che inizi con "Secondo me ..." su come Python legge `"grams" or "food" not in row`: in "Dopo" la riprendi e scrivi se reggeva.)

Secondo me (risposta di Nick in chat, trascritta, data dopo aver aperto la tabella di precedenza): "quindi è (grams or food) not in row ovvero true not in row ovvero true"
(Nota dell'orchestratore: la lettura della tabella seguiva un'indicazione sbagliata dell'orchestratore, "in alto = priorità più bassa"; nella documentazione attuale la tabella va dalla priorità più alta, in alto, alla più bassa. Il passaggio "(grams or food) → true" è invece di Nick.)

Secondo me, versione 2 (2026-10-30, dopo la correzione sulla tabella): "grams or (food not in row) ovvero grams or true -> grams"

Dipende da `row`? (risposta in chat, dopo l'Esperimento 0b): "no non dipende da cosa c'è in row perché grams è sempre truly"

Lettura di `meals.py` prima di eseguire (risposta in chat, trascritta):
- `has_required_fields`: "è sbagliata perché ritorna sempre true andrebbe scritto qualcosa come if grams in row and foodo in row return true else return false"
- `grams_label`: "ritorna unknown anche su valore 0, contro la specifica"
- `needs_review`: "questo sbaglia le precedenze dovrebbe mettere delle parentesi tra gli operandi dell'or"
- `portion_or_default`: "questo è sbagliato perché su 0 ritorna default"
- `is_new_food`: nessuna osservazione
- dubbi: "dubbi rispetto a cosa?"
- casi limite: "i casi limite li vedo principalmente sul fatto che non c'è tipizzazione di nessun tipo"

Seconda risposta, dopo le domande dell'orchestratore (trascritta):
1. `has_required_fields`: "essendo sempre truthy returna sempre false"
2. `portion_or_default`: "c'è anche la stringa vuota ma non so se si considera falsy o truthy"
3. `is_new_food`: "if not entry.get("food") is None and not entry["food"] in seen_foods è tutta sbagliata, andrebbe scritta come if ... is not None and ... not in seen_foods"
4. dubbio: "il dubbio è su "  " vale truthy o falsy"
   casi limite: "casi limite errati: in grams_label 0, in portion_or_default lo 0, in portion or default la stringa " ", l'ho verificato nel repl per toglirmi il dubbio"
   (verifica nel REPL fatta senza previsione scritta prima; output non riportato)
   Previsione: nessuna, "non lo sapevo". Esito riportato da Nick: "ho imparato una cosa nuova "  " è truthy"



## Durante
(Previsioni test per test e esperimenti: previsione scritta prima, poi output copiato.)

### Esperimento 0 — `or` / `and` (in chat, prima della nota di design)
Regole dichiarate prima (risposte di Nick in chat, trascritte):
- prima risposta: "l'or ha sempre bisogno di guardare a destra, l'and solo se la prima condizione è falsa" → poi "si vero è al contrario" (dopo che l'orchestratore ha detto che era al contrario)
- "or smette di guardare a destra se la prima condizione è vera"
- "and restituisce subito false se la prima è false e true solo se anche la seconda è true"
- "la stringa non vuota in python è sempre true"

Previsione:
1. `True or print("right side evaluated")` → True
2. `False and print("right side evaluated")` → False
3. `"grams" or "food"` → True
4. `0 and "food"` → False
5. `"grams" and ""` → False

Output:
```
>>> True or print("right side evaluated")
True
>>> False and print("right side evaluated")
False
>>> "grams" or "food"
'grams'
>>> 0 and "food"
0
>>> "grams" and ""
''
```

Confronto (risposte di Nick in chat, trascritte; arrivate dopo domande guidate dell'orchestratore):
- ipotesi 1: "mi sembra che quando è false stampa il primo mentre quando è true stampa il secondo" → smentita dalle righe 3 e 5
- ipotesi 2: "è il contrario" → smentita dalla riga 4
- "che dipende dall'operando" / "dall'operatore"
- "quindi lui stampa sull'operando su cui si ferma, dove quindi dipende se è falsy in and si ferma subito se truly in and si ferma al primo falsy ecc.."
- regola finale: "and con tutti truly restituisce l'ultimo, or si ferma al primo truly o se tutti falsy l'ultimo"

### Previsione test per test, codice originale (2026-10-30, in chat, prima di pytest)
1. test_required_fields_complete_row: rosso, "ritorna sempre false"
2. test_required_fields_missing_grams: verde, "ritorna sempre false"
3. test_label_positive_grams: "probabilmente rosso perché ritorna con apici singoli non doppi apici l'assert ma il valore è corretto"
4. test_label_missing_grams: "rosso sempre per gli apici singoli ma valore corretto"
5. test_label_zero_grams: rosso
6. test_default_when_none: verde
7. test_default_when_blank_text: rosso
8. test_default_keeps_zero: rosso
9. test_default_keeps_text_zero: verde
10. test_review_unconfirmed_huge_portion: verde
11. test_review_confirmed_huge_portion: verde
12. test_review_confirmed_high_kcal: rosso
13. test_new_food: rosso
14. test_known_food: verde
15. test_food_none: verde

Totale rossi previsti (contati dall'orchestratore sulla lista; Nick non ha dato il totale): 8 (1, 3, 4, 5, 7, 8, 12, 13)

Output pytest:
```
F...F.FF...F...                                                          [100%]
FAILED test_meals.py::test_required_fields_complete_row - AssertionError: assert False is True
FAILED test_meals.py::test_label_zero_grams - AssertionError: assert 'unknown' == '0 g'
FAILED test_meals.py::test_default_when_blank_text - AssertionError: assert '   ' == 100
FAILED test_meals.py::test_default_keeps_zero - assert 100 == 0
FAILED test_meals.py::test_review_confirmed_high_kcal - AssertionError: assert True is False
5 failed, 10 passed in 0.05s
```
Scarti rispetto alla previsione (elencati dall'orchestratore; la spiegazione è di Nick): 3 e 4 previsti rossi → verdi; 13 previsto rosso → verde. 12/15 previsioni giuste.
- 13 (Nick, in chat): "if not (entry.get("food") is None) and not (entry["food"] in seen_foods): sarebbe così quindi in realtà è tutta corretta."
- 3 e 4 (Nick, in chat): "riguardo agli apici non lo so ma di solito mi è viene detto di stare attento negli assert su questo punto degli apici, spiegami come funziona." → spiegazione di teoria dell'orchestratore (E006)

### Esperimento apici (dopo la spiegazione)
Previsione per `("40 g" == '40 g', "0" == 0, ["oats", 40], len("40 g"))`: True, False, ['oats', 40], 4

Output:
```
(True, False, ['oats', 40], 4)
```
Cosa dicono gli apici nell'output di pytest (Nick, in chat, dopo due domande): "penso a capire che è una stringa?"

### Dopo la correzione (2026-10-30)
Previsione prima di rilanciare pytest (Nick, in chat): "mi aspetto 15 verdi, cosa ho cambiato si vede alla fine ho modificato tutte le valutazioni booleane". Riga per funzione e motivo della scelta su `is_new_food` non forniti (riscritta).

Output pytest: non riportato. Nick (in chat): "ho fatto una piccola modifica adesso i test passano tutti". La previsione "15 verdi" quindi non reggeva al primo lancio. Modifica successiva (dal diff): in `portion_or_default` aggiunto `type(raw) is str and` prima di `raw.replace(...)`.
Secondo lancio (eseguito dall'orchestratore per la trascrizione): `15 passed`.
Primo lancio, a voce (Nick, in chat): "l'unico errore che ho commesso è non aver considerato che potevano arrivare anche degli interi nella funzione" (precisazione di Nick: "l'unico errore mi riferivo al lancio del test")

### Esperimento 0b — precedenza, `row = {}` (2026-10-30)
Dopo una domanda dell'orchestratore sul passaggio "grams or true": "ah giusto non valuta mai il lato destro perché or si ferma al primo truly, in questo caso grams"

Previsione:
1. `"grams" or "food" not in row` → grams
2. `("grams" or "food") not in row` → true
3. `"grams" or ("food" not in row)` → grams

Output (le tre espressioni in una tupla: il REPL di 3.14 mostra solo l'ultima espressione di un blocco incollato):
```
>>> row = {}
>>> ("grams" or "food" not in row, ("grams" or "food") not in row, "grams" or ("food" not in row))
('grams', True, 'grams')
```



## Dopo
(Cosa era diverso da come pensavi; la regola che ne ricavi; "reggeva?" sulla frase iniziale.)

(Risposte di Nick in chat, trascritte; scritte sull'elenco dei 6 scarti preparato dall'orchestratore)
1. "allora ne ricavo che gli operatori booleani su valori non booleani tornano sempre il valore su cui si fermano, and si ferma non appena incontra un false o l'ultimo valore dell'operazione e or si ferma appena incontra un true o sull'ultimo valore dell'operazione"
2. "ho sbagliato a considerare le parentesi e ho sbagliato l'output ragionando ancora in booleano nonostante avessi capito la regola"
3. "ho continuato a sbagliare dicendo che tornava true, invece tornava false perché si ferma su grams"
4. "si aveva un problema di leggibilità ma le precedenze erano corrette"
5. "apice o doppio apice è indifferente dipende solo da quale funzione viene usata sulla stringa per rappresentarla, str, print, repr..."



## Riscaldamento (2026-10-30, proposto dal reviewer, dopo la review)
Domanda di Nick: "esiste qualche funzione sulle stringhe che mi dice se è una stringa vuota o /t /n??" → indicata la sezione "String Methods" e `dir(str)` (livello 2, senza nome del metodo). Nick ha trovato da solo: `isspace`.

Previsione per `("".isspace(), "\t\n".isspace(), " 0 ".isspace())`: False, True, False

Proposta di Nick in chat (non ancora applicata in `meals.py` al momento della trascrizione):
```python
def is_invalid_str(s):
    s = s.strip()
    s = s.replace(" ", "")
    if s.isspace() or not s:
        return True
    return False

if raw is None or (type(raw) is str and is_invalid_str(raw)):
    return default
return raw
```
`grams_label`: condizione ridotta a `if grams is None:`.

Output:
(output di `isspace` non ancora riportato)

Versione 2 di Nick (dopo le domande su `strip`/`replace`), nome `is_only_whitespace`:
- risposta 1: "no ma può restare in mezzo a due stringhe tipo "0 2" potrei anche solo fare s = s.replace(" ", "") if s.isspace() or not s:"
- risposta 3 (nome): "only whitespace"

Versione 3 di Nick (dopo la domanda "togli il replace: cambia qualcosa?"):
```python
def is_only_whitespace(s):
    if s.isspace() or not s:
        return True
    return False
```
Output `isspace`: `(False, True, False)` (previsione giusta 3/3).

Versione 3 applicata in `meals.py`, insieme a `grams_label` con `if grams is None:`. Forma `if/return True/return False` lasciata, motivo non dato.
Previsione test nascosti (Nick): 27 verdi.
Output (lanciati dall'orchestratore): base `15 passed`; nascosti `27 passed`.
