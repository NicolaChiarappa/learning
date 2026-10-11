# Snippet 5 - predict every printed line.
original = {"name": "ada", "tags": ["x"], "scores": [1, 2]}
snapshot = dict(original)

snapshot["tags"] += ["y"]
snapshot["name"] += "!"
snapshot["scores"] = [9]

print(original)
print(snapshot)
print(snapshot["tags"] is original["tags"])
print(snapshot["scores"] is original["scores"])
