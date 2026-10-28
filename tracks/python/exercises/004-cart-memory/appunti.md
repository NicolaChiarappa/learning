# Appunti — 004

## Prima di iniziare
(3-5 righe, dopo aver letto codice e regole e prima di eseguire qualsiasi cosa: cosa pensi che non vada e perché; un dubbio concreto; i casi limite che ricavi dalle regole.)

allora ho dato un occhio alle funzioni implementate il primissimo problema che noto è:
```python
def new_cart(customer, items=[], created_at=time.time()):
```
in questa firma viene dichiarato due defualt:time.time()  e questo vuol dire che qualsiasi carrello costruito senza passare un argomento condividerà il carrello e il tempo di creazione

faccio questo esperimento
se ho torto mi aspetto false, se ho ragione mi aspetto true
```python
import time
>>> def new_cart(customer, items=[], created_at=time.time()):
...     return (customer, items, created_at)
 cart1 = new_cart("ann")
>>> cart2 = new_cart("ann")
>>> cart2[1] is cart1[1]
>>> cart1[2] is cart2[2]

```

output : True, True

assodato che questo errore esiste possiamo anche prevedere che tutte le funzioni di modifica come rimozione di items dal carrello andranno a modificare tutti i carrelli che sono stati creati senza parametri

quindi anche i test come test_items_keep_the_order_they_were_added_in se lanciati in sequenza ad altri precedenti fallirà perché l'oggetto items è già stato modificato, questo l'ho dimostrato già con l'esperimento

## Durante
(Previsione dei 6 test base prima del primo lancio, poi il rosso incollato e il confronto. Per ogni esperimento: "se ho ragione: ... / se ho torto: ..." scritto prima, poi l'output dal terminale e quale dei due è uscito.)

*(Da qui le risposte sono date da Nick in chat e trascritte fedelmente dall'orchestratore.)*

**Test base:** lanciati prima di scrivere la previsione; nessuna previsione test per test disponibile. Osservato da Nick: `test_items_keep_the_order_they_were_added_in` passa da solo, fallisce nel gruppo. Output non incollato.

**Esperimento B, previsioni (prima di eseguire):**
- B1: "mine contiene [("tea", 300)] e is mine vale True adesso"
- B2: "mine vale [] mentre is mine è false"
- B3: "non ho capito di quali due righe parli"

**Esperimento C, previsioni (prima di eseguire):** sul codice originale "entrambi true".

**Correzione prevista:** "nella firma della funzione (items = list, creates_at=None): if created_at is None created_at = time.time()"
- B3 (dopo riformulazione dell'orchestratore): "la prima quella di B1"
- Su `items=list`, alla domanda "cosa c'è in `cart["items"]` e quanto vale `type(...)`": "nel type penso che ci sarebbe un callable quindi forse meglio mettere list() nel defualt"
- Su `items=list()` (dopo la domanda "quando viene eseguita `list()`? quante liste per tre carrelli?"): "giusto viene chiamato una volta sola allora possiamo mettere anche per list=None e poi creare una nuova lista dentro la funzione come per create_at"
- Perché di B3: "+= "incrementa" la lista sul posto non crea un nuovo oggetto a differenza di lista = lista +[elemento]"
- C sul codice corretto (prima di eseguire): "true, false"

**Output A, B, C sul codice originale** (script fornito dall'orchestratore, lanciato da Nick in un processo nuovo):
```
A before: ([], 1793186869.8597188)
B1: [('tea', 300)] True
B2: [] False
C original: True True
```
Confronto di Nick: "tutte giuste".

**R7, ragionamento** (dopo che l'orchestratore ha spiegato quale pezza su `add_item` si intende e ha chiesto se il difetto resta e come vederlo senza `add_item`): "si il difetto c'è ancora ma il test di regressione potrebbe essere proprio l'esperimento che ho fatto quindi creo i due carrelli e li confronto alla creazione"
- Operatore: "uso l'operatore is come ho già fatto sull'esperimento [...] creo due carrelli li confronto con is se sono è True il test fallisce quindi sarà un assert not carrelo1[1] is carrello2[1]"
- Dopo la domanda dell'orchestratore su cosa restituisce la `new_cart` di `cart.py`: "si intendo cart["items"]"

**Test di regressione** (`test_regression.py`, scritto da Nick). Previsione prima del lancio: "mi aspetto di fallire con originale e di avere il verde con cart corretto. il messaggio di errore è il fallimento sull'assert, non so come lo segnala pytest"

Output sul codice corretto (`new_cart` da `cart`, lanciato da PyCharm):
```
tracks/python/exercises/004-cart-memory/test_regression.py::test_new_cart PASSED [100%]
============================== 1 passed in 0.00s ===============================
```
Output sul codice originale (chiamate temporaneamente a `cart_original.new_cart`):
```
tracks/python/exercises/004-cart-memory/test_regression.py::test_new_cart FAILED [100%]
test_regression.py:4 (test_new_cart)
[] != []

Expected :[]
Actual   :[]
<Click to see difference>

def test_new_cart():
        cart1 = cart_original.new_cart("bob")
        cart2 = cart_original.new_cart("ann")
    
>       assert not cart2["items"] is cart1["items"]
E       assert not [] is []

tracks/python/exercises/004-cart-memory/test_regression.py:9: AssertionError
============================== 1 failed in 0.01s ===============================
```
Confronto di Nick: "sisi la previsione è corretta"

**Suite completa, previsione prima del lancio:** "l'unico che fallirebbe è test_total_cents_sums_the_prices ma perché il test non legge gli apici"
- Dopo tre domande dell'orchestratore (tipo restituito, R6, cosa dicono gli apici): "restituisce una stringa, va corretto il codice: return total"


## Dopo
(Cosa era diverso da come pensavi; la scelta di correzione, "X invece di Y perché"; quali regole R1-R7 ritieni coperte dai test base e quali no; quanti test nascosti su 12 pensi di passare; la regola che ti porti via, scritta in modo che valga per codice mai visto.)

*(Risposte date in chat il 2026-10-28, trascritte dall'orchestratore.)*

- Regole R1-R7 coperte dai test base e stima dei test nascosti: non date per scelta di Nick ("delle regole andiamo avanti non ci importa").
- Regola che si porta via: "il default delle funzioni va usato con cautela e solo quando ha davvero senso che venga condiviso con tutti i chiamanti, in tutti gli altri casi meglio passare None e istanziare nel corpo della funzione."


