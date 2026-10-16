# 004 — Il carrello che ricorda
Modulo: M01 | Difficoltà: 3 | Tempo: 60 minuti | Tipo: nuovo (default valutati alla definizione) + ripasso E005, E007, E006, E001/E004

Un carrello online "si ricorda" dei clienti precedenti. Trovi il perché, lo correggi, e dimostri la correzione con un test tuo.

## Teoria essenziale
`def` è un'istruzione che **viene eseguita**: quando il modulo viene caricato, Python valuta le espressioni dei valori di default **una volta**, e ne conserva i risultati nella funzione (`nome_funzione.__defaults__`). Le chiamate successive non rivalutano niente: se non passi l'argomento, il parametro guarda l'oggetto già costruito, sempre lo stesso.

```python
import random

def roll(sides=random.randint(1, 6)):   # evaluated once, when "def" runs
    return sides

print(roll(), roll(), roll())           # three equal numbers
print(roll.__defaults__)                # the stored default: a one-element tuple
```

Qui il default è un `int`, immutabile, eppure "ricorda" lo stesso: il problema non è la mutabilità, è **quando** l'espressione viene valutata. Con un oggetto mutabile in più si vede anche il danno. In Django lo stesso errore è `default=[]` invece di `default=list` in un campo.
Documentazione: Tutorial, "Default Argument Values". Dopo la correzione, non prima: Programming FAQ, "Why are default values shared between objects?".

`print("ab")` scrive `ab`, ma pytest mostra le stringhe dentro un'asserzione con gli apici: `assert 'x' == 1` dice che a sinistra c'è una stringa, a destra un int.

## Il problema
`cart.py` gestisce il carrello di un piccolo negozio. Un carrello è un dict con `customer`, `items` (lista di tuple `(nome, prezzo_in_centesimi)`) e `created_at`. In produzione: "il carrello di un cliente contiene a volte cose di un altro", "i carrelli creati nello stesso giorno hanno tutti la stessa ora", "il totale ha il formato sbagliato". Non c'è altro.

## Regole (con il perché)
1. **R1** `new_cart(customer, items=..., created_at=...)` restituisce un carrello nella forma sopra. Senza `items` parte vuoto; con `items` parte con quelli. *(Il contratto.)*
2. **R2** Un carrello creato senza `items` non condivide niente con nessun altro carrello, qualunque cosa sia successa prima. *(Due clienti sul sito nello stesso momento.)*
3. **R3** Senza `created_at`, vale l'istante della chiamata. *(Si ordinano gli ordini per data.)*
4. **R4** Se il chiamante passa `created_at`, vale quello. *(Si importano ordini passati.)*
5. **R5** `add_item` e `empty_cart` modificano il carrello ricevuto e restituiscono `None`. *(Contratto sui propri argomenti.)*
6. **R6** `total_cents` restituisce un **int**; `0` per un carrello vuoto. *(I prezzi sono centesimi.)*
7. **R7** Lasci un test tuo in `test_regression.py` che riproduce R2, fallisce per la causa giusta sul codice originale, e **non diventa verde correggendo soltanto `add_item`**. *(Un test che si lascia ingannare da una pezza non protegge.)*

I test base **non** coprono tutte le regole. Quali restano scoperte lo dici tu in "Dopo".

## Cosa fare
1. Leggi `cart.py`, `test_cart.py` e le regole. Non eseguire niente.
2. Scrivi "Prima di iniziare" in `appunti.md`.
3. In "Durante", **prima** del primo lancio, scrivi per ciascuno dei 6 test base, nell'ordine del file: rosso o verde sul codice originale, con una riga di motivo. Poi lancia `$PY -m pytest -q`, **incolla il rosso** e confronta tu, test per test. Lancia anche da solo il terzo test (`-k items_keep`) e dì cosa cambia.
4. Esperimenti, ciascuno con "se ho ragione: ... / se ho torto: ..." scritto prima e output incollato dopo:
   - **A.** cosa contiene `new_cart.__defaults__` prima di qualunque chiamata e dopo `add_item(new_cart("x"), "tea", 300)`; è lo stesso oggetto di `cart["items"]`?
   - **B.** `mine = []; cart = new_cart("x", items=mine)`. Dopo `cart["items"] += [("tea", 300)]`, cosa contiene `mine` e quanto vale `cart["items"] is mine`? E dopo, partendo da capo, `cart["items"] = cart["items"] + [("tea", 300)]`? Poi: quale delle due righe, dentro `add_item`, farebbe trapelare il default condiviso?
   - **C.** due carrelli appena creati: `a["items"] == b["items"]` e `a["items"] is b["items"]`, prima sul codice originale e poi sul corretto. Quattro valori, tutti previsti prima.
5. Scrivi `test_regression.py` (R7). Lancialo sull'originale: deve essere rosso.
6. Correggi `cart.py` cambiando il minimo: firme invariate (stessi nomi e stessa possibilità di chiamare `new_cart("x")`), `test_cart.py` intatto. Il test deve passare, e il C sul corretto deve dare il risultato che hai previsto.
7. Scrivi "Dopo" in `appunti.md`.

Nomi, codice e commenti in inglese e per ruolo, non per tipo; appunti in italiano.

## Comandi
```bash
cd /Users/nicolachiarappa/Desktop/Projects/learning/tracks/python/exercises/004-cart-memory
PY=/Users/nicolachiarappa/Desktop/Projects/learning/.venv/bin/python
$PY -m pytest -q                      # test_cart.py + test_regression.py
$PY -m pytest -q -k items_keep        # un test da solo
```
Lanciali da questa cartella: dalla radice del repo i nomi collidono con 001/002. `original/cart_original.py` è una copia di riferimento: non modificarla. All'inizio `cart.py` è identico.

## Consegna
Quando i test passano e `appunti.md` ha le tre parti, scrivi all'orchestratore "consegno 004". Ti farà 3-4 domande in chat.
Punto di controllo a 40 minuti: se non sei ancora alla correzione, salta l'esperimento B; mai il rosso incollato, le previsioni e il test di regressione.
Se dopo 20 minuti sei bloccato, scrivi in "Dopo" dove, cosa hai provato e che ipotesi hai: un tentativo minimo onesto vale come consegna.
