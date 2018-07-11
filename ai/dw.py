
def dw(X, y, internal):
    delta3, a1 = internal['probs'], internal['a1']
    num_examples = X.shape[0]

    # yhat - y
    delta3[range(num_examples), y] -= 1
    delta2 = (1 - np.tanh(z1)
    dW2 = (a1.T).dot(delta3)
    db2 = delta3
    dW1 = X.T.
