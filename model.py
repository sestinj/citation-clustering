import torch


class Model(torch.nn.Module):
    def __init__(self, input_channels, output_channels=5, hidden_layers=[8, 8, 16, 16, 8, 8]):
        super(Model, self).__init__()
        self.linears = []
        hidden_layers.insert(0, input_channels)
        hidden_layers.append(output_channels)
        self.hidden_layers = hidden_layers
        for i in range(len(hidden_layers) - 1):
            linear = torch.nn.Linear(hidden_layers[i], hidden_layers[i+1])
            self.add_module("Linear " + str(i), linear)
            if not i == len(hidden_layers) - 2:
                self.add_module("Batch Norm " + str(i), torch.nn.BatchNorm1d(hidden_layers[i+1]))

        self.add_module("Sigmoid", torch.nn.Sigmoid())

    def forward(self, x):
        for module in enumerate(self.modules()):
            x = module(x)
        return x.index