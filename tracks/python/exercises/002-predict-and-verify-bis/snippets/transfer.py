# Transfer line - predict every printed line.
def retag(record, tag):
    record["tags"] = record["tags"] + [tag]
    return record


row = {"tags": ["a"]}
same = retag(row, "b")
print(row)
print(same is row)
