import numpy as np

def calculate_loss(model, X, y, reg_lambda):
    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']
    num_examples = X.shape[0]
    z1 = X.dot(W1) + b1
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) + b2
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    logs = -np.log(probs[range(num_examples), y])
    data_loss = np.sum(logs)
    data_loss += reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
    return 1./num_examples * data_loss
