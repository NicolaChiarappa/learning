# Snippet 10 (optional challenge) - predict every printed line.
record = ([1], 2)   ##allora la tupla è immutabile ma immagino che la lista il suo interno lo sia
record[0].append(9)    ##quindi questa riga potrebbe funzionare
print(record)           ##([1,9], 2)

try:
    record[1] += 1
except TypeError:
    print("TypeError")  ## io credo che qui abbiamo un typeerror perché stiamo cercando di sostituire un oggetto nella tupla che però è immutabile quindi "TypeError"
print(record)  ##([1,9], 2)


#Non so come funziona il + sulle liste
try:
    record[0] += [5]
except TypeError:
    print("TypeError again")
print(record)
