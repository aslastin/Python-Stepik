class multifilter:
    def judge_half(pos, neg):
        return pos >= neg

    def judge_any(pos, neg):
        return pos >= 1

    def judge_all(pos, neg):
        return neg == 0

    def __init__(self, iterable, *funcs, judge=judge_any):
        self.iterable = iterable
        self.funcs = funcs
        self.judge = judge
        self.i = 0

    def __next__(self):
        while self.i < len(self.iterable):
            pos, neg = 0, 0
            x = self.iterable[self.i]
            for f in self.funcs:
                if f(x):
                    pos += 1
                else:
                    neg += 1
            self.i += 1
            if self.judge(pos, neg):
                return x
        raise StopIteration

    def __iter__(self):
        return self
