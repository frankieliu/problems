import numpy as np


# backward
# Read deepnotes.io/softmax-crossentropy
# Nice explanation for cross-entropy:
# www.quora.com/Whats-an-intuitive-way-to-think-of-cross-entropy
def backward(model, X, y, probs, a1, reg_lambda, epsilon):

    W1, b1, W2, b2 = model['W1'], model['b1'], model['W2'], model['b2']

    delta3 = probs
    num_examples = X.shape[0]
    delta3[range(num_examples), y] -= 1

    # \del L / \del W2 = a_1^T (\hat{y} - y)
    dW2 = (a1.T).dot(delta3)
    # \del L / \del b2 = (\hat{y} - y)
    db2 = np.sum(delta3, axis=0, keepdims=True)

    delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))
    # \del L / \del W1 = x^T (1-|a_1|^2) \delta_3 W_2^T
    dW1 = np.dot(X.T, delta2)
    db1 = np.sum(delta2, axis=0)

    # Add regularization terms (b1 and b2 don't have regularization terms)
    dW2 += reg_lambda * W2
    dW1 += reg_lambda * W1

    # Gradient descent parameter update
    W1 += -epsilon * dW1
    b1 += -epsilon * db1
    W2 += -epsilon * dW2
    b2 += -epsilon * db2

    # Assign new parameters to the model
    model = {'W1': W1, 'b1': b1, 'W2': W2, 'b2': b2}

    return model
