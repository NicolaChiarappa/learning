# Snippet 1 - predict every printed line.
scores = [7, 9, 4]      # inizializza una lista e assegna la label "scores"
backup = scores     # la label "backup" punta allo stesso oggetto di scores
backup.append(10)   # essendo la lista mutabile, l'oggetto lista diventa [7,9,4,10]
print(scores)   #[7,9,4,10]
print(scores is backup) #True
