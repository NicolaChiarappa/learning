# Snippet 4 - predict every printed line.
def grow(collection):
    collection += (5,)
    return collection


as_list = [1, 2]
as_tuple = (1, 2)
grown_list = grow(as_list)
grown_tuple = grow(as_tuple)
print(as_list)
print(as_tuple)
print(grown_list is as_list)
print(grown_tuple == as_tuple)
