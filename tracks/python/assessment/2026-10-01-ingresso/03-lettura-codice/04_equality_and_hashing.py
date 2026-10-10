# TASK: predict the output of every print line and explain WHY.
# The exact wording of error messages does not matter: say which exception and what causes it.

from dataclasses import dataclass, field


@dataclass
class Tag:
    name: str


@dataclass(frozen=True)
class FrozenTag:
    name: str
    aliases: list[str] = field(default_factory=list)


class Product:
    def __init__(self, sku):
        self.sku = sku

    def __eq__(self, other):
        return isinstance(other, Product) and self.sku == other.sku

    def __hash__(self):
        return hash(self.sku)


print(Tag("a") == Tag("a"))
try:
    print({Tag("a")})
except TypeError as e:
    print("TypeError:", e)

ft = FrozenTag("x")
try:
    print(hash(ft))
except TypeError as e:
    print("TypeError:", e)

p = Product("A1")
catalog = {p: "first"}
p.sku = "B2"
print(p in catalog)
print(Product("A1") in catalog)
print(len(catalog))
