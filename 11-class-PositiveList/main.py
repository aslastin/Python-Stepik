class NonPositiveError(BaseException):
    pass


class PositiveList(list):
    def append(self, x):
        if type(x) is not int:
            raise ValueError("Can append only integer")
        if x <= 0:
            raise NonPositiveError('x must be > 0, but was ' + str(x))
        super().append(x)
