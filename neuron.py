class Neuron:
    def __init__(self, connections, activation_function):
        self.connections = connections
        self.activation_function = activation_function

    def feedforward(self):
        input_sum = 0
        for connection in self.connections:
            input_sum += connection.forward()
        return self.activation_function(input_sum)



