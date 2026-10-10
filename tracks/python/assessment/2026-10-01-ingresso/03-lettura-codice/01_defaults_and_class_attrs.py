# TASK: predict the exact output (every print line), then explain WHY for each line.


class Basket:
    items = []

    def __init__(self, owner, tags=[]):
        self.owner = owner
        self.tags = tags

    def add(self, item):
        self.items.append(item)

    def tag(self, label):
        self.tags.append(label)


a = Basket("anna")
b = Basket("bruno")
a.add("apple")
b.add("bread")
a.tag("vip")
c = Basket("carla", tags=["new"])
c.tag("promo")
b.items = ["water"]
b.add("milk")

print(a.items)
print(b.items)
print(Basket.items)
print(b.tags)
print(c.tags)
print(a.tags is b.tags)
