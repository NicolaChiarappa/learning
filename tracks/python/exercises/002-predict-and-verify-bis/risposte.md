# Risposte - 002

Scrivi qui, direttamente in questo file, dall'inizio alla fine. Un campo vuoto o lasciato solo con il suggerimento tra `<!-- -->` fa fallire i test di completezza.
Il codice degli snippet è già riportato sotto: non scriverci dentro e non modificare i file in `snippets/`.

Previsioni terminate alle: 19:39
Verifica iniziata alle: 19:52
Minuti di lavoro effettivo (previsioni, verifica, scarti, sintesi): circa 132 in totale dall'inizio (18:15) alla consegna (20:27), calcolati dall'orchestratore; Nick non ha dichiarato la ripartizione
Minuti persi su ambiente (terminale, IDE, comandi: non contano come lavoro): non dichiarati (compresi nel totale sopra)

---

## Snippet 1
**Codice:**
```python
# Snippet 1 - predict every printed line.
names = ["ada", "bob"]
names_alias = names
names += ["eve"]
print(names_alias)

ids = (1, 2)
ids_alias = ids
ids += (3,)
print(ids_alias)
print(ids)

label = "ab"
label_alias = label
label += "c"
print(label_alias)
```

**Righe:**
<!-- Una voce per riga significativa, sempre nella forma: "sposta un'etichetta (quale nome, verso quale oggetto)" oppure "modifica un oggetto (quale)", poi "dopo:" e l'elenco dei nomi che guardano lo stesso oggetto. Se non sai, scrivi "non so" e la tua ipotesi. Aggiungi tu le righe che mancano. -->
- `names_alias = names` →  aggiunge un'altra etichetta allo stesso oggetto ["ada", "bob"]
- `names += ["eve"]` →  aggiunge un elemento alla lista
- `ids_alias = ids` →  aggiunge un'altra etichetta allo stesso oggetto (1,2)
- `ids += (3,)` →  essendo immutabile crea una nuova tupla risultante (1,2,3)
- `label_alias = label` →  aggiunge un'altra label allo stesso oggetto stringa
- `label += "c"` →  crea una nuova stringa "abc" e la assegna alla label "label"

**Previsione:**
<!-- Output ESATTO, una riga per ogni print, dentro un blocco di codice. Vedi "Output esatto" nel README. -->
```
["ada", "bob", "eve"]
(1,2)
(1,2,3)
"ab"
```

**Sicurezza:** <!-- un numero da 1 a 5 -->
5

**Ipotesi alternativa e output che produrrebbe:**
<!-- Obbligatoria se la sicurezza è 1, 2 o 3: una seconda spiegazione plausibile e, in un blocco di codice, l'output ESATTO che darebbe. Deve essere diverso dalla tua previsione: se le due ipotesi danno lo stesso output, non sono due ipotesi. Se la sicurezza è 4 o 5 scrivi "no". -->
no

<!-- Fermati qui. Compila da qui in giù solo dopo aver chiuso le previsioni di tutti gli snippet. -->

**Output ottenuto:**
<!-- Incolla in un blocco di codice l'output reale. -->
```
['ada', 'bob', 'eve']
(1, 2)
(1, 2, 3)
ab
```

**Righe in cui previsione e output differiscono:**
<!-- Confronto riga per riga, fatto da te. Se coincidono tutte scrivi "nessuna". -->
nessuna nel contenuto (dichiarato da Nick). Solo forma (annotazione dell'orchestratore su richiesta di Nick): virgolette doppie invece di apici singoli nella lista; tuple senza spazio dopo la virgola; "ab" previsto tra virgolette, stampato senza.

**Dopo la verifica, la previsione era giusta (si/no):**
si
<!-- Se hai scritto "no" compila tutto lo scarto, nell'ordine. Se hai scritto "si" lascia vuoti i campi seguenti. -->
**Scarto - spiegazione:**
<!-- Cosa pensavi, cosa succede davvero, perché. Con i nomi veri del codice. -->

**Scarto - esperimento:**
<!-- Il codice REPL che provera' la tua spiegazione, in un blocco di codice. Nomi in inglese e per ruolo. Non eseguirlo ancora. -->

**Scarto - atteso (scritto prima di eseguire):**
<!-- Una riga "Atteso: <output esatto> perché <la spiegazione che stai mettendo alla prova>". Una riga per ogni blocco di esperimento. Se non sai cosa scrivere, non hai ancora un'ipotesi. -->

**Scarto - ottenuto:**
<!-- Incolla ciò che è uscito, in un blocco di codice. -->

**Scarto - la spiegazione regge (si/no):**

**Scarto - nuova spiegazione:**
<!-- Solo se hai scritto "no" sopra: la spiegazione corretta e l'esperimento (con la sua riga "Atteso") che la conferma. Altrimenti lascia vuoto. -->

---

## Snippet 2
**Codice:**
```python
# Snippet 2 - predict every printed line.
base_prices = [10, 20]
menu = {"lunch": base_prices}
bundle = [base_prices, base_prices]

base_prices.append(30)
bundle[0].append(40)
print(menu["lunch"])
print(bundle)
print(bundle[0] is bundle[1])

menu["lunch"] = [99]
print(base_prices)
print(bundle[1])
```

**Righe:**
<!-- Una voce per riga significativa, sempre nella forma: "sposta un'etichetta (quale nome, verso quale oggetto)" oppure "modifica un oggetto (quale)", poi "dopo:" e l'elenco dei nomi che guardano lo stesso oggetto. Se non sai, scrivi "non so" e la tua ipotesi. Aggiungi tu le righe che mancano. -->
- `base_prices = [10, 20]` →  crea un oggetto lista e assegna base_prices come label
- `menu = {"lunch": base_prices}` →  crea un nuova dizionario, il valore di "lunch" punta allo stesso oggetto a cui punta "base prices"
- `bundle = [base_prices, base_prices]` →  crea una nuova lista i cui valori sono due riferimenti alla lista "base prices", lista di liste
- `base_prices.append(30)` →  modifica la lista e aggiunge 30 in coda
- `bundle[0].append(40)` →  modifica la lista e aggiunge 40 in coda
- `menu["lunch"] = [99]` →  assegna una nuova lista alla chiave "lunch" del dizionario

**Previsione:**
<!-- Output ESATTO, una riga per ogni print, dentro un blocco di codice. Vedi "Output esatto" nel README. -->
```
[10,20,30,40]
[[10,20,30,40],[10,20,30,40]]
True
[10,20,30,40]
[10,20,30,40]
```

**Sicurezza:** <!-- un numero da 1 a 5 -->
5
**Ipotesi alternativa e output che produrrebbe:**
<!-- Obbligatoria se la sicurezza è 1, 2 o 3: una seconda spiegazione plausibile e, in un blocco di codice, l'output ESATTO che darebbe. Deve essere diverso dalla tua previsione: se le due ipotesi danno lo stesso output, non sono due ipotesi. Se la sicurezza è 4 o 5 scrivi "no". -->
no

<!-- Fermati qui. Compila da qui in giù solo dopo aver chiuso le previsioni di tutti gli snippet. -->

**Output ottenuto:**
<!-- Incolla in un blocco di codice l'output reale. -->
```
[10, 20, 30, 40]
[[10, 20, 30, 40], [10, 20, 30, 40]]
True
[10, 20, 30, 40]
[10, 20, 30, 40]
```

**Righe in cui previsione e output differiscono:**
<!-- Confronto riga per riga, fatto da te. Se coincidono tutte scrivi "nessuna". -->
nessuna nel contenuto (Nick aveva scritto "no"). Solo forma (annotazione dell'orchestratore su richiesta di Nick): liste senza spazio dopo le virgole (tutte e quattro le righe con liste).

**Dopo la verifica, la previsione era giusta (si/no):**
si
<!-- Se hai scritto "no" compila tutto lo scarto, nell'ordine. Se hai scritto "si" lascia vuoti i campi seguenti. -->
**Scarto - spiegazione:**
<!-- Cosa pensavi, cosa succede davvero, perché. Con i nomi veri del codice. -->

**Scarto - esperimento:**
<!-- Il codice REPL che provera' la tua spiegazione, in un blocco di codice. Nomi in inglese e per ruolo. Non eseguirlo ancora. -->

**Scarto - atteso (scritto prima di eseguire):**
<!-- Una riga "Atteso: <output esatto> perché <la spiegazione che stai mettendo alla prova>". Una riga per ogni blocco di esperimento. Se non sai cosa scrivere, non hai ancora un'ipotesi. -->

**Scarto - ottenuto:**
<!-- Incolla ciò che è uscito, in un blocco di codice. -->

**Scarto - la spiegazione regge (si/no):**

**Scarto - nuova spiegazione:**
<!-- Solo se hai scritto "no" sopra: la spiegazione corretta e l'esperimento (con la sua riga "Atteso") che la conferma. Altrimenti lascia vuoto. -->

---

## Snippet 3
**Codice:**
```python
# Snippet 3 - predict every printed line.
# Part A: module level.
log = ["start"]
mirror = log
log = []
log.append("x")
print(mirror)
print(log)


# Part B: the same line, inside a function.
def restart(log):
    log = []
    log.append("x")
    return log


session = ["start"]
result = restart(session)
print(session)
print(result)
print(result is session)
```

**Righe:**
<!-- Una voce per riga significativa, sempre nella forma: "sposta un'etichetta (quale nome, verso quale oggetto)" oppure "modifica un oggetto (quale)", poi "dopo:" e l'elenco dei nomi che guardano lo stesso oggetto. Se non sai, scrivi "non so" e la tua ipotesi. Aggiungi tu le righe che mancano. -->
- `mirror = log` →  crea etichetta mirror e la assegna allo stesso oggetto puntato da log
- `log = []   (livello di modulo)` →  assegna al log un altra lista vuota (nuovo oggetto)
- `log.append("x")   (livello di modulo)` →  aggiorna la lista e aggiunge "x" in coda
- `log = []   (dentro restart)` →  crea una nuova lista e la da alla label log ma nello scope delle funzione 
- `log.append("x")   (dentro restart)` →  aggiunge in coda "x" alla lista puntata da log nello scope della funzione
- `result = restart(session)` →  assegna a result il risultato della funzione quindi ["x"], session resta invariato

**Previsione:**
<!-- Output ESATTO, una riga per ogni print, dentro un blocco di codice. Vedi "Output esatto" nel README. -->
```
["start"]
["x"]
["start"]
["x"]
false
```

**Sicurezza:** <!-- un numero da 1 a 5 -->
5

**Ipotesi alternativa e output che produrrebbe:**
<!-- Obbligatoria se la sicurezza è 1, 2 o 3: una seconda spiegazione plausibile e, in un blocco di codice, l'output ESATTO che darebbe. Deve essere diverso dalla tua previsione: se le due ipotesi danno lo stesso output, non sono due ipotesi. Se la sicurezza è 4 o 5 scrivi "no". -->
no

<!-- Fermati qui. Compila da qui in giù solo dopo aver chiuso le previsioni di tutti gli snippet. -->

**Output ottenuto:**
<!-- Incolla in un blocco di codice l'output reale. -->
```
['start']
['x']
['start']
['x']
False
```

**Righe in cui previsione e output differiscono:**
<!-- Confronto riga per riga, fatto da te. Se coincidono tutte scrivi "nessuna". -->
nessuna nel contenuto (dichiarato da Nick). Solo forma (annotazione dell'orchestratore su richiesta di Nick): virgolette doppie invece di apici singoli (quattro righe); `false` minuscolo invece di `False`.

**Dopo la verifica, la previsione era giusta (si/no):**
si
<!-- Se hai scritto "no" compila tutto lo scarto, nell'ordine. Se hai scritto "si" lascia vuoti i campi seguenti. -->
**Scarto - spiegazione:**
<!-- Cosa pensavi, cosa succede davvero, perché. Con i nomi veri del codice. -->

**Scarto - esperimento:**
<!-- Il codice REPL che provera' la tua spiegazione, in un blocco di codice. Nomi in inglese e per ruolo. Non eseguirlo ancora. -->

**Scarto - atteso (scritto prima di eseguire):**
<!-- Una riga "Atteso: <output esatto> perché <la spiegazione che stai mettendo alla prova>". Una riga per ogni blocco di esperimento. Se non sai cosa scrivere, non hai ancora un'ipotesi. -->

**Scarto - ottenuto:**
<!-- Incolla ciò che è uscito, in un blocco di codice. -->

**Scarto - la spiegazione regge (si/no):**

**Scarto - nuova spiegazione:**
<!-- Solo se hai scritto "no" sopra: la spiegazione corretta e l'esperimento (con la sua riga "Atteso") che la conferma. Altrimenti lascia vuoto. -->

---

## Snippet 4
**Codice:**
```python
# Snippet 4 - predict every printed line.
def grow(collection):
    collection += (5,)
    return collection


as_list = [1, 2]
as_tuple = (1, 2)
grown_list = grow(as_list)
grown_tuple = grow(as_tuple)
print(as_list)
print(as_tuple)
print(grown_list is as_list)
print(grown_tuple == as_tuple)
```

**Righe:**
<!-- Una voce per riga significativa, sempre nella forma: "sposta un'etichetta (quale nome, verso quale oggetto)" oppure "modifica un oggetto (quale)", poi "dopo:" e l'elenco dei nomi che guardano lo stesso oggetto. Se non sai, scrivi "non so" e la tua ipotesi. Aggiungi tu le righe che mancano. -->
- `collection += (5,)   (chiamata con as_list)` →  aggiunge il 5 in coda, sta modificando l'oggetto passato come parametro
- `collection += (5,)   (chiamata con as_tuple)` →  crea una nuova tupla con il 5 in coda, l'oggetto originale non può essere modificato
- `grown_list = grow(as_list)` →  assegna alla label grown_list l'oggetto lista modificato 
- `grown_tuple = grow(as_tuple)` →  assegna a grown_tuple il nuovo oggetto tupla creato dentro la funzione

**Previsione:**
<!-- Output ESATTO, una riga per ogni print, dentro un blocco di codice. Vedi "Output esatto" nel README. -->
```
[1,2,5]
(1,2)
True
False
```

**Sicurezza:** <!-- un numero da 1 a 5 -->
5
**Ipotesi alternativa e output che produrrebbe:**
<!-- Obbligatoria se la sicurezza è 1, 2 o 3: una seconda spiegazione plausibile e, in un blocco di codice, l'output ESATTO che darebbe. Deve essere diverso dalla tua previsione: se le due ipotesi danno lo stesso output, non sono due ipotesi. Se la sicurezza è 4 o 5 scrivi "no". -->
no

<!-- Fermati qui. Compila da qui in giù solo dopo aver chiuso le previsioni di tutti gli snippet. -->

**Output ottenuto:**
<!-- Incolla in un blocco di codice l'output reale. -->
```
[1, 2, 5]
(1, 2)
True
False
```

**Righe in cui previsione e output differiscono:**
<!-- Confronto riga per riga, fatto da te. Se coincidono tutte scrivi "nessuna". -->
nessuna nel contenuto (dichiarato da Nick). Solo forma (annotazione dell'orchestratore su richiesta di Nick): lista e tupla senza spazio dopo le virgole.

**Dopo la verifica, la previsione era giusta (si/no):** si

<!-- Se hai scritto "no" compila tutto lo scarto, nell'ordine. Se hai scritto "si" lascia vuoti i campi seguenti. -->
**Scarto - spiegazione:**
<!-- Cosa pensavi, cosa succede davvero, perché. Con i nomi veri del codice. -->

**Scarto - esperimento:**
<!-- Il codice REPL che provera' la tua spiegazione, in un blocco di codice. Nomi in inglese e per ruolo. Non eseguirlo ancora. -->

**Scarto - atteso (scritto prima di eseguire):**
<!-- Una riga "Atteso: <output esatto> perché <la spiegazione che stai mettendo alla prova>". Una riga per ogni blocco di esperimento. Se non sai cosa scrivere, non hai ancora un'ipotesi. -->

**Scarto - ottenuto:**
<!-- Incolla ciò che è uscito, in un blocco di codice. -->

**Scarto - la spiegazione regge (si/no):**

**Scarto - nuova spiegazione:**
<!-- Solo se hai scritto "no" sopra: la spiegazione corretta e l'esperimento (con la sua riga "Atteso") che la conferma. Altrimenti lascia vuoto. -->

---

## Snippet 5
**Codice:**
```python
# Snippet 5 - predict every printed line.
original = {"name": "ada", "tags": ["x"], "scores": [1, 2]}
snapshot = dict(original)

snapshot["tags"] += ["y"]
snapshot["name"] += "!"
snapshot["scores"] = [9]

print(original)
print(snapshot)
print(snapshot["tags"] is original["tags"])
print(snapshot["scores"] is original["scores"])
```

**Righe:**
<!-- Una voce per riga significativa, sempre nella forma: "sposta un'etichetta (quale nome, verso quale oggetto)" oppure "modifica un oggetto (quale)", poi "dopo:" e l'elenco dei nomi che guardano lo stesso oggetto. Se non sai, scrivi "non so" e la tua ipotesi. Aggiungi tu le righe che mancano. -->
- `snapshot = dict(original)` →  ipotesi1: costruisce un nuovo dizionario con le copie dei valori, ipotesi2: nuovo dizionario con riferimenti agli oggetti del primo dizionario
- `snapshot["tags"] += ["y"]` →  aggiunge in coda alla lista di tags "y"
- `snapshot["name"] += "!"` →  aggiunge in coda "!" alla stringa name, quindi costruisce un nuovo oggetto stringa, essendo immutabile
- `snapshot["scores"] = [9]` →  aggiunge in cosa il 9 alla lista di scores

**Previsione:**
<!-- Output ESATTO, una riga per ogni print, dentro un blocco di codice. Vedi "Output esatto" nel README. -->
Ipotesi1:
```
{"name": "ada", "tags": ["x"], "scores": [1, 2]}
{"name": "ada!", "tags": ["x","y"], "scores": [1, 2, 9]}
false
false
```

**Sicurezza:** <!-- un numero da 1 a 5 -->
3

**Ipotesi alternativa e output che produrrebbe:**
<!-- Obbligatoria se la sicurezza è 1, 2 o 3: una seconda spiegazione plausibile e, in un blocco di codice, l'output ESATTO che darebbe. Deve essere diverso dalla tua previsione: se le due ipotesi danno lo stesso output, non sono due ipotesi. Se la sicurezza è 4 o 5 scrivi "no". -->
Ipotesi2:
```
{"name": "ada!", "tags": ["x","y"], "scores": [1, 2, 9]}
{"name": "ada!", "tags": ["x","y"], "scores": [1, 2, 9]}
true
true
```



<!-- Fermati qui. Compila da qui in giù solo dopo aver chiuso le previsioni di tutti gli snippet. -->

**Output ottenuto:**
<!-- Incolla in un blocco di codice l'output reale. -->
```
{'name': 'ada', 'tags': ['x', 'y'], 'scores': [1, 2]}
{'name': 'ada!', 'tags': ['x', 'y'], 'scores': [9]}
True
False
```


**Righe in cui previsione e output differiscono:**
<!-- Confronto riga per riga, fatto da te. Se coincidono tutte scrivi "nessuna". -->
le righe sono tutte sbagliate tranne il primo true
**Dopo la verifica, la previsione era giusta (si/no):**
no
<!-- Se hai scritto "no" compila tutto lo scarto, nell'ordine. Se hai scritto "si" lascia vuoti i campi seguenti. -->
**Scarto - spiegazione:**
<!-- Cosa pensavi, cosa succede davvero, perché. Con i nomi veri del codice. -->
io ho fatto due ipotesi e ho spiegato in entrambe cosa mi aspettavo, però ho letto male il codice
l'ipotesi che regge è che il costruttore non copia solo i valori ma proprio i puntatori agli oggetti agisce come un copy
ma non ho notato che il += sulle stringhe costruisce un nuovo oggetto e il snapshot["scores"] = [9] assegnava una nuova lista alla label

quindi per verificarlo faccio così




**Scarto - esperimento:**
<!-- Il codice REPL che provera' la tua spiegazione, in un blocco di codice. Nomi in inglese e per ruolo. Non eseguirlo ancora. -->
```
base = {"key1":[1,2,3]}
second = dict(base)
second["key1"] is base ["key1"] 
```
mi aspetto True
**Scarto - atteso (scritto prima di eseguire):**
<!-- Una riga "Atteso: <output esatto> perché <la spiegazione che stai mettendo alla prova>". Una riga per ogni blocco di esperimento. Se non sai cosa scrivere, non hai ancora un'ipotesi. -->
atteso : True
**Scarto - ottenuto:**
<!-- Incolla ciò che è uscito, in un blocco di codice. -->
True

**Scarto - la spiegazione regge (si/no):**
si
**Scarto - nuova spiegazione:**
<!-- Solo se hai scritto "no" sopra: la spiegazione corretta e l'esperimento (con la sua riga "Atteso") che la conferma. Altrimenti lascia vuoto. -->

---

## Chiusura delle previsioni
<!-- Compila dopo aver finito tutti i 5 snippet e prima di eseguire qualunque cosa. Si ricava dai tuoi campi, non a sentimento. -->
**Snippet con almeno un "non so" o sicurezza 3 o meno:**
1
**Stima dei giusti (su 5):**
4
<!-- Regola della consegna: gli snippet del campo precedente contano come sbagliati. La stima non può superare 5 meno quel numero. -->

---

## Sintesi e prova di trasferimento
**Il mio errore di ragionamento più frequente:**
<!-- Un errore, non "non conoscevo il linguaggio". Cita lo snippet. -->
il mio errore di ragionamento è che considero solo la mutabilità di un tipo per determinare come si comporta python

**Un caso di questo esercizio in cui la regola "mutabile o immutabile" non basta a decidere:**
<!-- Quale riga, quale snippet, e perché la regola tace o sbaglia. -->
in questo caso la lista è mutabile ma qui viene riassegnata snapshot["scores"] = [9]
**La mia regola:**
<!-- Scritta come domanda da farti su una riga di codice, con ciò che fai a seconda della risposta. -->
sulla riga che sto analizzando devo chiedermi: la label la stiamo spostando, o stiamo aggiornando l'oggetto che referenzia?

**Riga nuova - codice:**
```python
# Transfer line - predict every printed line.
def retag(record, tag):
    record["tags"] = record["tags"] + [tag]
    return record


row = {"tags": ["a"]}
same = retag(row, "b")
print(row)
print(same is row)
```

**Riga nuova - spiegazione:**
<!-- Applica la tua regola alla funzione retag e alla riga della sua seconda istruzione, riga per riga, nella forma dello snippet. Prima della previsione. -->
record["tags"] = record["tags"] + [tag]
questa riga sta riassegnando la label ad una nuova lista che è il risultato dell'operazione di somma di due liste

**Riga nuova - previsione:**
<!-- Output esatto, in un blocco di codice. -->
```
{'tags': ['a', 'b']}
True
```

**Riga nuova - sicurezza:**
5

**Riga nuova - output ottenuto:**
<!-- Dopo averla eseguita (puoi lanciare snippets/transfer.py). Blocco di codice. -->
```
{'tags': ['a', 'b']}
True
```

**La regola ha retto (si/no):**
si

**Se no, come cambio la regola:**
<!-- Solo se hai scritto "no". -->

---

## Nota di blocco
Solo se consegni con tentativo minimo: snippet esatto e punto esatto in cui non sai andare avanti; cosa hai provato.
