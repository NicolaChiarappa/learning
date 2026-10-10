# TASK: predict the output of every print line (in order) and explain WHY.
# Then answer: why is the pattern used in `risky()` dangerous in real code?


def parse(value):
    try:
        return int(value)
    except ValueError:
        print("bad value")
        return None
    finally:
        print("parsed")


def risky():
    try:
        raise KeyError("missing")
    finally:
        return "finally wins"


def load(config):
    try:
        return config["port"]
    except KeyError as e:
        raise RuntimeError("no port") from e


print(parse("42"))
print(parse("x"))
print(risky())
try:
    load({})
except RuntimeError as e:
    print(type(e.__cause__).__name__, e.__suppress_context__)
try:
    load({"port": 1})["x"]
except Exception as e:
    print(type(e).__name__)
