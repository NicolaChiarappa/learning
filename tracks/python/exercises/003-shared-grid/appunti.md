# Appunti — 003

## Prima di iniziare
(3-5 righe, dopo aver letto codice e regole e prima di eseguire qualsiasi cosa: cosa pensi che non vada e perché; un dubbio concreto; i casi limite che ricavi dalle regole.)

dubbio1 : Allora prima di iniziare ho già notato che la riga 16 e 17 potrebbero contenere un errore logico ovvero viene creato un oggetto [FREE] * seats_per_row con label free_row e poi la lista subito sotto costruisce "row" liste che secondo me puntano tutte alla stessa lista

dubbio 2: inoltre una cosa che mi sembra scorretta è modificare in quel modo la lista nella funzione close_row, perché la label viene assegnata ad un nuovo oggetto e qualcuno potrebbe star puntando a quell'oggetto che però sarà disallineato dall'attuale riga dopo la modifica, 
io modificherei la lista annidata invece che la lista contenitore


## Durante
(Per ogni esperimento o esecuzione: una riga "mi aspetto: ..." scritta prima, poi l'output copiato dal terminale.)

per verificare il dubbio sulla riga 16-17 farei questo esperimento nella shell
```python
FREE = "free"
free_row = [FREE] * 3
free_hall = [free_row for _ in range(5)]

for row in free_hall:
    print(id(row))
```


se ho ragione la shell stamperà "row" id tutti uguali
se ho torto gli id stampati saranno tutti diversi

output:
    
4369592064
4369592064
4369592064
4369592064
4369592064

dubbio 2: per verificare quello che ho detto mi immagino del codice client che usa la lista e interroga la lista "obiettivo" in momenti diversi tra questi due momenti lancio la funzione close_row e dovrei vedere come la seconda interrogazione non coincide con lo stato attuale della lista
non è propriamente un errore però si può evitare di creare incongruenze del genere andando a modificare l'oggetto stesso senza crearne un altro. 
Non riesco a vedere in quale caso ha senso che quella funzione crei un oggetto nuovo onestamente quindi potrei sbagliare
lo script è una cosa del genere

```python
def incorrect_close_row(hall, row):
    hall[row] = ["close"] * len(hall[row])

def correct_close_row(hall,row):
    for seat in hall[row]:
        seat = "close"

hall = list[list[str]]()

rows = 4
seat_per_row = 5

for _ in range(rows):
    hall.append(["free"] * seat_per_row)

second_row = hall[1]
incorrect_close_row(hall, 1)
result = hall[1] != second_row
print(result)  #Qui mi aspetto True

third_row = hall[2] 
correct_close_row(hall, 2)
ora hall[2] contiene tutte stringhe "close"
result = hall[2] != third_row 
print(result) ## Qui mi aspetto False
```



se ho torto l'output sarà 
false, false
oppure 
true, true

output:
True
False

tutti i test che testano una proprietà su una singola riga falliranno perché in realtà la lista è una sola visto che chi la costruisce istanzia un solo oggetto
quindi questi falliscono

```python
def test_book_seat_changes_only_that_seat():
    hall = build_hall(3, 2)
    book_seat(hall, 1, 0)
    assert hall == [["free", "free"], ["taken", "free"], ["free", "free"]]


def test_add_seat_grows_only_that_row():
    hall = build_hall(2, 2)
    add_seat(hall, 0)
    assert hall == [["free", "free", "free"], ["free", "free"]]


def test_close_row_closes_only_that_row():
    hall = build_hall(3, 2)
    close_row(hall, 1)
    assert hall == [["free", "free"], ["closed", "closed"], ["free", "free"]]
```



inoltre fallisce anche questo perché la funzione torna una lista di stringhe non interi

```python
def test_free_per_row_counts_free_seats():
    assert free_per_row(build_hall(2, 3)) == [3, 3]
```


### Prove ricostruite dopo
(Codice incollato da Nick in chat il 2026-10-15, solo riformattato dall'orchestratore, nell'ordine in cui è stato incollato. Aspettative ed esiti NON scritti prima.)

**Prova 1** (`close_row`)
```python
for seat in hall[row]:
    seat = CLOSED
```
Cosa mi aspettavo: mi aspettavo di modificare il valore di tutti gli elementi di hall[row]
Cosa è uscito: nulla, semplicemente seat non punta più all'oggetto della lista, ho solo spostato il label su un nuovo oggetto
Cosa ne ricavo: che non si modificano così i valori dentro un for, avrei dovuto fare una cosa simile 
```python  
i=0
... for _ in lista:
...     lista[i] = "closed"
...     i = i+1
```

**Prova 2** (`build_hall`)
```python
for row in range(rows-1):
    hall[row].append([FREE] * seats_per_row)
```
Cosa mi aspettavo: mi aspettavo di popolare hall di "rows" liste ognuna contenente "seats_per_row" free
Cosa è uscito: indexerror perché l'append funziona solo se in quella posizione c'è già una lista, cosa non vera per una lista vuota. inoltre avrei comunque popolato con rows-1 liste
Cosa ne ricavo: avrei dovuto fare l'append direttamente su hall per "rows" volte; il range con argomento x lavora da 0 a x-1 quindi non è necessario aggiungere il -1

**Prova 3** (`build_hall`)
```python
for row in range(rows):
    hall[row].append([FREE] * seats_per_row)
```
Cosa mi aspettavo: mi aspettavo di popolare hall di "rows" liste ognuna contenente "seats_per_row" free
Cosa è uscito: IndexError vedi sopra
Cosa ne ricavo: vedi sopra

**Prova 4** (`build_hall`)
```python
free_row = [FREE] * seats_per_row
return [free_row] * 2
```
Cosa mi aspettavo: di moltiplicare la lista
Cosa è uscito: invece il *2 moltiplica il contenuto della lista
Cosa ne ricavo: il moltiplicatore su una lista moltiplica i suoi elementi

**Prova 5** (`build_hall`)
```python
free_row = [FREE] * seats_per_row
return [list(free_row)] * 2
```
Cosa mi aspettavo: mi aspettavo che il contenuto moltiplicato (in questo caso le liste interne) fossero oggetti diversi
Cosa è uscito: tutte le liste erano un unico oggetto
Cosa ne ricavo: la moltiplicazione degli elementi di una lista produce solo nuovi riferimenti agli stessi oggetti


questo esperimento lo conferma:
```python
lista = [list(free_row)] * 2
... 
>>> 
>>> for e in lista:
...     id(e)
...     
4342123136
4342123136
```

avevo scritto un test per verificare la completa indipendenza tra due sale


```python
def test_two_hall_are_independent():
    hall = build_hall(3, 2)
    hall2 = build_hall(3, 2)

    assert id(hall2) != id(hall)

    ids = {id(row) for row in hall}
    assert len(ids) == len(hall)

    ids = {id(row) for row in hall2}
    assert len(ids) == len(hall2)
```

era debole perché testava gli id degli elementi delle due sale separtamente l'ho modificato così:


questa funzione lo bucava pur essendo scorretta
```python
default_last_row = list[str]()


def incorrect_build_hall(rows: int, seats_per_row: int) -> Hall:
    hall_obj = list[list[str]]()
    for _ in range(rows):
        hall_obj.append([FREE] * seats_per_row)
    hall_obj.append(default_last_row)

    return hall_obj

```

```python
def test_two_hall_are_independent():
    hall = incorrect_build_hall(3, 2)
    hall2 = incorrect_build_hall(3, 2)

    assert id(hall2) != id(hall)

    ids1 = {id(row) for row in hall}
    ids2 = {id(row2) for row2 in hall2}

    ids = ids1.union(ids2)
    assert len(ids) == len(hall) + len(hall2)
```


## Dopo
(Cosa era diverso da come pensavi; la scelta di correzione, "X invece di Y perché"; quali regole R1-R9 ritieni coperte dai test e quali no; quanti test nascosti su 10 pensi di passare; la regola che ti porti via.)

tutto ciò che credevo fosse diverso è scritto nelle prove che ho fatto sopra, leggi quelle,
la correzione fatta sulla build hall deriva direttamente dal fatto che la regola R2 chiede indipendenza delle righe
questo errore spiega il bug che trovano i clienti: conteggi sfasati, modifiche accidentali ecc, 
la funzione di close_row mi sembra più sicura se modifiche l'oggetto stesso senza crearne uno nuovo
la funzione di free_row sbagliava solo il tipo di ritorno

le regole coperte secondo me sono la 1, 2,3,4,5,6,7,9
il codice non copre nessun caso limite, non fa controlli di nessun tipo

quindi mi aspetto di fallire tutti i test che riguardano questi casi, il resto credo di superarli

(.venv) nicolachiarappa@macbookair 003-shared-grid %   python -m pytest -q                                                                                                                               
                                                                                                                                                                                                           
                                                                                                                                                                                                           
  .............                                                                                                                                                                                            
  [100%]                                                                                                                                                                                                   
  13 passed in 0.02s                                      
