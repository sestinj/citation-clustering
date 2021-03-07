import torch
from model import Model


PARAMS = {
    num_epochs: 25,
    train_proportion: 0.8
}

data = "DATA"

def split_data(data):
    test_proportion = (1.0 - train_proportion) / 2.0
    return data[:len(data)*PARAMS.train_proportion], data[len(data)*PARAMS.train_proportion:len(data)*(PARAMS.train_proportion+test_proportion)], data[len(data)*(PARAMS.train_proportion+test_proportion):]

def eval(data):


for epoch in PARAMS.num_epochs:
    optimizer = torch.optim.Adam(model.parameters(), lr=0.05)
    model = Model(8)

    train_data, val_data, test_data
    train(model)