# Risposte — 001

Compila ogni campo. Un campo vuoto o lasciato col testo di esempio fa fallire i test di completezza.

Previsioni terminate alle: 18:36
Verifica iniziata alle: 18:40
Quanti snippet su 9 penso di aver previsto giusti (prima di verificare): 7

---

## Snippet 1
**Previsione:**
```
[7,9,4,10]
True
```

**Spiegazione:**
- `scores = [7, 9, 4]`: inizializza una lista e assegna la label "scores"
- `backup = scores`: la label "backup" punta allo stesso oggetto di scores
- `backup.append(10)`: essendo la lista mutabile, l'oggetto lista diventa [7,9,4,10]

**Sicurezza (1-5):** 5

**Dopo la verifica, la previsione era giusta (si/no):** si

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**

---

## Snippet 2
**Previsione:**
```
[7,9,4]
[7,9,4,10]
False
```

**Spiegazione:**
- `scores = [7, 9, 4]`: inizializza una lista e assegna la label "scores"
- `backup = scores`: la label "backup" punta allo stesso oggetto di scores
- `backup = backup + [10]`: non so cosa fa l'operazione di somma fatta in questo modo su una lista, ipotizzando che costruisca un nuovo oggetto

**Sicurezza (1-5):** 3

**Dopo la verifica, la previsione era giusta (si/no):** si

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**

---

## Snippet 3
**Previsione:**
```
[7,9,4]
false
```

**Spiegazione:**
- `backup += [10]`: non so cosa fa l'operazione di somma fatta su una lista, ipotizzando che costruisca un nuovo oggetto a quel punto scores e backup puntano a liste diverse

**Sicurezza (1-5):** 3

**Dopo la verifica, la previsione era giusta (si/no):** no

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**
avevo ipotizzato che il + e il += costruivano un nuovo oggetto invece l'unico a costruire un nuovo oggetto è il + e veniva riassegnato alla stessa label
nel repl ho fatto questo
 scores = [7, 9, 4]
>>> backup = scores
>>> backup += [10]   
>>> print(backup)
[7, 9, 4, 10]
>>> print(scores)
[7, 9, 4, 10]
>>> print(scores is backup)
True
>>> backup = backup + [10]
>>> print(scores is backup)
False
>>> print(scores)
[7, 9, 4, 10]
>>> print(scores is backup)

---

## Snippet 4
**Previsione:**
```
"  ada lovelace "
"Ada Lovelace"
"  ada lovelace "
```

**Spiegazione:**
- `raw_name = "  ada lovelace "`: assegna a raw_name la stringa che è immutabile
- `raw_name.strip()`: il risultato viene perso
- `raw_name.title()`: il risultato viene perso
- `print(repr(raw_name))`: non so cosa fa la funzione di repr() probabile che stampi "  ada lovelace "
- `clean_name = raw_name.strip().title()`: clean_name fa riferimento all'oggetto stringa "Ada Lovelace"
- `print(repr(clean_name))`: non so cosa fa la funzione di repr() probabile che stampo "Ada Lovelace"
- `print(repr(raw_name))`: non so cosa fa la funzione di repr() probabile che stampi "  ada lovelace "

**Sicurezza (1-5):** 5

**Dopo la verifica, la previsione era giusta (si/no):** si

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**

---

## Snippet 5
**Previsione:**
```
True
False
True
[1,2,3]
True
```

**Spiegazione:**
- `morning = [1, 2, 3]`: assenga la lista al label morning
- `evening = [1, 2, 3]`: assenga una nuova lista al label evening
- `same_as_morning = morning`: assegna un'altra label allo stesso oggetto a cui punta morning
- `print(morning == evening)`: True il valore è lo stesso
- `print(morning is evening)`: False, l'oggetto è diverso, ovvero l'id
- `print(morning is same_as_morning)`: True, stesso oggetto
- `history = {"first": morning}`: Assegna un dict alla label history
- `morning.append(4)`: aggiunge un valore alla lista a cui punta morning
- `print(history["first"])`: non so se il dizionario ha una copia di morning oppure il riferimento io credo una copia quindi dico [1,2,3]
- `print(history["first"] == evening)`: True

**Sicurezza (1-5):** 3

**Dopo la verifica, la previsione era giusta (si/no):** no

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**
avevo ipotizzato che nel dizionario ci finiva una copia della lista invece è proprio l'oggetto stesso quindi nel repl ho fatto
 dizionario = {"lista": scores}
>>> dizionario
{'lista': [7, 9, 4, 10]}
>>> scores.append(11)
>>> dizionario
{'lista': [7, 9, 4, 10, 11]}
---

## Snippet 6
**Previsione:**
```
True, False
[10, 20, 30]
[99, 20, 30]
```

**Spiegazione:**
- `original = [10, 20, 30]`: assegna la lista a original
- `duplicate = original.copy()`: crea una copia, quindi oggetto diverso, id diverso
- `duplicate[0] = 99`: asegna 99 al primo elemento della lista

**Sicurezza (1-5):** 5

**Dopo la verifica, la previsione era giusta (si/no):** si

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**

---

## Snippet 7
**Previsione:**
```
["milk", "eggs"]
True
[milk, eggs, tea]
[milk, eggs, tea]
True
```

**Spiegazione:**
- `print(shopping)`: ["milk", "eggs"] perché la funzione add_item aggiunge in coda la stringa data "eggs"
- `print(result is shopping)`: True, perché a result è assegnato l'oggetto risultante dalla funzione, la funzione all'interno non fa altro che modificare l'oggetto preso in ingresso
- parte con `with_item`: questa sezione non lo so perché non ho capito l'operatore di somma come agisce sulla lista; ipotizzo che costruisca un nuovo oggetto, ma il risultato non cambia perché nella funzione il puntatore in ingresso viene riassegnato

**Sicurezza (1-5):** 3

**Dopo la verifica, la previsione era giusta (si/no):** no

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**
ho sbagliato perché credevo che quando la funzione fa 
 items = items + [item] il primo items è l'oggetto passato in ingresso invece è una variabile che vive esclusivamente nello scope della funzione
mentre se la funzione fosse stata così sarebbe stato diverso
 def with_item(items, item):
...     items += [item]
...     return items
...     
>>> shopping is with_item(shopping, "eggs")
True

Integrazione:
l'errore che ho commesso è aver pensato che le due funzioni si comportassero diversamente ma senza spiegare il perché:
la differenza sta nel fatto che la prima chiama append sulla lista passata in ingresso e la ritorna, invece la seconda riassegna alla label un altro oggetto e lo fa attraverso l'operazione di +
quindi deduciamo che l'operazione += si coporta come append, ovvero "incrementa" lo stesso oggetto e la label punta ancora a quello
mentre lista = lista + [10] costruisce un nuovo oggetto e lo assegna alla label, che nel caso della funzione è una label che ha scope interno alla funzione quindi items fuori dalla funzione vale ancora la lista "senza il 10"
per verificarlo ho fatto questa cosa

come si nota nell'ultimo output l'id cambia appena viene riassegnata la label
 
>>> def add_item(items, item):
...     items.append(item)
...     print(id(items))
...     return items
... 
... 
... def with_item(items, item):
...     items = items + [item]
...     print(id(items))
...     return items
...     
>>> lista = []
>>> with_item(lista, 1)
4306005376
[1]
>>> id(lista)
4306000064
>>> lista
[]
>>> add_item(lista)
Traceback (most recent call last):
  File "<python-input-30>", line 1, in <module>
    add_item(lista)
    ~~~~~~~~^^^^^^^
TypeError: add_item() missing 1 required positional argument: 'item'
>>> add_item(lista,1)
4306000064
[1]
>>> id(lista)
4306000064
>>> def add_item(items, item):
...     items.append(item)
...     print(id(items))
...     return items
... 
... 
... def with_item(items, item):
...     print(id(items))
...     items = items + [item]
...     print(id(items))
...     return items
...     
>>> with_item(lista, 1)
4306000064
4305993792
[1, 1]
>>> 


---

## Snippet 8
**Previsione:**
```
5
[6,6]
["x"]
[]
```

**Spiegazione:**
- `print(visits)`: 5 perché l'oggetto dato in ingresso alla funzione è un int, immutabile quindi il risultato della funzione va assegnato ad una label, visit è rimasto così com'era
- `print(daily_visits)`: [6,6] perché l'oggetto preso in ingresso è una lista di int quindi gli int dentro la lista sono altri oggetti ma la lista stessa è ancora puntata da daily_visits quindi "vede la modifica"
- `print(second)`: ["x"] perché first = second = [] assegna a due label lo stesso oggetto
- `print(fourth)`: [] perché  third, fourth = [], [] assegna due liste diverse

**Sicurezza (1-5):** 5

**Dopo la verifica, la previsione era giusta (si/no):** si

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**

---

## Snippet 9
**Previsione:**
```
{"starters": ["soup"], "mains": ["pasta"]}
{"starters": ["soup"], "mains": ["pasta"]}
false
false
```

**Spiegazione:**
- `shallow = menu.copy()`: non conosco la differenza tra copy e deepcopy, penso che la copy copi solo la struttura mentre deepcopy anche i valori allora

**Sicurezza (1-5):** 1

**Dopo la verifica, la previsione era giusta (si/no):** no

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**
avevo ipotizzato che il copy copiasse i la struttura mentre deepcopy anche i valori. Invece usando il repl ho capito che:
1. il copy costruisce un nuovo dizionario e i value puntano agli stessi ogetti del dizionario originale, quindi aggiornando sulla copia le modifiche sono riflesse sull'originale
2. il deepcopy copia i valori ma non i riferimenti agli oggetti quindi nuovo dizionario e nuovi oggetti nei value
quindi aggirnando la lista sulla copia (deepcopy) NON si aggiorna anche la lista sul dizionario originale

per verificarlo farò delle prove questo è quello che mi aspetto
dictionary = {"numbers": [1,2,3]}

dict_copy = dictionary.copy()
deep = copy.deepcopy(dictionary)
dict_copy["numbers"].append(4)
deep["numbers"].append(5)
dictionary["numbers"] stampa [1,2,3,4]
deep["numbers"] stampa [1,2,3,5]

output reale
>>> import copy
>>> dictionary = {"numbers": [1,2,3]}
... 
... dict_copy = dictionary.copy()
... deep = copy.deepcopy(dictionary)
... dict_copy["numbers"].append(4)
... deep["numbers"].append(5)
... 
>>> dictionary["numbers"] 
[1, 2, 3, 4]
>>> deep["numbers"]
[1, 2, 3, 5]
>>> 


inoltre nella riga shallow["desserts"] = ["cake"] si nota come viene aggiornato il dizionario di copia ma non quello originale, perché?
io ipotizzo che l'oggetto dizionario è diverso dalla copia quindi facendo 

shallow is menu avrò false
solo le liste di value sono gli stessi oggetti
quindi se aggiorno il DIZIONARIO e non la Lista/il value condiviso non vedrò la modifica nel dizionario originale
mi aspetto questi output

originale = {"key1": []}
copy = originale.copy()

originale is copy false

copy["key1"] is originale["key1"] True
copy["key2"] = [1,2,3]
originale["key2"] KeyError

output reale
>>> originale = {"key1": []}
... copy = originale.copy()
... 
>>> originale is copy
False
>>> copy["key1"] is originale["key1"]
True
>>> copy["key2"] = [1,2,3]
>>> originale["key2"]
Traceback (most recent call last):
  File "<python-input-46>", line 1, in <module>
    originale["key2"]
    ~~~~~~~~~^^^




---

## Snippet 10 (facoltativo)
**Previsione:**
```
([1,9], 2)
TypeError
([1,9], 2)
?
?
```

**Spiegazione:**
- `record = ([1], 2)`: allora la tupla è immutabile ma immagino che la lista il suo interno lo sia
- `record[0].append(9)`: quindi questa riga potrebbe funzionare
- `record[1] += 1`: io credo che qui abbiamo un typeerror perché stiamo cercando di sostituire un oggetto nella tupla che però è immutabile quindi "TypeError"
- ultimo blocco (`record[0] += [5]`): Non so come funziona il + sulle liste

**Sicurezza (1-5):** 3

**Dopo la verifica, la previsione era giusta (si/no):** no

**Se no, cosa avevo sbagliato, perché, e quale prova ho fatto nel REPL:**
ho dimenticato di aggiornare la risposta ma l'avrei fatta corretta pur non sapendo come funziona il +, lo si deduce dalle risposte che ho dato negli esercizi precedenti
---

## Sintesi finale (3-5 righe)
Qual è l'errore di ragionamento che hai fatto più spesso? C'è una regola che adesso applicheresti a una riga di codice che non hai mai visto?
**Risposta:**
non ho fatto propriamente errori di ragionamento, gli errori che ho fatto sono dovuti più al fatto che non conoscevo alcuni comportamenti del linguaggio e le mie ipotesi spesso si sono rivelate sbagliate
## Nota Django (facoltativa)
Django controlla in fase di avvio i campi del modello e per alcuni (per esempio `JSONField`) segnala come sospetto un default passato come istanza (`default=[]`) invece che come callable (`default=list`). Usando solo ciò che hai visto negli snippet 1-9, scrivi un'ipotesi: che problema può nascere? Poi provala nel REPL con un esempio tuo, senza Django.
**Risposta:** il problema che può nascere è che quella lista o oggetto passato come default può essere puntato da altre label e non sempre si sa, è più facile modificare quel default senza accorgersi
>>> class Oggetto:
...     def __init__(lista):
...         self.lista = lista
...         
>>> def costruisci(lista=[]):
...     oggetto = Oggetto(lista)
...     return oggetto
...     
>>> oggetto1 = costruisci()
Traceback (most recent call last):
  File "<python-input-2>", line 1, in <module>
    oggetto1 = costruisci()
  File "<python-input-1>", line 2, in costruisci
    oggetto = Oggetto(lista)
TypeError: Oggetto.__init__() takes 1 positional argument but 2 were given
>>> class Oggetto:
...     def __init__(self, lista):
...         self.lista = lista
...         
>>> oggetto1 = costruisci()
>>> oggetto2 = costruisci()
>>> oggetto1.lista is oggetto2.lista
True
>>> oggetto1.lista.append(1)
>>> oggetto2.lista
[1]

Quindi quando in una funzione inserisco un default sto passando un oggetto che useranno tutte le chiamate a quella funzione? Non lo sapevo, credevo ne venisse costruito uno ogni volta che la chiamata veniva fatta
## Nota di blocco (solo se consegni con tentativo minimo)
Snippet esatto e punto esatto in cui non sai andare avanti; cosa hai provato:
