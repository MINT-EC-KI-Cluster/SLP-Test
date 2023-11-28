class Connection:
    def __init__(self):
        self.weight = 0.0
        self.input = 0.0

    def set_weight(self, weight):
        self.weight = weight

    def set_input(self, input):
        self.input = input

    def forward(self):
        return self.input * self.weight
