# Snippet 1 - predict every printed line.
names = ["ada", "bob"]
names_alias = names
names += ["eve"]
print(names_alias)

ids = (1, 2)
ids_alias = ids
ids += (3,)
print(ids_alias)
print(ids)

label = "ab"
label_alias = label
label += "c"
print(label_alias)
