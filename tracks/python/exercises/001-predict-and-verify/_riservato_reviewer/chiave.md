# CHIAVE — 001 — RISERVATA AL REVIEWER (Nick non aprire prima di consegnare)

Output verificati con Python 3.14 (`.venv` del repository). Il comportamento mostrato è stabile su tutte le versioni 3.x recenti.

## Snippet 1
```
[7, 9, 4, 10]
True
```
`backup` è un'altra etichetta sullo stesso oggetto lista; `append` lo modifica.

## Snippet 2
```
[7, 9, 4]
[7, 9, 4, 10]
False
```
`backup + [10]` costruisce una lista nuova; `backup` viene spostato su di essa, `scores` resta sull'originale.

## Snippet 3
```
[7, 9, 4, 10]
True
```
`+=` su una lista estende l'oggetto sul posto e riassegna `backup` allo stesso oggetto. Contrasto con lo snippet 2.

## Snippet 4
```
'  ada lovelace '
'Ada Lovelace'
'  ada lovelace '
```
Le due chiamate isolate producono stringhe nuove subito scartate. `raw_name` non cambia mai.

## Snippet 5
```
True
False
True
[1, 2, 3, 4]
False
```
`morning == evening` (stesso valore), non lo stesso oggetto; `same_as_morning` è lo stesso oggetto; `history` tiene un riferimento a `morning`, quindi vede l'`append`; `history["first"]` ora ha 4 elementi, `evening` 3.

## Snippet 6
```
True False
[10, 20, 30]
[99, 20, 30]
```
`.copy()` produce un oggetto distinto con lo stesso contenuto.

## Snippet 7
```
['milk', 'eggs']
True
['milk', 'eggs']
['milk', 'eggs', 'tea']
False
```
`add_item` muta l'oggetto passato e restituisce lo stesso oggetto. `with_item` costruisce una lista nuova e sposta l'etichetta locale `items`: il chiamante non vede nulla.

## Snippet 8
```
5
[6, 6]
['x']
[]
```
`counter += 1` su un int sposta l'etichetta locale; il valore restituito è scartato. `counters[position] += 1` modifica gli elementi della lista condivisa. `first = second = []` crea un solo oggetto con due nomi; `third, fourth = [], []` ne crea due.

## Snippet 9
```
{'starters': ['soup', 'salad'], 'mains': ['pasta']}
{'starters': ['soup'], 'mains': ['pasta']}
True
False
```
`menu.copy()` copia solo il dict esterno: le liste interne sono condivise, quindi `append` su `starters` si vede in `menu`. `shallow["desserts"] = [...]` aggiunge una chiave solo a `shallow`. `deepcopy` duplica anche le liste interne.

## Snippet 10 (facoltativo)
```
([1, 9], 2)
TypeError
([1, 9], 2)
TypeError again
([1, 9, 5], 2)
```
La tupla è immutabile ma contiene una lista mutabile. `record[1] += 1` fallisce (non si può riassegnare l'elemento). `record[0] += [5]`: la lista viene estesa sul posto (`__iadd__`), poi l'assegnazione all'indice della tupla fallisce con `TypeError`: l'effetto sulla lista però è avvenuto.

## Nota Django (facoltativa, non valutata in modo rigido)
Risposta attesa: un default `[]` è un unico oggetto creato alla definizione del campo; tutte le istanze che lo usano senza passare un valore condividono la stessa lista (stesso meccanismo dello snippet 1). `default=list` è un callable chiamato a ogni istanza, che produce un oggetto nuovo. Sarà materia dell'esercizio 3 del modulo.
