class Auto:
    def __init__(self, sor):
        self.auto = sor[0]
        self.datum = int(sor[1])

    def __str__(self):
        return f"{self.auto}, {self.datum}"