# Snippet 2 - predict every printed line.
base_prices = [10, 20]
menu = {"lunch": base_prices}
bundle = [base_prices, base_prices]

base_prices.append(30)
bundle[0].append(40)
print(menu["lunch"])
print(bundle)
print(bundle[0] is bundle[1])

menu["lunch"] = [99]
print(base_prices)
print(bundle[1])
