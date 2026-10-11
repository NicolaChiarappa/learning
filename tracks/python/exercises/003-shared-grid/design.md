# Nota di design — 003
(Questo file è un cancello: si compila PRIMA di modificare `seating.py`. Controllo: `pytest -q test_delivery.py -k gate`. Le sezioni 1-3 si scrivono solo leggendo il codice e le regole del README, senza eseguire niente. Nella sezione 4 esegui solo dopo aver scritto le due righe "Se ho ragione" e "Se ho torto". Il file si riusa nei prossimi esercizi: stessa struttura.)

## 1. Chi guarda cosa
Leggi `build_hall` in `seating.py` così com'è. Dopo `hall = build_hall(3, 2)`:

**Posizioni e liste:**
<!-- Una voce per posizione: `hall[0]`, `hall[1]`, `hall[2]`, ciascuna con la lista che quella posizione guarda. Dai a ogni lista distinta un nome per ruolo (in inglese). Se due posizioni guardano la stessa lista, usa lo stesso nome. Sei sicuro? Scrivilo come lo vedi, non come vorresti che fosse. -->

## 2. Casi limite dalla consegna
<!-- Almeno 3 righe, dalle regole R1-R9 del README. Formato di ogni riga:
- `chiamata concreta, per esempio build_hall(...)` → cosa deve succedere (regola Rn)
Se la consegna non dice cosa deve succedere, scrivi "la consegna non lo dice" e cosa decidi tu. -->

## 3. Test che prevedo rossi
**Test che prevedo rossi:**
<!-- I nomi dei test di `test_seating.py` che pensi falliscano sul codice così com'è, in base al tuo schema della sezione 1. I test non nominati li prevedi verdi. Se pensi che nessuno fallisca scrivi "nessuno". -->

## 4. Esperimento sulla causa
**Ipotesi sulla causa:**
<!-- Una frase: dove pensi sia il difetto, in quale funzione e in quale riga. -->

**Ipotesi rivale:**
<!-- Una frase: un'altra causa plausibile, diversa dalla tua, che avrebbe prodotto gli stessi sintomi. -->

**Codice:**
```python
```
<!-- Al massimo 6 righe, da eseguire nel REPL o in un file usa e getta, che decidono tra le due ipotesi. Deve usare `build_hall` e almeno un confronto con `is`. Nomi in inglese e per ruolo. -->

**Se ho ragione:**
<!-- L'output esatto, carattere per carattere, se vale la tua ipotesi. -->

**Se ho torto:**
<!-- L'output esatto, DIVERSO dal precedente, se vale l'ipotesi rivale. Se non riesci a scriverlo, l'esperimento non decide niente: cambialo. -->

**Output ottenuto:**
```
```
<!-- Da compilare dopo aver eseguito. Incollato dal terminale, mai riscritto a mano. -->

**È uscito:**
<!-- Una sola parola: ragione / torto / nessuno dei due -->
