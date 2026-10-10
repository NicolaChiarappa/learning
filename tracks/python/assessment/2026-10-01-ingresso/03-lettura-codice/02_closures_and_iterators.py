# TASK: predict the exact output (every print line), then explain WHY for each line.

multipliers = [lambda x: x * i for i in range(1, 4)]
print([m(10) for m in multipliers])

squares = (n * n for n in range(5))
print(sum(squares))
print(sum(squares))
print(4 in squares)

nums = [1, 2, 3, 4, 5, 6]
it = iter(nums)
pairs = list(zip(it, it))
print(pairs)

first, *middle, last = "abcde"
print(first, middle, last)

data = [3, 8, 1]
if (n := len(data)) > 2:
    print(f"{n} items")
