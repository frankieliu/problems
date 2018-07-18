import numpy as np


# forward propagation
def forward(model, X, y):

    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']

    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    # z2_max = np.max(z2, axis=1, keepdims=True)
    # z3 = z2_max * np.array([1, 1])
    # z2 = z2 - z3
    exp_scores = np.exp(z2)
    # print("sum shape {}".format(np.sum(exp_scores, axis=1, keepdims=True).shape))
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    yhat = np.argmax(probs, axis=1)

    # z1 output of first layer before activation function
    # a1 output of first layer after activation function
    return {'z1': z1, 'a1': a1, 'probs': probs, 'yhat': yhat}
