# CHIAVE — 002 — RISERVATA AL REVIEWER (Nick non aprire prima di consegnare)

Output verificati con Python 3.14 (`.venv` del repository), lanciando ogni file con `python -I`.

## Snippet 1
```
['ada', 'bob', 'eve']
(1, 2)
(1, 2, 3)
ab
```
`names += ["eve"]` estende la lista sul posto e riassegna `names` allo stesso oggetto: `names_alias` vede la modifica. Su tupla e stringa non esiste un'estensione sul posto: `+=` si comporta come `= ... +`, costruisce un oggetto nuovo e sposta solo l'etichetta del nome a sinistra; l'alias resta sul vecchio oggetto. Stesso simbolo, effetto che dipende dall'oggetto (E005).

## Snippet 2
```
[10, 20, 30, 40]
[[10, 20, 30, 40], [10, 20, 30, 40]]
True
[10, 20, 30, 40]
[10, 20, 30, 40]
```
`menu` e `bundle` contengono riferimenti alla stessa lista di `base_prices`, non copie (E003). `menu["lunch"] = [99]` modifica il dict `menu` (cambia a cosa punta la chiave) e non tocca `base_prices` né `bundle`: la riga con indice a sinistra agisce sul dict. Le ultime due righe cercano chi pensa che l'assegnazione alla chiave "propaghi" a `base_prices`.

## Snippet 3
```
['start']
['x']
['start']
['x']
False
```
Parte A e parte B sono la stessa riga `log = []`: sposta un'etichetta (`log` a livello di modulo; il parametro `log` dentro `restart`), poi `append` modifica la lista nuova. Né `mirror` né `session` vedono nulla. Il `log` globale non viene toccato dalla funzione (il parametro è un nome locale). Chi risponde `['x']` alla terza riga ripete E002.

## Snippet 4
```
[1, 2, 5]
(1, 2)
True
False
```
Stessa riga `collection += (5,)`: sulla lista estende l'oggetto del chiamante (visibile in `as_list`, `grown_list is as_list`); sulla tupla crea un oggetto nuovo e sposta solo il parametro locale (`as_tuple` intatta, `grown_tuple != as_tuple`). Nessuna eccezione: `list += tuple` è lecito (estende con gli elementi di qualunque iterabile). Chi predice `TypeError` ha confuso `+=` con `+` (`names + (5,)` solleverebbe).

## Snippet 5
```
{'name': 'ada', 'tags': ['x', 'y'], 'scores': [1, 2]}
{'name': 'ada!', 'tags': ['x', 'y'], 'scores': [9]}
True
False
```
`dict(original)` è una copia superficiale: dict nuovo, valori condivisi. `snapshot["tags"] += ["y"]` modifica la lista condivisa (poi riassegna la chiave allo stesso oggetto): si vede in `original`. `snapshot["name"] += "!"` crea una stringa nuova e cambia solo la chiave di `snapshot`. `snapshot["scores"] = [9]` cambia solo la chiave di `snapshot`.

## Riga nuova (trasferimento)
```
{'tags': ['a', 'b']}
True
```
`record["tags"] = ...` ha un indice a sinistra: modifica il dict a cui `record` è attaccato, cioè `row`. Il valore assegnato è una lista nuova (`+`), ma il dict è lo stesso, quindi la modifica è visibile a chi chiama. Unisce snippet 3 (parametro) e 5 (riassegnare una chiave): chi ha interiorizzato "riassegnare dentro una funzione non si vede fuori" sbaglia qui, e va letto come E001/E002 non risolti.
