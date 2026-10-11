# Snippet 3 - predict every printed line.
scores = [7, 9, 4]
backup = scores
backup += [10]      ## non so cosa fa l'operazione di somma fatta su una lista, ipotizzando che costruisca un nuovo oggetto a quel punto scores e backup puntano a liste diverse
print(scores) #[7,9,4]
print(scores is backup) ##false
