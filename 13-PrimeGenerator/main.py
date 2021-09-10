def primes():
    was = []
    cur = 2
    while True:
        for x in was:
            if not cur % x:
                break
        else:
            was.append(cur)
            yield cur
        cur += 1
