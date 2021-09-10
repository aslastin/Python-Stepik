class MoneyBox:
    def __init__(self, capacity):
        self.bal = 0
        self.capacity = capacity

    def can_add(self, v):
        return self.bal + v <= self.capacity

    def add(self, v):
        if not self.can_add(v):
            raise ValueError(f"Can not add {v} money to box")
        self.bal += v
