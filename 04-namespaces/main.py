def createNs(d, ns, parent=None):
    d[ns] = {'Vars': set(), 'Parent': parent}


def getNs(d, ns, var):
    if ns in d:
        cur = d[ns]
        if var in cur['Vars']:
            return ns
        return getNs(d, cur['Parent'], var)
    return None


n = int(input())
d = {}
for i in range(n):
    op, ns, arg = input().split()
    if op == 'create':
        createNs(d, ns, arg)
    elif op == 'add':
        if ns not in d:
            createNs(d, ns)
        d[ns]['Vars'].add(arg)
    elif op == 'get':
        print(getNs(d, ns, arg))
