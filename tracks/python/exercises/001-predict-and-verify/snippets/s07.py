# Snippet 7 - predict every printed line.
def add_item(items, item):
    items.append(item)
    return items


def with_item(items, item):
    items = items + [item]
    return items


shopping = ["milk"]
result = add_item(shopping, "eggs")
print(shopping) ## ["milk", "eggs"] perché la funzione add_item aggiunge in coda la stringa data "eggs"
print(result is shopping)   ## True, perché a result è assegnato l'oggetto risultante dalla funzione, la funzione all'interno non fa altro che modificare l'oggetto preso in ingresso


## questa sezione non lo so perché non ho capito l'operatore di somma come agisce sulla lista
## ipotizzo che costruisca un nuovo oggetto
## ma il risultato non cambia perché nella funzione il puntatore in ingresso viene riassegnato
other = with_item(shopping, "tea")
print(shopping) ## [milk, eggs, tea]
print(other) ## [milk, eggs, tea]
print(other is shopping) ##True
