import numpy as np

def probs(model, X, y):

    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    yhat = np.argmax(probs, axis=1)

    # z1 output of first layer before non-linear function
    # a1 output of first layer after non-linear function
    return {'z1': z1, 'a1': a1, 'probs': probs, 'yhat': yhat}
