# Snippet 6 - predict every printed line.
original = [10, 20, 30] ## assegna la lista a original
duplicate = original.copy() #crea una copia, quindi oggetto diverso, id diverso
print(original == duplicate, original is duplicate) ## True, False

duplicate[0] = 99 ## asegna 99 al primo elemento della lista
print(original) ##[10, 20, 30]
print(duplicate) ##[99, 20, 30]
