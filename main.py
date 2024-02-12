import activiation_functions
from connection import Connection
from neuron import Neuron

if __name__ == '__main__':
    input_1 = Connection()
    input_2 = Connection()
    input_3 = Connection()

    neuron = Neuron([input_1, input_2, input_3], activiation_functions.identity)

    input_1.set_input(0)
    input_2.set_input(1)
    input_3.set_input(2)

    input_1.set_weight(0.1)
    input_2.set_weight(0.2)
    input_3.set_weight(0.3)

    # Kommentiere die jeweilige Zeile ein, um die Zwischenergebnisse zu sehen
    # print(input_1.forward())
    # print(input_2.forward())
    # print(input_3.forward())

    print(neuron.feedforward())
