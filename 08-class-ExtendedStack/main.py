class ExtendedStack(list):
    def apply_op(self, op):
        if len(self) < 2:
            raise ValueError("Required at least 2 elements to apply an operation")
        self.append(eval(str(self.pop()) + op + str(self.pop())))

    def sum(self):
        self.apply_op('+')

    def sub(self):
        self.apply_op('-')

    def mul(self):
        self.apply_op('*')

    def div(self):
        self.apply_op('//')
