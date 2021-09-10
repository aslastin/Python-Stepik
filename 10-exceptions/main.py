def need_to_catch(e, excepts, was, visited=None):
    if visited is None:
        visited = set()
    if e in visited:
        return True
    visited.add(e)
    if e in was:
        return False
    for anc in excepts[e]:
        if not need_to_catch(anc, excepts, was, visited):
            return False
    return True


n = int(input())
excepts = {}
for i in range(n):
    es = input().split()
    excepts[es[0]] = [] if len(es) == 1 else es[2:]

m = int(input())
was = set()
for i in range(m):
    e = input()
    if not need_to_catch(e, excepts, was):
        print(e)
    was.add(e)
