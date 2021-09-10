class LoggableList(list, Loggable):
    def append(self, x):
        super().append(x)
        self.log(x)
