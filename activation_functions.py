import math


def identity(x): return x
def sigmoid(x): return 1 / (1 + math.exp(-x))
def tanh(x): return math.tanh(x)
def relu(x): return max(0, x)

