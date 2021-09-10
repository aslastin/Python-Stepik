s, t = input(), input()
i, cnt = 0, 0
while True:
    i = s.find(t, i) + 1
    if i:
        cnt += 1
    else:
        break
print(cnt)
