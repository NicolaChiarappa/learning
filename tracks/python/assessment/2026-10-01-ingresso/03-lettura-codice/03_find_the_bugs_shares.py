# TASK: this code has several problems (some are bugs, some are fragilities).
# 1. List ALL of them, ordered by severity (most serious first).
# 2. For each: what input triggers it and what the observable effect is.
# 3. Describe how you would fix the two most serious ones (prose or signatures, no full rewrite).
#
# Assume expenses.csv exists and contains lines like:  food,12.50


def share_by_category(expenses):
    """Return the percentage of total spending for each category.

    `expenses` is an iterable of (category, amount) pairs.
    """
    total = sum(amount for _, amount in expenses)
    shares = {}
    for category, amount in expenses:
        shares[category] = round(amount / total * 100, 1)
    return shares


def read_expenses(path):
    with open(path) as f:
        for line in f:
            category, amount = line.strip().split(",")
            yield category, float(amount)


print(share_by_category([("food", 30.0), ("rent", 70.0)]))
print(share_by_category(read_expenses("expenses.csv")))


def read_expenses(path):
    with open(path) as f:
        for line in f:
            category, amount = line.strip().split(",")
            yield category, float(amount)





