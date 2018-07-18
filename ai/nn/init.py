import numpy as np


def initialize(nn_input_dim, nn_hdim, nn_output_dim):
    W1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
    b1 = np.zeros((1, nn_hdim))
    W2 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)
    b2 = np.zeros((1, nn_output_dim))
    return {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}
