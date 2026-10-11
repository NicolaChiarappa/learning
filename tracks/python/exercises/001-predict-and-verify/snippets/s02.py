# Snippet 2 - predict every printed line.
scores = [7, 9, 4]  # inizializza una lista e assegna la label "scores"
backup = scores     # la label "backup" punta allo stesso oggetto di scores
backup = backup + [10]  #non so cosa fa l'operazione di somma fatta in questo modo su una lista, ipotizzando che costruisca un nuovo oggetto
print(scores)   ## [7,9,4]
print(backup)   ##[7,9,4,10]
print(scores is backup) #False
