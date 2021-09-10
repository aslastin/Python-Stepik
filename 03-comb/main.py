def comb(n, k, _cache=None):
    if _cache is None:
        _cache = {}
    pair = (n, k)
    if pair in _cache:
        return _cache[pair]
    if n < k:
        return 0
    elif k == 0:
        return 1
    _cache[pair] = comb(n - 1, k, _cache) + comb(n - 1, k - 1, _cache)
    return _cache[pair]


n, k = map(int, input().split())
print(comb(n, k))
