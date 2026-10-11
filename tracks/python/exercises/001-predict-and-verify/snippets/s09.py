# Snippet 9 - predict every printed line.
import copy

menu = {"starters": ["soup"], "mains": ["pasta"]}
shallow = menu.copy() ## non conosco la differenza tra copy e deepcopy, penso che la copy copi solo la struttura mentre deepcopy anche i valori allora seguono i print che scrivo di seguito
deep = copy.deepcopy(menu)

shallow["starters"].append("salad")
shallow["desserts"] = ["cake"]

print(menu) ## {"starters": ["soup"], "mains": ["pasta"]}
print(deep) ## {"starters": ["soup"], "mains": ["pasta"]}
print(shallow["mains"] is menu["mains"]) ##false
print(deep["mains"] is menu["mains"]) ##false


