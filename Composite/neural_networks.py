from abc import ABC
from collections.abc import Iterable


class Connectable(Iterable, ABC):
    def connect_to(self, other):
        if self == other:
            return

        for s in self:
            for o in other:
                s.outputs.append(o)
                o.inputs.append(s)

# class Neuron:
class Neuron(Connectable):
    def __init__(self, name):
        self.name = name
        self.inputs = []
        self.outputs = []

    def __iter__(self): # for turning a single value -> collection
        yield self

    def __str__(self):
        return f'{self.name}, {len(self.inputs)} inputs, {len(self.outputs)} outputs'

    # def connect_to(self, other):
    #     self.outputs.append(other)
    #     self.inputs.append(self)


# What if we want Large groups of Neuron rather than a single Neuron?

# class NeuronLayer(list):
class NeuronLayer(list, Connectable):
    def __init__(self, name, count):
        super().__init__()
        self.name = name
        for x in range(0, count):
            self.append(Neuron(f'{name}-{x}'))
        
    def __str__(self):
        return f'{self.name} with {len(self)} neurons'

# However, we need to connect the neurons

def connect_to(self, other):
    if self == other:
        return 
    
    for s in self:   
        for o in other: # Error since its a scalar value. Turn the scalar value into a collection to solve this error
            s.outputs.append(o)
            o.inputs.append(s)


if __name__ == '__main__':
    neuron1 = Neuron('n1')
    neuron2 = Neuron('n2')
    layer1 = NeuronLayer('L1', 3)
    layer2 = NeuronLayer('L2', 4)

    # Error! 
    # Neuron.connect_to = connect_to
    # NeuronLayer.connect_to = connect_to

    neuron1.connect_to(neuron2)
    neuron1.connect_to(layer1)

    layer1.connect_to(neuron2)
    layer1.connect_to(layer2)

    print(neuron1)
    print(neuron2)
    print(layer1)
    print(layer2)

    # n1, 2 inputs, 2 outputs
    # n2, 0 inputs, 0 outputs
    # L1 with 3 neurons
    # L2 with 4 neurons
