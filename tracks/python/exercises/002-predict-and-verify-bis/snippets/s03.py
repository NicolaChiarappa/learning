# Snippet 3 - predict every printed line.
# Part A: module level.
log = ["start"]
mirror = log
log = []
log.append("x")
print(mirror)
print(log)


# Part B: the same line, inside a function.
def restart(log):
    log = []
    log.append("x")
    return log


session = ["start"]
result = restart(session)
print(session)
print(result)
print(result is session)
