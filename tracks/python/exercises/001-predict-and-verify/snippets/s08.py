# Snippet 8 - predict every printed line.
def bump(counter):
    counter += 1
    return counter


def bump_all(counters):
    for position in range(len(counters)):
        counters[position] += 1


visits = 5
bump(visits)
print(visits) ## 5 perché l'oggetto dato in ingresso alla funzione è un int, immutabile quindi il risultato della funzione va assegnato ad una label, visit è rimasto così com'era

daily_visits = [5, 5]
bump_all(daily_visits)
print(daily_visits) #[6,6] perché l'oggetto preso in ingresso è una lista di int quindi gli int dentro la lista sono altri oggetti ma la lista stessa è ancora puntata da daily_visits quindi "vede la modifica"

first = second = []
first.append("x")
third, fourth = [], []
third.append("y")
print(second) ## ["x"] perché first = second = [] assegna a due label lo stesso oggetto
print(fourth) ## [] perché  third, fourth = [], [] assegna due liste diverse
