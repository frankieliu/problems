import numpy as np

def build_model(nn_input_dim, nn_output_dim, nn_hdim):
    np.random.seed(0)
    W1 = np.random.randn(nn_input_dim, nn_hdim) / np.sqrt(nn_input_dim)
    b1 = np.zeros((1, nn_hdim))
    W1 = np.random.randn(nn_hdim, nn_output_dim) / np.sqrt(nn_hdim)
    b1 = np.zeros((1, nn_output_hdim))
    model = {
        'W1': W1,
        'b1': b1,
        'W2': W2,
        'b2': b2
    }
