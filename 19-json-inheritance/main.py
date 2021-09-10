import json


def dfs(children_by_class, cls, visited=None):
    if visited is None:
        visited = set()
    if cls in visited:
        return 0
    cnt = 1
    visited.add(cls)
    for child in children_by_class[cls]:
        cnt += dfs(children_by_class, child, visited)
    return cnt


json_cs = input()
cs = json.loads(json_cs)
children_by_parent = {cls["name"]: set() for cls in cs}
for cls in cs:
    name = cls["name"]
    for parent in cls["parents"]:
        children_by_parent[parent].add(name)

cnt_by_name = {parent: dfs(children_by_parent, parent) for parent in children_by_parent}

for name in sorted(cnt_by_name):
    print(name, ":", cnt_by_name[name])
