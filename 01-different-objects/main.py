unique = set()
for obj in objects:
    unique.add(id(obj))
print(len(unique))
