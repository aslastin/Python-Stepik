def checkAnc(classes, anc, child, visited=None):
    if visited is None:
        visited = set()
    if child in visited:
        return False
    if anc == child:
        return True
    visited.add(child)
    for base in classes[child]:
        if checkAnc(classes, anc, base, visited):
            return True
    return False


n = int(input())
classes = {}
for _ in range(n):
    info = input().split()
    classes[info[0]] = info[2:] if len(info) > 1 else []

q = int(input())
for _ in range(q):
    anc, child = input().split()
    print('Yes' if checkAnc(classes, anc, child) else 'No')
