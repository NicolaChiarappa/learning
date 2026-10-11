# Snippet 5 - predict every printed line.
morning = [1, 2, 3] ## assenga la lista al label morning
evening = [1, 2, 3] ##  assenga una nuova lista al label evening
same_as_morning = morning ## assegna un'altra label allo stesso oggetto a cui punta morning

print(morning == evening)   ##True il valore è lo stesso
print(morning is evening)   ## False, l'oggetto è diverso, ovvero l'id
print(morning is same_as_morning)   ## True, stesso oggetto

history = {"first": morning}    #Assegna un dict alla label history
morning.append(4)               #aggiunge un valore alla lista a cui punta morning
print(history["first"])         # non so se il dizionario ha una copia di morning oppure il riferimento io credo una copia quindi dico [1,2,3]
print(history["first"] == evening)  #True
